from collections.abc import Mapping
from typing import Any

from worlds.AutoWorld import World

from . import items, locations, regions

class PJWorld(World):
    """
    Mario & Luigi: Paper Jam is a turn-based RPG on the Nintendo 3DS
    """

    game = "Mario & Luigi: Paper Jam"

    location_name_to_id = locations.BLOCK_LOCATION_ID
    item_name_to_id = items.ITEM_ID

    origin_region_name = "Peach's Castle"

    def create_regions(self) -> None:
        regions.create_and_connect_regions(self)
        locations.create_all_locations(self)

    def create_items(self) -> None:
        items.create_all_items(self)

    def create_item(self, name: str) -> items.PJItem:
        return items.create_item_with_correct_classification(self, name)

    def get_filler_item_name(self) -> str:
        return items.get_random_filler_item_name(self)
    