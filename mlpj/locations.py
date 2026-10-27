from __future__ import annotations
from typing import TYPE_CHECKING

from BaseClasses import ItemClassification, Location

from . import items

if TYPE_CHECKING:
    from .world import PJWorld

BLOCK_LOCATION_ID = {
    #PC (Peach's Castle) 1-9
    "PC Throne Room Left Block": 1,
    "PC Throne Room Right Block": 2,

    "PC Main Hall Block": 3,

    "PC Left Room Upper Block": 4,
    "PC Left Room Lower Block": 5,

    "PC Shop Room Left Block": 6,
    "PC Shop Room Right Block": 7,

    "PC Outside Upper Block": 8,
    "PC Outside Lower Block": 9,
}

def get_block_ids(location_names: list[str]) -> dict[str, int | None]:
    return {location_name: BLOCK_LOCATION_ID[location_name] for location_name in location_names}


#Location Name: (Address, Bitmask)
BLOCK_DATA = {
    #PC (Peach's Castle)
    "PC Throne Room Left Block": (0x007BB429, 0x01),
    "PC Throne Room Right Block": (0x007BB428, 0x80),

    "PC Main Hall Block": (0x007BB429, 0x02),

    "PC Left Room Upper Block": (0x007BB47C, 0x04),
    "PC Left Room Lower Block": (0x007BB47C, 0x08),

    "PC Shop Room Left Block": (0x007BB47C, 0x20),
    "PC Shop Room Right Block": (0x007BB47C, 0x10),

    "PC Outside Upper Block": (0x007BB47C, 0x40),
    "PC Outside Lower Block": (0x007BB47C, 0x80),
}

class PJLocation(Location):
    game: str = "Mario & Luigi: Paper Jam"
    block_location_table: dict[str, int] = BLOCK_LOCATION_ID
    block_data_table: dict[str, tuple[int, int]] = BLOCK_DATA

def create_all_locations(world: PJWorld) -> None:
    create_blocks(world)

def create_blocks(world: PJWorld) -> None:
    peachcastle = world.get_region("Peach's Castle")

    peachcastle_locations = get_block_ids(
        [
         "PC Throne Room Left Block",
         "PC Throne Room Right Block",
         "PC Main Hall Block",
         "PC Left Room Upper Block",
         "PC Left Room Lower Block",
         "PC Shop Room Left Block",
         "PC Shop Room Right Block",
         "PC Outside Upper Block",
         "PC Outside Lower Block"
         ]
    )
    peachcastle.add_locations(peachcastle_locations, PJLocation)