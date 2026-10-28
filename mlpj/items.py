from __future__ import annotations
from typing import TYPE_CHECKING

from BaseClasses import Item, ItemClassification

if TYPE_CHECKING:
    from .world import PJWorld

ITEM_ID = {
    #Coins
    "Coin": 1,
    "5 Coin": 2,
    "10 Coin": 3,
    "50 Coin": 4,
    "100 Coin": 5,

    #Inventory Items
    "Mushroom": 10,
    "Super Mushroom": 11,
    "Ultra Mushroom": 12,
    "Max Mushroom": 13,

    "Nut": 14,
    "Super Nut": 15,
    "Ultra Nut": 16,
    "Max Nut": 17,

    "Syrup Jar": 18,
    "Supersyrup Jar": 19,
    "Ultrasyrup Jar": 20,
    "Max Syrup Jar": 21,

    "Candy": 22,
    "Super Candy": 23,
    "Ultra Candy": 24,
    "Max Candy": 25,

    "1-Up Mushroom": 26,
    "1-Up DX": 27,
    "Double 1-Up Mushroom": 28,

    "Refreshing Herb": 29,
    "Boo Biscuit": 30,

    "Heart Bean": 31,
    "Bros. Bean": 32,
    "Power Bean": 33,
    "Defense Bean": 34,
    "Speed Bean": 35,
    "Stache Bean": 36,

    "Heart Bean DX": 37,
    "Bros. Bean DX": 38,
    "Power Bean DX": 39,
    "Defense Bean DX": 40,
    "Speed Bean DX": 41,
    "Stache Bean DX": 42,

    #Test
    "Test Progression": 100,
}

ITEM_CLASS = {
    #Coins
    "Coin": ItemClassification.filler,
    "5 Coin": ItemClassification.filler,
    "10 Coin": ItemClassification.filler,
    "50 Coin": ItemClassification.filler,
    "100 Coin": ItemClassification.filler,

    #Inventory Items
    "Mushroom": ItemClassification.filler,
    "Super Mushroom": ItemClassification.filler,
    "Ultra Mushroom": ItemClassification.filler,
    "Max Mushroom": ItemClassification.filler,

    "Nut": ItemClassification.filler,
    "Super Nut": ItemClassification.filler,
    "Ultra Nut": ItemClassification.filler,
    "Max Nut": ItemClassification.filler,

    "Syrup Jar": ItemClassification.filler,
    "Supersyrup Jar": ItemClassification.filler,
    "Ultrasyrup Jar": ItemClassification.filler,
    "Max Syrup Jar": ItemClassification.filler,

    "Candy": ItemClassification.filler,
    "Super Candy": ItemClassification.filler,
    "Ultra Candy": ItemClassification.filler,
    "Max Candy": ItemClassification.filler,

    "1-Up Mushroom": ItemClassification.filler,
    "1-Up DX": ItemClassification.filler,
    "Double 1-Up Mushroom": ItemClassification.filler,

    "Refreshing Herb": ItemClassification.filler,
    "Boo Biscuit": ItemClassification.filler,

    "Heart Bean": ItemClassification.filler,
    "Bros. Bean": ItemClassification.filler,
    "Power Bean": ItemClassification.filler,
    "Defense Bean": ItemClassification.filler,
    "Speed Bean": ItemClassification.filler,
    "Stache Bean": ItemClassification.filler,

    "Heart Bean DX": ItemClassification.filler,
    "Bros. Bean DX": ItemClassification.filler,
    "Power Bean DX": ItemClassification.filler,
    "Defense Bean DX": ItemClassification.filler,
    "Speed Bean DX": ItemClassification.filler,
    "Stache Bean DX": ItemClassification.filler,

    #Test
    "Test Progression": ItemClassification.progression,
}

class PJItem (Item):
    game = "Mario & Luigi: Paper Jam"

def get_random_filler_item_name(world: PJWorld):
    return world.random.choice([name for name, classification in ITEM_CLASS.items() if classification == ItemClassification.filler])

def create_item_with_correct_classification(world, name: str) -> PJItem:
    classification = ITEM_CLASS[name]

    return PJItem(
        name,
        classification,
        ITEM_ID[name],
        world.player
    )

def create_all_items(world: PJWorld) -> None:
    itempool: list[Item] = [
        world.create_item("Test Progression"),
    ]

    number_of_items = len(itempool)
    number_of_unfilled_locations = len(world.multiworld.get_unfilled_locations(world.player))
    needed_number_of_filler_items = number_of_unfilled_locations - number_of_items

    itempool += [world.create_filler() for _ in range(needed_number_of_filler_items)]

    world.multiworld.itempool += itempool