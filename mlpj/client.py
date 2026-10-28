import logging
import time
from dataclasses import dataclass
from typing import TYPE_CHECKING
 
import worlds._bizhawk as bizhawk
from worlds._bizhawk.client import BizHawkClient
 
from .itemdata import COUNTERS, ITEM_NAME_BY_ID
from .locations import LOCATION_DATA as BLOCK_DATA
 
if TYPE_CHECKING:
    from worlds._bizhawk.context import BizHawkClientContext
 
logger = logging.getLogger("Client")
 
DOMAIN = "System Bus"
 
# One entry per unique flag byte, so blocks that share a byte only cost one read.
BLOCK_FLAG_ADDRESSES = sorted({block.address for block in BLOCK_DATA.values()})
 
# How long to wait for a block's reward to actually show up in the inventory
# before giving up on taking it back.
REMOVAL_WINDOW_SECONDS = 10.0
 
 
@dataclass
class PendingRemoval:
    amount: int      # how much of the vanilla reward still has to be taken back
    deadline: float  # time.monotonic() after which we stop waiting for it
 
 
class PJClient(BizHawkClient):
    game = "Mario & Luigi: Paper Jam"
    system = "3DS"
 
    def __init__(self) -> None:
        super().__init__()
        # Blocks already seen as hit during this connection. None until the first read.
        self.handled_blocks: set[str] | None = None
        # Counter values from the previous tick (item ID -> value). None until the first read.
        self.last_counts: dict[int, int] | None = None
        # Vanilla rewards still waiting to be taken back (item ID -> amount owed).
        self.pending: dict[int, PendingRemoval] = {}
 
    async def validate_rom(self, ctx: "BizHawkClientContext") -> bool:
        try:
            system = await bizhawk.get_system(ctx.bizhawk_ctx)
 
            if system != "3DS":
                return False
 
        except bizhawk.RequestFailedError:
            return False
 
        ctx.game = self.game
        ctx.items_handling = 0b111
        ctx.want_slot_data = True
        ctx.watcher_timeout = 0.125  # tick faster so a block's reward is caught promptly
 
        self.handled_blocks = None
        self.last_counts = None
        self.pending = {}
 
        return True
 
    async def game_watcher(self, ctx: "BizHawkClientContext") -> None:
        if ctx.server is None or ctx.server.socket.closed or ctx.slot_data is None:
            return
 
        # Block flags and counters go in ONE read so they're a snapshot of the same frame.
        counter_ids = list(COUNTERS)
        try:
            reads = await bizhawk.read(
                ctx.bizhawk_ctx,
                [(address, 1, DOMAIN) for address in BLOCK_FLAG_ADDRESSES]
                + [(address, size, DOMAIN) for address, size in COUNTERS.values()],
            )
        except bizhawk.RequestFailedError:
            return
 
        flag_reads = reads[:len(BLOCK_FLAG_ADDRESSES)]
        counter_reads = reads[len(BLOCK_FLAG_ADDRESSES):]
 
        # bizhawk.read returns bytes objects; the 3DS is little-endian.
        flags = {address: raw[0] for address, raw in zip(BLOCK_FLAG_ADDRESSES, flag_reads)}
        counts = {item_id: int.from_bytes(raw, "little") for item_id, raw in zip(counter_ids, counter_reads)}
 
        for name in await self.check_blocks(ctx, flags):
            self.queue_removal(name)
 
        await self.process_removals(ctx, counts)
 
        # Next tick compares against this one. process_removals edits `counts` to match
        # what it wrote, so our own removals never look like the player gaining items.
        self.last_counts = counts
 
    async def check_blocks(self, ctx: "BizHawkClientContext", flags: dict[int, int]) -> list[str]:
        """Sends location checks for hit blocks and returns the blocks that were *just* hit."""
        hit_now = {
            name
            for name, block in BLOCK_DATA.items()
            if flags[block.address] & block.bitmask
        }
 
        if self.handled_blocks is None:
            # First read after connecting: anything already hit is old news.
            self.handled_blocks = set(hit_now)
            fresh: set[str] = set()
        else:
            # A block counts as freshly hit only if it's new this connection AND the server
            # doesn't already have it. That keeps reloading a save (flags jumping from
            # 0 to set) from looking like a block hit and eating real inventory.
            fresh = {
                name for name in hit_now - self.handled_blocks
                if BLOCK_DATA[name].location_id not in ctx.checked_locations
            }
            self.handled_blocks |= hit_now
 
        # Send every hit block the server doesn't have yet. Location checks are idempotent.
        # (If world.py adds a base offset to location IDs, add it here too.)
        new_locations = {BLOCK_DATA[name].location_id for name in hit_now} - ctx.checked_locations
        if new_locations:
            await ctx.send_msgs([{"cmd": "LocationChecks", "locations": sorted(new_locations)}])
 
        return sorted(fresh, key=lambda name: BLOCK_DATA[name].location_id)
 
    def queue_removal(self, name: str) -> None:
        block = BLOCK_DATA[name]
        item_name = ITEM_NAME_BY_ID.get(block.item_id, f"Unknown item {block.item_id}")
        logger.info(f"Block hit: {name} (vanilla contents: {block.quantity}x {item_name})")
 
        if block.item_id not in COUNTERS:
            logger.warning(
                f"Can't take back {block.quantity}x {item_name} from {name}: "
                f"no counter address for item ID {block.item_id}"
            )
            return
 
        deadline = time.monotonic() + REMOVAL_WINDOW_SECONDS
        pending = self.pending.get(block.item_id)
        if pending is None:
            self.pending[block.item_id] = PendingRemoval(block.quantity, deadline)
        else:
            pending.amount += block.quantity
            pending.deadline = deadline
 
    async def process_removals(self, ctx: "BizHawkClientContext", counts: dict[int, int]) -> None:
        """Takes back rewards as they land. Edits `counts` in place to match what it writes."""
        previous = self.last_counts if self.last_counts is not None else counts
 
        for item_id, pending in list(self.pending.items()):
            item_name = ITEM_NAME_BY_ID.get(item_id, f"Unknown item {item_id}")
 
            if time.monotonic() > pending.deadline:
                logger.warning(f"Never saw {item_name} go up; giving up on taking back {pending.amount}")
                del self.pending[item_id]
                continue
 
            current = counts[item_id]
            gained = current - previous[item_id]
            if gained <= 0:
                continue  # the reward hasn't landed yet
 
            # Only take back what actually arrived (e.g. less if the inventory was full),
            # and never more than the block owes.
            remove = min(gained, pending.amount)
            address, size = COUNTERS[item_id]
            new_value = current - remove
 
            # Guarded: the write only happens if the value is still what we just read.
            written = await bizhawk.guarded_write(
                ctx.bizhawk_ctx,
                [(address, new_value.to_bytes(size, "little"), DOMAIN)],
                [(address, current.to_bytes(size, "little"), DOMAIN)],
            )
 
            if not written:
                # Value changed under us. Keep the old baseline so the gain is still
                # visible next tick and we retry.
                counts[item_id] = previous[item_id]
                continue
 
            logger.info(f"Took back {remove}x {item_name} ({current} -> {new_value})")
            counts[item_id] = new_value
            pending.amount -= remove
            if pending.amount <= 0:
                del self.pending[item_id]
 
