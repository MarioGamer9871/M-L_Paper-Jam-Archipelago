import json
import logging
import os
import time
from dataclasses import dataclass
from typing import TYPE_CHECKING

import Utils
import worlds._bizhawk as bizhawk
from worlds._bizhawk.client import BizHawkClient

from .itemdata import COUNTER_CAPS, COUNTERS, GRANTS, ITEM_NAME_BY_ID
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

# FILL IN (strongly recommended): (address, bitmask) of a flag that is only set while a save is
# loaded and the inventory in RAM is the live one (not the title screen, and not a battle if
# battles use their own copy). While this is None, received items are given immediately,
# so connecting on the title screen would "give" them into memory that then gets overwritten.
READY_FLAG: tuple[int, int] | None = None

# Where the client remembers how many received items it has already given you.
RECEIVED_FILE = "pj_received_items.json"

# Move unlock flags, ordered from the most-significant bit to the least-significant bit.
MOVE_FLAGS_ADDRESS = 0x007BB3F4
MOVE_ITEM_FLAGS = {
    300: (0b00000001, "Dash Socks"),
    302: (0b00100000, "Trio Grab"),
    303: (0b01000000, "Trio Drill"),
    304: (0b10000000, "Trio Plane"),
}
PROGRESSIVE_HAMMERS_ITEM_ID = 301
PROGRESSIVE_HAMMER_FLAGS = (
    (0b00001000, "Hammer"),
    (0b00010000, "Trio Hammer"),
)


def received_key(ctx: "BizHawkClientContext") -> str:
    return f"{ctx.seed_name}_{ctx.team}_{ctx.slot}"


def load_received_index(ctx: "BizHawkClientContext") -> int:
    try:
        with open(Utils.user_path("data", RECEIVED_FILE), "r", encoding="utf-8") as file:
            return int(json.load(file).get(received_key(ctx), 0))
    except (OSError, ValueError, AttributeError):
        return 0


def save_received_index(ctx: "BizHawkClientContext", index: int) -> None:
    path = Utils.user_path("data", RECEIVED_FILE)
    try:
        with open(path, "r", encoding="utf-8") as file:
            data = json.load(file)
        if not isinstance(data, dict):
            data = {}
    except (OSError, ValueError):
        data = {}

    data[received_key(ctx)] = index
    try:
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding="utf-8") as file:
            json.dump(data, file)
    except OSError as error:
        logger.warning(f"DEBUG: Couldn't save received-item progress ({error}); items may be given again next connect")


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
        # How many entries of ctx.items_received have already been given to the player.
        # None until loaded from disk after connecting.
        self.received_index: int | None = None

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
        self.received_index = None

        return True

    async def game_watcher(self, ctx: "BizHawkClientContext") -> None:
        if ctx.server is None or ctx.server.socket.closed or ctx.slot_data is None:
            return

        # Block flags, counters and the ready flag go in ONE read so they're a snapshot of the same frame.
        counter_ids = list(COUNTERS)
        requests = (
            [(address, 1, DOMAIN) for address in BLOCK_FLAG_ADDRESSES]
            + [(address, size, DOMAIN) for address, size in COUNTERS.values()]
            + [(MOVE_FLAGS_ADDRESS, 1, DOMAIN)]
        )
        if READY_FLAG is not None:
            requests.append((READY_FLAG[0], 1, DOMAIN))

        try:
            reads = await bizhawk.read(ctx.bizhawk_ctx, requests)
        except bizhawk.RequestFailedError:
            return

        flag_end = len(BLOCK_FLAG_ADDRESSES)
        counter_end = flag_end + len(counter_ids)
        move_flags = reads[counter_end][0]

        # bizhawk.read returns bytes objects; the 3DS is little-endian.
        flags = {address: raw[0] for address, raw in zip(BLOCK_FLAG_ADDRESSES, reads[:flag_end])}
        counts = {item_id: int.from_bytes(raw, "little") for item_id, raw in zip(counter_ids, reads[flag_end:counter_end])}
        ready = True if READY_FLAG is None else bool(reads[counter_end + 1][0] & READY_FLAG[1])

        for name in await self.check_blocks(ctx, flags):
            self.queue_removal(name)

        await self.process_removals(ctx, counts)

        if ready:
            await self.receive_items(ctx, counts, move_flags)

        # Next tick compares against this one. process_removals and receive_items edit
        # `counts` to match what they wrote, so our own writes never look like the
        # player gaining items (or a block reward).
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
        logger.info(f"DEBUG: Block hit: {name} (vanilla contents: {block.quantity}x {item_name})")

        if block.item_id not in COUNTERS:
            logger.warning(
                f"DEBUG: Can't take back {block.quantity}x {item_name} from {name}: "
                f"DEBUG: no counter address for item ID {block.item_id}"
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
                logger.warning(f"DEBUG: Never saw {item_name} go up; giving up on taking back {pending.amount}")
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

            logger.info(f"DEBUG: Took back {remove}x {item_name} ({current} -> {new_value})")
            counts[item_id] = new_value
            pending.amount -= remove
            if pending.amount <= 0:
                del self.pending[item_id]

    async def receive_items(
        self, ctx: "BizHawkClientContext", counts: dict[int, int], move_flags: int
    ) -> None:
        """Adds received items to the inventory and unlocks moves. Edits `counts` in place."""
        if self.received_index is None:
            # Never ahead of what the server has sent, in case the room was reset.
            self.received_index = min(load_received_index(ctx), len(ctx.items_received))

        start = self.received_index
        new_items = ctx.items_received[start:]
        if not new_items:
            return
        end = start + len(new_items)

        # Add up everything received since last time, per counter.
        totals: dict[int, int] = {}
        move_mask = 0
        hammer_count = sum(
            network_item.item == PROGRESSIVE_HAMMERS_ITEM_ID
            for network_item in ctx.items_received[:start]
        )
        for network_item in new_items:
            move = MOVE_ITEM_FLAGS.get(network_item.item)
            if move is not None:
                move_mask |= move[0]
                continue
            if network_item.item == PROGRESSIVE_HAMMERS_ITEM_ID:
                hammer_count += 1
                if hammer_count <= len(PROGRESSIVE_HAMMER_FLAGS):
                    move_mask |= PROGRESSIVE_HAMMER_FLAGS[hammer_count - 1][0]
                continue

            grant = GRANTS.get(network_item.item)
            if grant is None or grant[0] not in COUNTERS:
                name = ITEM_NAME_BY_ID.get(network_item.item, f"item ID {network_item.item}")
                logger.info(f"DEBUG: Received {name}: nothing to add to the inventory")
                continue
            counter_id, amount = grant
            totals[counter_id] = totals.get(counter_id, 0) + amount

        # One atomic write for everything: either all of it lands or none of it does.
        writes: list[tuple[int, bytes, str]] = []
        guards: list[tuple[int, bytes, str]] = []
        results: dict[int, tuple[int, int]] = {}  # counter ID -> (old value, new value)
        for counter_id, amount in totals.items():
            name = ITEM_NAME_BY_ID.get(counter_id, f"Unknown item {counter_id}")
            address, size = COUNTERS[counter_id]
            current = counts[counter_id]
            cap = COUNTER_CAPS[counter_id]
            new_value = min(current + amount, cap)

            if new_value < current + amount:
                logger.warning(f"DEBUG:{name} would pass the cap of {cap}; dropping {current + amount - new_value}")
            if new_value == current:
                continue

            writes.append((address, new_value.to_bytes(size, "little"), DOMAIN))
            guards.append((address, current.to_bytes(size, "little"), DOMAIN))
            results[counter_id] = (current, new_value)

        new_move_flags = move_flags | move_mask
        unlocked_moves = [
            name
            for bit, name in (*MOVE_ITEM_FLAGS.values(), *PROGRESSIVE_HAMMER_FLAGS)
            if (new_move_flags & bit) and not (move_flags & bit)
        ]
        if new_move_flags != move_flags:
            writes.append((MOVE_FLAGS_ADDRESS, bytes([new_move_flags]), DOMAIN))
            guards.append((MOVE_FLAGS_ADDRESS, bytes([move_flags]), DOMAIN))

        if writes and not await bizhawk.guarded_write(ctx.bizhawk_ctx, writes, guards):
            return  # memory changed under us; the index isn't advanced, so we retry next tick

        for counter_id, (current, new_value) in results.items():
            name = ITEM_NAME_BY_ID.get(counter_id, f"Unknown item {counter_id}")
            logger.info(f"DEBUG: Received {new_value - current}x {name} ({current} -> {new_value})")
            counts[counter_id] = new_value

        for name in unlocked_moves:
            logger.info(f"DEBUG: Unlocked move: {name}")

        self.received_index = end
        save_received_index(ctx, end)
