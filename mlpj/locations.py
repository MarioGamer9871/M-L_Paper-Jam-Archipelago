from __future__ import annotations
from typing import TYPE_CHECKING, NamedTuple

from BaseClasses import Location

from . import items

if TYPE_CHECKING:
    from .world import PJWorld

class BlockData(NamedTuple):
    address: int      # RAM address of the byte holding this block's "hit" flag
    bitmask: int      # the bit in that byte that gets set once the block is hit
    location_id: int  # Archipelago location ID (unique; never renumber existing ones)
    item_id: int      # vanilla contents: an ID from itemdata.COINS / itemdata.ITEMS
    quantity: int     # vanilla amount
    region: str       # region this location gets created in
 
#Region Names
PC ="Peach's Castle"
SP ="Sunbeam Plains"

#Location Name: (Address, Bitmask, LocationID, ItemInside, Quantity, Region)
LOCATION_DATA: dict[str, BlockData] = {
    #PC (Peach's Castle) 1-9
    "PC Throne Room Left Block": BlockData(0x007BB429, 0x01, 1, 1, 50, PC), #50 Coin
    "PC Throne Room Right Block": BlockData(0x007BB428, 0x80, 2, 1, 10, PC), #10 Coin
 
    "PC Main Hall Block": BlockData(0x007BB429, 0x02, 3, 1, 10, PC), #10 Coin
 
    "PC Left Room Upper Block": BlockData(0x007BB47C, 0x04, 4, 1, 5, PC), #5 Coin
    "PC Left Room Lower Block": BlockData(0x007BB47C, 0x08, 5, 1, 10, PC), #10 Coin
 
    "PC Shop Room Left Block": BlockData(0x007BB47C, 0x20, 6, 1, 10, PC), #10 Coin
    "PC Shop Room Right Block": BlockData(0x007BB47C, 0x10, 7, 1, 5, PC), #5 Coin
 
    "PC Outside Upper Block": BlockData(0x007BB47C, 0x40, 8, 1, 50, PC), #50 Coin
    "PC Outside Lower Block": BlockData(0x007BB47C, 0x80, 9, 12, 2, PC), #Ultra Mushroom x2

    #SP (Sunbeam Plains) 10-
    #SP Blocks (Sunbeam Plains) 10-69
    "SP First Room Island Block": BlockData(0x007BB405, 0x04, 10, None, 1, SP), #Cozy Wear (Gear) - Needs: Dash Socks (Logic)

    "SP Second Room Top Left Left Block": BlockData(0x007BB401, 0x04, 11, 1, 5, SP), #5 Coin
    "SP Second Room Top Left Right Block": BlockData(0x007BB401, 0x10, 12, 10, 2, SP), #Mushroom x2
    "SP Second Room Top Right Block": BlockData(0x007BB401, 0x08, 13, None, 1, SP), #Bare Boots DX (Gear) - Needs: Trio Plane (Logic)
    "SP Second Room Right Island Block": BlockData(0x007BB404, 0x02, 14, 1, 50, SP), #50 Coin - Needs: Trio Grab (Logic)

    "SP Top Left Room Right Upper Block": BlockData(0x007BB401, 0x40, 15, 1, 1, SP), #Coin
    "SP Top Left Room Right Lower Block": BlockData(0x007BB402, 0x02, 16, 1, 5, SP), #5 Coin
    "SP Top Left Room Left Block": BlockData(0x007BB401, 0x20, 17, 1, 5, SP), #5 Coin
    "SP Top Left Room Island Block": BlockData(0x007BB402, 0x08, 18, None, 1, SP), #Fighter Wear (Gear) - Needs: Trio Grab (Logic)
    "SP Top Left Room Upper Left Block": BlockData(0x007BB401, 0x80, 19, 18, 2, SP), #Syrup Jar x2 - Needs: Trio Grab, Trio Plane (Logic)
    "SP Top Left Room Upper Right Block": BlockData(0x007BB402, 0x10, 20, 1, 5, SP), #5 Coin - Needs: Trio Grab, Trio Plane (Logic)
    "SP Top Left Room M Block": BlockData(0x007BB402, 0x01, 21, 14, 1, SP), #Nut - Needs: Trio Grab, Trio Plane (Logic)
    "SP Top Left Room L Block": BlockData(0x007BB402, 0x04, 22, 1, 1, SP), #Coin - Needs: Trio Grab, Trio Plane (Logic)
    #SP Top Left Room leads to Deep Gloomy Woods so Logic for "Sunbeam Plains to Deep Gloomy Woods" Needs: Trio Grab, Trio Plane (Logic) (Region Logic) (Regions: Sunbeam Plains, Deep Gloomy Woods)

    "SP Paper Petey Room Behind Crack Left Block": BlockData(0x007BB402, 0x20, 23, 10, 1, SP), #Mushroom - Needs: Trio Grab (Logic)
    "SP Paper Petey Room Behind Crack Right Block": BlockData(0x007BB414, 0x01, 24, 1, 1, SP), #Coin - Needs: Trio Grab (Logic)
    "SP Paper Petey Room Lower Left Block": BlockData(0x007BB414, 0x02, 25, 1, 5, SP), #5 Coin - Needs: Trio Grab (Logic)
    "SP Paper Petey Room Lower Middle Block": BlockData(0x007BB424, 0x80, 26, 1, 1, SP), #Coin - Needs: Trio Grab (Logic)
    "SP Paper Petey Room Lower Right Block": BlockData(0x007BB441, 0x04, 27, 1, 5, SP), #5 Coin - Needs: Trio Grab (Logic)
    "SP Paper Petey Room Near Gloomy Woods Block": BlockData(0x007BB432, 0x40, 28, 1, 5, SP), #5 Coin - Needs: Trio Grab (Logic)
    #SP Paper Petey Room leads to Gloomy Woods so Logic for "Sunbeam Plains to Gloomy Woods" Needs: Trio Grab (Logic) (Region Logic) (Regions: Sunbeam Plains, Gloomy Woods)

    "SP Paper Mario Room Behind Crack Left Block": BlockData(0x007BB403, 0x20, 29, None, 1, SP), #So-So Boots (Gear) - Needs: Trio Grab, Trio Drill (Logic)
    "SP Paper Mario Room Behind Crack Right Block": BlockData(0x007BB403, 0x40, 30, 22, 1, SP), #Candy - Needs: Trio Grab, Trio Drill (Logic)
    "SP Paper Mario Room P Block": BlockData(0x007BB45B, 0x08, 31, 11, 1, SP), #Super Mushroom - Needs: Trio Grab, Trio Drill (Logic)
    "SP Paper Mario Room Lower Path P Block": BlockData(0x007BB403, 0x80, 32, 23, 1, SP), #Super Candy - Needs: Trio Grab (Logic)
    "SP Paper Mario Room Lower Path M Block": BlockData(0x007BB404, 0x01, 33, 1, 10, SP), #10 Coin - Needs: Trio Grab (Logic)

    "SP Lakitu Center Room Upper Area Left Block": BlockData(0x007BB403, 0x04, 34, 26, 1, SP), #1-Up Mushroom - Needs: Trio Grab, Trio Drill (Logic)
    "SP Lakitu Center Room Upper Area Middle Block": BlockData(0x007BB403, 0x08, 35, 1, 1, SP), #Coin - Needs: Trio Grab, Trio Drill (Logic)
    "SP Lakitu Center Room Upper Area Right Block": BlockData(0x007BB403, 0x10, 36, 29, 1, SP), #Refreshing Herb - Needs: Trio Grab, Trio Drill (Logic)
    "SP Lakitu Center Room Lower Path Left Block": BlockData(0x007BB403, 0x02, 37, None, 1, SP), #Filler Brooch (Gear) - Needs: Trio Grab (Logic) 
    "SP Lakitu Center Room Lower Path Right Block": BlockData(0x007BB415, 0x02, 38, 1, 50, SP), #50 Coin - Needs: Trio Grab (Logic) 

    "SP Bowser Board Room Upper Path P Block": BlockData(0x007BB42F, 0x40, 39, 1, 10, SP), #10 Coin - Needs: Dash Socks, Trio Grab, Trio Drill (Logic)
    "SP Bowser Board Room Lower Path Left Block": BlockData(0x007BB443, 0x04, 40, 1, 5, SP), #5 Coin - Needs: Trio Grab (Logic)
    "SP Bowser Board Room Lower Path Right Block": BlockData(0x007BB430, 0x01, 41, None, 1, SP), #Knockout Boots (Gear) - Needs: Trio Grab (Logic)

    "SP Petey Room Right Area Upper Block": BlockData(0x007BB45B, 0x10, 42, 1, 5, SP), #5 Coin - Needs: Trio Grab, Trio Drill (Logic)
    "SP Petey Room Right Area Middle Block": BlockData(0x007BB404, 0x20, 43, 1, 1, SP), #Coin - Needs: Trio Grab, Trio Drill (Logic)
    "SP Petey Room Right Area Lower Block": BlockData(0x007BB404, 0x10, 44, 1, 10, SP), #10 Coin - Needs: Trio Grab, Trio Drill (Logic)
    "SP Petey Room Lower Left Area Right Block": BlockData(0x007BB418, 0x01, 45, 28, 1, SP), #Double 1-Up Mushroom - Needs: Trio Grab, Trio Drill (Logic)
    "SP Petey Room Lower Left Area Left Block": BlockData(0x007BB468, 0x20, 46, 1, 50, SP), #50 Coin - Needs: Trio Grab (Logic)

    "SP Papercraft Room Upper Left Block": BlockData(0x007BB404, 0x40, 47, 1, 5, SP), #5 Coin - Needs: Trio Grab, Trio Drill (Logic)
    "SP Papercraft Room Upper Middle Block": BlockData(0x007BB405, 0x01, 48, 18, 2, SP), #Syrup Jar x2 - Needs: Trio Grab, Trio Drill (Logic)
    "SP Papercraft Room Upper Right Block": BlockData(0x007BB405, 0x02, 49, 1, 1, SP), #Coin - Needs: Trio Grab, Trio Drill (Logic)
    "SP Papercraft Room Lower Block": BlockData(0x007BB404, 0x80, 50, 26, 1, SP), #1-Up Mushroom - Needs: Trio Grab, Trio Drill (Logic)
    #SP Papercraft Room leads to Doop Doop Dunes so Logic for "Sunbeam Plains to Doop Doop Dunes" Needs: Trio Grab, Trio Drill

    "SP Toad Town Block": BlockData(0x007BB458, 0x10, 51, 1, 10, SP), #10 Coin - Needs: Trio Grab, Trio Drill (Logic)
    "SP Toad Town Behind Crack Left Block": BlockData(0x007BB422, 0x40, 52, 14, 1, SP), #Nut - Needs: Trio Grab, Trio Drill (Logic)
    "SP Toad Town Behind Crack Right Block": BlockData(0x007BB47B, 0x40, 53, 1, 10, SP), #10 Coin - Needs: Trio Grab, Trio Drill (Logic)

    "SP Right Cloud Room Lower Right Block": BlockData(0x007BB42B, 0x01, 54, 1, 10, SP), #10 Coin - Needs: Trio Grab, Trio Plane (Logic)
    "SP Right Cloud Room Lower Left Block": BlockData(0x007BB42A, 0x20, 55, 1, 50, SP), #50 Coin - Needs: Trio Grab, Trio Plane (Logic)
    "SP Right Cloud Room Lower Middle Right Block": BlockData(0x007BB42A, 0x80, 56, 12, 2, SP), #Ultra Mushroom x2 - Needs: Trio Grab, Trio Plane (Logic)
    "SP Right Cloud Room Lower Middle Left Block": BlockData(0x007BB42A, 0x40, 57, 1, 50, SP), #50 Coin - Needs: Trio Grab, Trio Plane (Logic)
    "SP Right Cloud Room Upper Right M Block": BlockData(0x007BB42A, 0x10, 58, 1, 10, SP), #10 Coin - Needs: Trio Grab, Trio Plane (Logic)
    "SP Right Cloud Room Upper Right L Block": BlockData(0x007BB42A, 0x08, 59, 1, 50, SP), #50 Coin - Needs: Trio Grab, Trio Plane (Logic)
    "SP Right Cloud Room Upper Left Block": BlockData(0x007BB47D, 0x01, 60, 27, 1, SP), #1-Up DX - Needs: Trio Grab, Trio Plane (Logic)
    
    "SP Left Cloud Room Upper Left Block": BlockData(0x007BB42D, 0x04, 61, None, 1, SP), #Flashy Wear (Gear) - Needs: Trio Grab, Trio Plane (Logic)
    "SP Left Cloud Room Upper Right Block": BlockData(0x007BB42D, 0x02, 62, 1, 50, SP), #50 Coin - Needs: Trio Grab, Trio Plane (Logic)
    "SP Left Cloud Room Lower Right Block": BlockData(0x007BB42D, 0x20, 63, 1, 10, SP), #10 Coin - Needs: Trio Grab, Trio Plane (Logic)
    "SP Left Cloud Room Lower Middle Block": BlockData(0x007BB42D, 0x08, 64, 24, 1, SP), #Ultra Candy - Needs: Trio Grab, Trio Plane (Logic)
    "SP Left Cloud Room Lower Left Block": BlockData(0x007BB42D, 0x10, 65, 1, 50, SP), #50 Coin - Needs: Trio Grab, Trio Plane (Logic)
}
 
 
def _validate_block_data() -> None:
    """Catch copy/paste mistakes when adding blocks, at import time."""
    location_ids = [block.location_id for block in LOCATION_DATA.values()]
    if len(location_ids) != len(set(location_ids)):
        raise ValueError("LOCATION_DATA has a duplicate location ID")
 
    flags = [(block.address, block.bitmask) for block in LOCATION_DATA.values()]
    if len(flags) != len(set(flags)):
        raise ValueError("LOCATION_DATA has two blocks using the same address + bitmask")
 
 
_validate_block_data()
 
# Name -> ID table for the world's location_name_to_id, derived from LOCATION_DATA.
BLOCK_LOCATION_ID: dict[str, int] = {name: block.location_id for name, block in LOCATION_DATA.items()}
 
class PJLocation(Location):
    game: str = "Mario & Luigi: Paper Jam"
    block_location_table: dict[str, int] = BLOCK_LOCATION_ID
    block_data_table: dict[str, BlockData] = LOCATION_DATA
 
def create_all_locations(world: PJWorld) -> None:
    create_blocks(world)
 
def create_blocks(world: PJWorld) -> None:
    # Group blocks by region, then add each group to its region.
    locations_by_region: dict[str, dict[str, int]] = {}
    for name, block in LOCATION_DATA.items():
        locations_by_region.setdefault(block.region, {})[name] = block.location_id
 
    for region_name, region_locations in locations_by_region.items():
        world.get_region(region_name).add_locations(region_locations, PJLocation)
