# Coin: ID
COINS = {
    "Coin": 1,
    "5 Coin": 2,
    "10 Coin": 3,
    "50 Coin": 4,
    "100 Coin": 5,
}

# Item(ItemID, Address)
ITEMS = {
    #Inventory Items
    "Mushroom": (10, 0x007BB1CC),
    "Super Mushroom": (11, 0x007BB1CD),
    "Ultra Mushroom": (12, 0x007BB1CE),
    "Max Mushroom": (13, 0x007BB1CF),

    "Nut": (14, 0x007BB1D0),
    "Super Nut": (15, 0x007BB1D1),
    "Ultra Nut": (16, 0x007BB1D2),
    "Max Nut": (17, 0x007BB1D3),

    "Syrup Jar": (18, 0x007BB1D4),
    "Supersyrup Jar": (19, 0x007BB1D5),
    "Ultrasyrup Jar": (20, 0x007BB1D6),
    "Max Syrup Jar": (21, 0x007BB1D7),

    "Candy": (22, 0x007BB1D8),
    "Super Candy": (23, 0x007BB1D9),
    "Ultra Candy": (24, 0x007BB1DA),
    "Max Candy": (25, 0x007BB1DB),

    "1-Up Mushroom": (26, 0x007BB1DC),
    "1-Up DX": (27, 0x007BB1DD),
    "Double 1-Up Mushroom": (28, 0x007BB1DE),

    "Refreshing Herb": (29, 0x007BB1DF),
    "Boo Biscuit": (30, 0x007BB1E6),

    "Heart Bean": (31, 0x007BB1E0),
    "Bros. Bean": (32, 0x007BB1E1),
    "Power Bean": (33, 0x007BB1E2),
    "Defense Bean": (34, 0x007BB1E3),
    "Speed Bean": (35, 0x007BB1E4),
    "Stache Bean": (36, 0x007BB1E5),

    "Heart Bean DX": (37, 0x007BB1E7),
    "Bros. Bean DX": (38, 0x007BB1E8),
    "Power Bean DX": (39, 0x007BB1E9),
    "Defense Bean DX": (40, 0x007BB1EA),
    "Speed Bean DX": (41, 0x007BB1EB),
    "Stache Bean DX": (42, 0x007BB1EC),
}

ITEM_NAME_BY_ID = {
    **{item_id: name for name, item_id in COINS.items()},
    **{item_id: name for name, (item_id, _address) in ITEMS.items()},
}

# FILL IN: (address, byte width) of the coin counter, e.g. (0x007BB1xx, 4).
# While this is None, blocks that give coins are skipped (with a warning) instead of crashing.
COIN_COUNTER: tuple[int, int] | None = (0x007BB1C4, 4)
 
# Everything the client can read and take back from, by item ID: item ID -> (address, byte width).
# Inventory items are 1 byte each. Values are read as little-endian.
COUNTERS: dict[int, tuple[int, int]] = {
    item_id: (address, 1) for item_id, address in ITEMS.values()
}
if COIN_COUNTER is not None:
    COUNTERS[COINS["Coin"]] = COIN_COUNTER

# ---- Receiving items from Archipelago ----

# Coins an AP coin item is worth. They go into the coin counter (item ID 1 in COUNTERS).
COIN_AMOUNTS = {
    "Coin": 1,
    "5 Coin": 5,
    "10 Coin": 10,
    "50 Coin": 50,
    "100 Coin": 100,
}

# What each received AP item does: AP item ID -> (counter item ID, amount to add).
# Inventory items add 1 of themselves; coin items add coins to the coin counter.
# Items not in here (e.g. "Test Progression") are received but don't touch the inventory.
GRANTS: dict[int, tuple[int, int]] = {
    **{item_id: (item_id, 1) for item_id, _address in ITEMS.values()},
    **{COINS[name]: (COINS["Coin"], amount) for name, amount in COIN_AMOUNTS.items()},
}

# Highest value a counter may reach when the client gives you something.
# ASSUMED values, check them against the game: anything over the cap is dropped.
MAX_ITEM_COUNT = 99
MAX_COIN_COUNT = 9_999_999

COUNTER_CAPS: dict[int, int] = {item_id: MAX_ITEM_COUNT for item_id in COUNTERS}
if COIN_COUNTER is not None:
    COUNTER_CAPS[COINS["Coin"]] = MAX_COIN_COUNT
