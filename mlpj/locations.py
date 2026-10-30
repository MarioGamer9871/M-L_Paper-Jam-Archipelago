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
DDD = "Doop Doop Dunes"
TT = "Twinsy Tropics"
GW = "Gloomy Woods"
MB = "Mount Brrr"
NBC = "Neo Bowser's Castle"

#Location Name: (Address, Bitmask, LocationID, ItemInside, Quantity, Region)
LOCATION_DATA: dict[str, BlockData] = {
    #PC (Peach's Castle Destroyed) 1-9
    "PC Throne Room Left Block": BlockData(0x007BB429, 0x01, 1, 1, 50, PC), #50 Coin
    "PC Throne Room Right Block": BlockData(0x007BB428, 0x80, 2, 1, 10, PC), #10 Coin
 
    "PC Main Hall Block": BlockData(0x007BB429, 0x02, 3, 1, 10, PC), #10 Coin
 
    "PC Left Room Upper Block": BlockData(0x007BB47C, 0x04, 4, 1, 5, PC), #5 Coin
    "PC Left Room Lower Block": BlockData(0x007BB47C, 0x08, 5, 1, 10, PC), #10 Coin
 
    "PC Shop Room Left Block": BlockData(0x007BB47C, 0x20, 6, 1, 10, PC), #10 Coin
    "PC Shop Room Right Block": BlockData(0x007BB47C, 0x10, 7, 1, 5, PC), #5 Coin
 
    "PC Outside Upper Block": BlockData(0x007BB47C, 0x40, 8, 1, 50, PC), #50 Coin
    "PC Outside Lower Block": BlockData(0x007BB47C, 0x80, 9, 12, 2, PC), #Ultra Mushroom x2

    #SP (Sunbeam Plains) 10-109
    #SP Blocks 10-69
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

    #SP Beanspots 70-109
    "SP Second Room Upper Beanspot": BlockData(0x007BB419, 0x02, 70, 1, 50, SP), #50 Coin - Needs: Trio Drill (Logic)
    "SP Second Room Middle Beanspot": BlockData(0x007BB405, 0x10, 71, 32, 1, SP), #Bros. Bean - Needs: Trio Drill (Logic)
    "SP Second Room Lower Beanspot": BlockData(0x007BB405, 0x08, 72, 1, 50, SP), #50 Coin - Needs: Trio Drill (Logic)

    "SP Top Left Room Far Left Beanspot": BlockData(0x007BB404, 0x04, 73, 1, 50, SP), #50 Coin - Needs: Trio Grab, Trio Drill, Trio Plane (Logic)
    "SP Top Left Room Middle Left Beanspot": BlockData(0x007BB404, 0x08, 74, 1, 50, SP), #50 Coin - Needs: Trio Grab, Trio Drill, Trio Plane (Logic)
    "SP Top Left Room Middle Right Beanspot": BlockData(0x007BB418, 0x02, 75, 35, 1, SP), #Speed Bean - Needs: Trio Grab, Trio Drill, Trio Plane (Logic)
    "SP Top Left Room Far Right Beanspot": BlockData(0x007BB418, 0x04, 76, 36, 1, SP), #Stache Bean - Needs: Trio Grab, Trio Drill, Trio Plane (Logic)

    "SP Paper Petey Room Top Left Left Beanspot": BlockData(0x007BB427, 0x04, 77, 1, 50, SP), #50 Coin - Needs: Trio Grab, Trio Drill (Logic)
    "SP Paper Petey Room Top Left Middle Beanspot": BlockData(0x007BB427, 0x08, 78, 34, 1, SP), #Defense Bean - Needs: Trio Grab, Trio Drill (Logic)
    "SP Paper Petey Room Top Left Right Beanspot": BlockData(0x007BB432, 0x20, 79, 1, 50, SP), #50 Coin - Needs: Trio Grab, Trio Drill (Logic)
    "SP Paper Petey Room Top Right Left Beanspot": BlockData(0x007BB416, 0x10, 80, 1, 50, SP), #50 Coin - Needs: Trio Grab, Trio Drill (Logic)
    "SP Paper Petey Room Top Right Right Beanspot": BlockData(0x007BB416, 0x08, 81, 31, 1, SP), #Heart Bean - Needs: Trio Grab, Trio Drill (Logic)

    "SP Paper Mario Room Upper Path Beanspot": BlockData(0x007BB447, 0x01, 82, 34, 1, SP), #Defense Bean - Needs: Trio Grab, Trio Drill (Logic)
    "SP Paper Mario Room Lower Path Far Left Beanspot": BlockData(0x007BB42A, 0x04, 83, 1, 50, SP), #50 Coin - Needs: Trio Grab, Trio Drill (Logic)
    "SP Paper Mario Room Lower Path Middle Left Beanspot": BlockData(0x007BB45F, 0x08, 84, 36, 1, SP), #Stache Bean - Needs: Trio Grab, Trio Drill (Logic)
    "SP Paper Mario Room Lower Path Middle Right Beanspot": BlockData(0x007BB461, 0x01, 85, 1, 50, SP), #50 Coin - Needs: Trio Grab, Trio Drill (Logic)
    "SP Paper Mario Room Lower Path Far Right Beanspot": BlockData(0x007BB461, 0x02, 86, 32, 1, SP), #Bros. Bean - Needs: Trio Grab, Trio Drill (Logic)
    
    "SP Lakitu Center Room Upper Beanspot": BlockData(0x007BB425, 0x10, 87, 1, 50, SP), #50 Coin - Needs: Trio Grab, Trio Drill (Logic)
    "SP Lakitu Center Room Middle Beanspot": BlockData(0x007BB42F, 0x02, 88, 1, 50, SP), #50 Coin - Needs: Trio Grab, Trio Drill (Logic)
    "SP Lakitu Center Room Upper Beanspot": BlockData(0x007BB414, 0x40, 89, 31, 1, SP), #Heart Bean - Needs: Trio Grab, Trio Drill (Logic)

    "SP Petey Room Top Right Left Beanspot": BlockData(0x007BB416, 0x02, 90, 36, 1, SP), #Stache Bean - Needs: Trio Grab, Trio Drill (Logic)
    "SP Petey Room Top Right Right Beanspot": BlockData(0x007BB416, 0x04, 91, 31, 1, SP), #Heart Bean - Needs: Trio Grab, Trio Drill (Logic)
    "SP Petey Room Bottom Right Upper Beanspot": BlockData(0x007BB425, 0x04, 92, 35, 1, SP), #Speed Bean - Needs: Trio Grab, Trio Drill (Logic)
    "SP Petey Room Bottom Right Lower Beanspot": BlockData(0x007BB425, 0x08, 93, 1, 50, SP), #50 Coin - Needs: Trio Grab, Trio Drill (Logic)
    "SP Petey Room Bottom Left Left Beanspot": BlockData(0x007BB462, 0x02, 94, 1, 50, SP), #50 Coin - Needs: Trio Grab, Trio Drill (Logic)
    "SP Petey Room Bottom Left Middle Beanspot": BlockData(0x007BB468, 0x08, 95, 1, 50, SP), #50 Coin - Needs: Trio Grab, Trio Drill (Logic)
    "SP Petey Room Bottom Left Right Beanspot": BlockData(0x007BB468, 0x10, 96, 1, 50, SP), #50 Coin - Needs: Trio Grab, Trio Drill (Logic)

    "SP Papercraft Room Far Left Beanspot": BlockData(0x007BB425, 0x80, 97, 1, 50, SP), #50 Coin - Needs: Trio Grab, Trio Drill (Logic)
    "SP Papercraft Room Middle Left Beanspot": BlockData(0x007BB425, 0x40, 98, 34, 1, SP), #Defense Bean - Needs: Trio Grab, Trio Drill (Logic)
    "SP Papercraft Room Middle Right Beanspot": BlockData(0x007BB415, 0x01, 99, 1, 50, SP), #50 Coin - Needs: Trio Grab, Trio Drill (Logic)
    "SP Papercraft Room Far Right Beanspot": BlockData(0x007BB414, 0x80, 100, 32, 1, SP), #Bros. Bean - Needs: Trio Grab, Trio Drill (Logic)

    "SP Toad Town Left Upper Beanspot": BlockData(0x007BB43F, 0x08, 101, 1, 50, SP), #50 Coin - Needs: Trio Grab, Trio Drill (Logic)
    "SP Toad Town Left Lower Beanspot": BlockData(0x007BB43F, 0x04, 102, 35, 1, SP), #Speed Bean - Needs: Trio Grab, Trio Drill (Logic)
    "SP Toad Town Right Upper Beanspot": BlockData(0x007BB431, 0x01, 103, 1, 50, SP), #50 Coin - Needs: Trio Grab, Trio Drill (Logic)
    "SP Toad Town Right Lower Beanspot": BlockData(0x007BB431, 0x02, 104, 33, 1, SP), #Power Bean - Needs: Trio Grab, Trio Drill (Logic)

    #DDD (Doop Doop Dunes) 110-249
    #DDD Blocks 110-179
    "DDD First Room Bottom Left L Block": BlockData(0x007BB405, 0x20, 110, 1, 5, DDD), #5 Coin - Needs: 2x Progressive Hammer (Logic)
    "DDD First Room Bottom Left M Block": BlockData(0x007BB405, 0x40, 111, None, 1, DDD), #Guard Wear (Gear) - Needs: 2x Progressive Hammer (Logic)
    "DDD First Room Top Left Upper Block": BlockData(0x007BB405, 0x80, 112, 1, 5, DDD), #5 Coin
    "DDD First Room Lower Block": BlockData(0x007BB406, 0x01, 113, 1, 5, DDD), #5 Coin
    "DDD First Room Top Right Left Block": BlockData(0x007BB406, 0x02, 114, 1, 5, DDD), #5 Coin
    "DDD First Room Top Right Right Block": BlockData(0x007BB406, 0x04, 115, 1, 1, DDD), #Coin
    "DDD First Room Far Right Block": BlockData(0x007BB406, 0x08, 116, 1, 5, DDD), #5 Coin
    "DDD First Room Top Left Lower Block": BlockData(0x007BB40A, 0x01, 117, 18, 2, DDD), #Syrup Jar x2
 
    "DDD Second Room Top Left Lower Block": BlockData(0x007BB40A, 0x02, 118, 1, 5, DDD), #5 Coin
    "DDD Second Room Top Left Upper Block": BlockData(0x007BB40A, 0x04, 119, 10, 3, DDD), #Mushroom x3
    "DDD Second Room Valley Block": BlockData(0x007BB40A, 0x08, 120, 1, 5, DDD), #5 Coin
    "DDD Second Room Top Middle Block": BlockData(0x007BB40A, 0x10, 121, 1, 1, DDD), #Coin
    "DDD Second Room Cardboard Platform Block": BlockData(0x007BB40A, 0x20, 122, 1, 5, DDD), #5 Coin
    "DDD Second Room Top Right Upper Left Block": BlockData(0x007BB40A, 0x40, 123, 29, 1, DDD), #Refreshing Herb - Needs: Progressive Hammer or Trio Drill (Logic)
    "DDD Second Room Top Right Lower Left Block": BlockData(0x007BB40A, 0x80, 124, 1, 5, DDD), #5 Coin - Needs: Progressive Hammer or Trio Drill (Logic)
    "DDD Second Room Top Right Upper Right Block": BlockData(0x007BB40B, 0x01, 125, 1, 5, DDD), #5 Coin - Needs: Progressive Hammer or Trio Drill (Logic)
    "DDD Second Room Top Right Lower Right Block": BlockData(0x007BB40B, 0x02, 126, 1, 1, DDD), #Coin - Needs: Progressive Hammer or Trio Drill (Logic)
    #DDD Second Room leads to Mount Brrr so Logic for "Doop Doop Dunes to Mount Brrr" Needs: Trio Drill (Logic) (Region Logic) (Regions: Doop Doop Dunes, Mount Brrr)
 
    "DDD Big Hill Room Far Left Block": BlockData(0x007BB40C, 0x10, 127, 26, 1, DDD), #1-Up Mushroom - Needs: 2x Progressive Hammer (Logic)
    "DDD Big Hill Room Island Right Block": BlockData(0x007BB40C, 0x20, 128, 1, 5, DDD), #5 Coin - Needs: 2x Progressive Hammer (Logic)
    "DDD Big Hill Room Island Left Block": BlockData(0x007BB40C, 0x40, 129, 1, 5, DDD), #5 Coin - Needs: 2x Progressive Hammer (Logic)
    "DDD Big Hill Room Island Middle Block": BlockData(0x007BB40C, 0x80, 130, 1, 1, DDD), #Coin - Needs: 2x Progressive Hammer (Logic)
    "DDD Big Hill Room Near Trio Hammer Tutorial Block": BlockData(0x007BB40D, 0x01, 131, 1, 5, DDD), #5 Coin - Needs: 2x Progressive Hammer (Logic)
    "DDD Big Hill Room Far Right Block": BlockData(0x007BB40D, 0x02, 132, 1, 50, DDD), #50 Coin - Needs: 2x Progressive Hammer, Springboard (Logic)
    "DDD Big Hill Room Top Left Block": BlockData(0x007BB462, 0x08, 133, 1, 1, DDD), #Coin - Needs: Progressive Hammer (Logic)
 
    "DDD Toad Town Right Block": BlockData(0x007BB424, 0x40, 134, 1, 5, DDD), #5 Coin - Needs: Progressive Hammer (Logic)
    "DDD Toad Town Middle Block": BlockData(0x007BB43C, 0x80, 135, 1, 10, DDD), #10 Coin - Needs: Progressive Hammer (Logic)
    "DDD Toad Town Left Block": BlockData(0x007BB473, 0x80, 136, 1, 10, DDD), #10 Coin - Needs: Progressive Hammer (Logic)
 
    "DDD Oasis Room Near Water Left Block": BlockData(0x007BB415, 0x04, 137, 1, 10, DDD), #10 Coin - Needs: Progressive Hammer (Logic)
    "DDD Oasis Room Near Water Right Block": BlockData(0x007BB415, 0x08, 138, 1, 10, DDD), #10 Coin - Needs: Progressive Hammer (Logic)
    "DDD Oasis Room Cliff Near Water Block": BlockData(0x007BB415, 0x10, 139, 25, 1, DDD), #Max Candy - Needs: Progressive Hammer, Trio Plane (Logic)
    "DDD Oasis Room Top Cliff Block": BlockData(0x007BB415, 0x20, 140, None, 1, DDD), #POW Mush Jams (Gear) - Needs: Progressive Hammer, Trio Plane (Logic)
    "DDD Oasis Room P Block": BlockData(0x007BB415, 0x40, 141, 14, 2, DDD), #Nut x2 - Needs: Progressive Hammer (Logic)
    "DDD Oasis Room Top Right Cliff Block": BlockData(0x007BB415, 0x80, 142, 1, 50, DDD), #50 Coin - Needs: Progressive Hammer, Trio Plane (Logic)
    "DDD Oasis Room Bottom Right Block": BlockData(0x007BB416, 0x01, 143, 1, 5, DDD), #5 Coin - Needs: Progressive Hammer (Logic)
    "DDD Oasis Room Top Left Block": BlockData(0x007BB419, 0x04, 144, 1, 5, DDD), #5 Coin - Needs: Progressive Hammer (Logic)
    "DDD Oasis Room Bottom Left Block": BlockData(0x007BB430, 0x40, 145, 1, 10, DDD), #10 Coin - Needs: Progressive Hammer (Logic)
 
    "DDD Papercraft Room Top Left Block": BlockData(0x007BB475, 0x40, 146, 1, 10, DDD), #10 Coin - Needs: 2x Progressive Hammer, Springboard (Logic)
    "DDD Papercraft Room Top Right Block": BlockData(0x007BB475, 0x80, 147, 1, 5, DDD), #5 Coin - Needs: 2x Progressive Hammer, Springboard (Logic)
    "DDD Papercraft Room Bottom Left Block": BlockData(0x007BB476, 0x01, 148, 1, 10, DDD), #10 Coin - Needs: 2x Progressive Hammer, Springboard (Logic)
    "DDD Papercraft Room Bottom Right Block": BlockData(0x007BB476, 0x02, 149, 14, 2, DDD), #Nut x2 - Needs: 2x Progressive Hammer, Springboard (Logic)
 
    "DDD Beach Room Top Left Left Block": BlockData(0x007BB418, 0x08, 150, 12, 3, DDD), #Ultra Mushroom x3 - Needs: Progressive Hammer (Logic)
    "DDD Beach Room Top Left Right Block": BlockData(0x007BB418, 0x10, 151, 1, 100, DDD), #100 Coin - Needs: Progressive Hammer (Logic)
    "DDD Beach Room Bottom Left Block": BlockData(0x007BB418, 0x20, 152, 1, 10, DDD), #10 Coin - Needs: Progressive Hammer (Logic)
    "DDD Beach Room Top Right Block": BlockData(0x007BB418, 0x40, 153, 1, 10, DDD), #10 Coin - Needs: Progressive Hammer (Logic)
    "DDD Beach Room Lower Island Left Block": BlockData(0x007BB418, 0x80, 154, 1, 50, DDD), #50 Coin - Needs: Progressive Hammer (Logic)
    "DDD Beach Room Upper Island Left Block": BlockData(0x007BB419, 0x01, 155, 1, 5, DDD), #5 Coin - Needs: Progressive Hammer (Logic)
    "DDD Beach Room Lower Island P Block": BlockData(0x007BB42A, 0x01, 156, 1, 100, DDD), #100 Coin - Needs: Progressive Hammer (Logic)
    "DDD Beach Room Upper Island Right Block": BlockData(0x007BB47C, 0x02, 157, 15, 2, DDD), #Super Nut x2 - Needs: Progressive Hammer (Logic)
    #DDD Beach Room leads to Twinsy Tropics so Logic for "Doop Doop Dunes to Twinsy Tropics" Needs: Progressive Hammer (Logic) (Region Logic) (Regions: Doop Doop Dunes, Twinsy Tropics)
 
    "DDD Right Underground Room Top Left Upper Block": BlockData(0x007BB40F, 0x80, 158, 1, 50, DDD), #50 Coin - Needs: 2x Progressive Hammer (Logic)
    "DDD Right Underground Room Top Left Lower Block": BlockData(0x007BB410, 0x01, 159, 1, 10, DDD), #10 Coin - Needs: 2x Progressive Hammer (Logic)
    "DDD Right Underground Room Top Middle Block": BlockData(0x007BB410, 0x02, 160, 1, 5, DDD), #5 Coin - Needs: 2x Progressive Hammer (Logic)
    "DDD Right Underground Room Bottom Left Block": BlockData(0x007BB410, 0x04, 161, 1, 10, DDD), #10 Coin - Needs: 2x Progressive Hammer (Logic)
    "DDD Right Underground Room Near Pipe Block": BlockData(0x007BB410, 0x08, 162, 1, 10, DDD), #10 Coin - Needs: Progressive Hammer (Logic)
    "DDD Right Underground Room Top Right Left Block": BlockData(0x007BB410, 0x10, 163, 22, 1, DDD), #Candy - Needs: 2x Progressive Hammer, Springboard (Logic)
    "DDD Right Underground Room Top Right P Block": BlockData(0x007BB410, 0x20, 164, None, 1, DDD), #HP Gloves (Gear) - Needs: 2x Progressive Hammer, Springboard (Logic)
    "DDD Right Underground Room Top Right Upper Block": BlockData(0x007BB410, 0x40, 165, 1, 10, DDD), #10 Coin - Needs: 2x Progressive Hammer, Springboard (Logic)
    "DDD Right Underground Room Top Right Lower Block": BlockData(0x007BB410, 0x80, 166, 1, 10, DDD), #10 Coin - Needs: 2x Progressive Hammer, Springboard (Logic)
    "DDD Right Underground Room Cliff Near Springboard Block": BlockData(0x007BB411, 0x80, 167, 18, 2, DDD), #Syrup Jar x2 - Needs: 2x Progressive Hammer, Springboard (Logic)
 
    "DDD Left Underground Room Top Left Block": BlockData(0x007BB412, 0x01, 168, None, 1, DDD), #Steady Hammer (Gear) - Needs: Progressive Hammer (Logic)
    "DDD Left Underground Room Bottom Block": BlockData(0x007BB412, 0x02, 169, 1, 5, DDD), #5 Coin - Needs: Progressive Hammer (Logic)
    "DDD Left Underground Room Top Middle Block": BlockData(0x007BB412, 0x04, 170, 1, 10, DDD), #10 Coin - Needs: Progressive Hammer (Logic)
    "DDD Left Underground Room Top Right Block": BlockData(0x007BB412, 0x08, 171, 10, 3, DDD), #Mushroom x3 - Needs: Progressive Hammer (Logic)
 
    "DDD Toad Town Bottom Left House Block": BlockData(0x007BB42F, 0x20, 172, 1, 5, DDD), #5 Coin - Needs: Progressive Hammer (Logic)
 
    "DDD Toad Town Bottom Right House Block": BlockData(0x007BB425, 0x20, 173, 30, 4, DDD), #Boo Biscuit x4 - Needs: Progressive Hammer (Logic)

    #DDD Beanspots 180-249
    "DDD First Room Bottom Left Beanspot": BlockData(0x007BB408, 0x08, 180, 31, 1, DDD), #Heart Bean
    "DDD First Room Top Left Lower Beanspot": BlockData(0x007BB408, 0x10, 181, 32, 1, DDD), #Bros. Bean
    "DDD First Room Top Left Upper Beanspot": BlockData(0x007BB408, 0x20, 182, 33, 1, DDD), #Power Bean
    "DDD First Room Middle Hill Beanspot": BlockData(0x007BB408, 0x40, 183, 34, 1, DDD), #Defense Bean
    "DDD First Room Top Right Beanspot": BlockData(0x007BB408, 0x80, 184, 35, 1, DDD), #Speed Bean
    "DDD First Room Right Hill Beanspot": BlockData(0x007BB409, 0x01, 185, 36, 1, DDD), #Stache Bean
    "DDD First Room Right Alcove Left Beanspot": BlockData(0x007BB409, 0x02, 186, 1, 50, DDD), #50 Coin
    "DDD First Room Right Alcove Middle Beanspot": BlockData(0x007BB409, 0x04, 187, 32, 1, DDD), #Bros. Bean
    "DDD First Room Right Alcove Right Beanspot": BlockData(0x007BB409, 0x08, 188, 1, 50, DDD), #50 Coin
    "DDD First Room Bottom Right Far Left Beanspot": BlockData(0x007BB409, 0x10, 189, 34, 1, DDD), #Defense Bean
    "DDD First Room Bottom Right Middle Left Beanspot": BlockData(0x007BB409, 0x20, 190, 35, 1, DDD), #Speed Bean
    "DDD First Room Bottom Right Middle Right Beanspot": BlockData(0x007BB409, 0x40, 191, 36, 1, DDD), #Stache Bean
    "DDD First Room Bottom Right Far Right Beanspot": BlockData(0x007BB409, 0x80, 192, 31, 1, DDD), #Heart Bean

    "DDD Second Room Top Left Lower Beanspot": BlockData(0x007BB40B, 0x04, 193, 31, 1, DDD), #Heart Bean
    "DDD Second Room Top Left Upper Beanspot": BlockData(0x007BB40B, 0x08, 194, 32, 1, DDD), #Bros. Bean
    "DDD Second Room Upper Left Cactus Beanspot": BlockData(0x007BB40B, 0x10, 195, 1, 50, DDD), #50 Coin
    "DDD Second Room Upper Right Cactus Beanspot": BlockData(0x007BB40B, 0x20, 196, 34, 1, DDD), #Defense Bean
    "DDD Second Room Lower Right Cactus Beanspot": BlockData(0x007BB40B, 0x40, 197, 35, 1, DDD), #Speed Bean
    "DDD Second Room Lower Left Cactus Beanspot": BlockData(0x007BB40B, 0x80, 198, 36, 1, DDD), #Stache Bean
    "DDD Second Room Right Upper Beanspot": BlockData(0x007BB40C, 0x01, 199, 31, 1, DDD), #Heart Bean
    "DDD Second Room Right Upper Middle Beanspot": BlockData(0x007BB40C, 0x02, 200, 1, 50, DDD), #50 Coin
    "DDD Second Room Right Lower Middle Beanspot": BlockData(0x007BB40C, 0x04, 201, 33, 1, DDD), #Power Bean
    "DDD Second Room Right Lower Beanspot": BlockData(0x007BB40C, 0x08, 202, 1, 50, DDD), #50 Coin

    "DDD Big Hill Room Star Formation Left Beanspot": BlockData(0x007BB40F, 0x08, 203, 1, 50, DDD), #50 Coin
    "DDD Big Hill Room Star Formation Top Beanspot": BlockData(0x007BB40F, 0x10, 204, 32, 1, DDD), #Bros. Bean
    "DDD Big Hill Room Star Formation Right Beanspot": BlockData(0x007BB40F, 0x20, 205, 1, 50, DDD), #50 Coin
    "DDD Big Hill Room Under Blocks Right Beanspot": BlockData(0x007BB40F, 0x40, 206, 32, 1, DDD), #Bros. Bean
    "DDD Big Hill Room Star Formation Lower Left Beanspot": BlockData(0x007BB414, 0x04, 207, 34, 1, DDD), #Defense Bean
    "DDD Big Hill Room Star Formation Lower Right Beanspot": BlockData(0x007BB414, 0x08, 208, 35, 1, DDD), #Speed Bean
    "DDD Big Hill Room Under Blocks Left Beanspot": BlockData(0x007BB414, 0x10, 209, 36, 1, DDD), #Stache Bean
    "DDD Big Hill Room Under Blocks Middle Beanspot": BlockData(0x007BB414, 0x20, 210, 31, 1, DDD), #Heart Bean

    "DDD Oasis Room Bottom 1st Beanspot": BlockData(0x007BB417, 0x01, 211, 1, 50, DDD), #50 Coin
    "DDD Oasis Room Bottom 2nd Beanspot": BlockData(0x007BB417, 0x02, 212, 32, 1, DDD), #Bros. Bean
    "DDD Oasis Room Bottom 3rd Beanspot": BlockData(0x007BB417, 0x04, 213, 33, 1, DDD), #Power Bean
    "DDD Oasis Room Bottom 4th Beanspot": BlockData(0x007BB417, 0x08, 214, 34, 1, DDD), #Defense Bean
    "DDD Oasis Room Bottom 5th Beanspot": BlockData(0x007BB417, 0x10, 215, 35, 1, DDD), #Speed Bean
    "DDD Oasis Room Bottom 6th Beanspot": BlockData(0x007BB417, 0x20, 216, 36, 1, DDD), #Stache Bean
    "DDD Oasis Room Bottom 7th Beanspot": BlockData(0x007BB417, 0x40, 217, 31, 1, DDD), #Heart Bean
    "DDD Oasis Room Bottom 8th Beanspot": BlockData(0x007BB417, 0x80, 218, 1, 50, DDD), #50 Coin
    "DDD Oasis Room Top Right Cliff Left Beanspot": BlockData(0x007BB45E, 0x04, 219, 33, 1, DDD), #Power Bean
    "DDD Oasis Room Top Right Cliff Middle Beanspot": BlockData(0x007BB45E, 0x08, 220, 34, 1, DDD), #Defense Bean
    "DDD Oasis Room Top Right Cliff Right Beanspot": BlockData(0x007BB47C, 0x01, 221, 35, 1, DDD), #Speed Bean

    "DDD Right Underground Room Very Top Beanspot": BlockData(0x007BB411, 0x01, 222, 31, 1, DDD), #Heart Bean
    "DDD Right Underground Room Top Left Upper Beanspot": BlockData(0x007BB411, 0x02, 223, 32, 1, DDD), #Bros. Bean
    "DDD Right Underground Room Top Left Middle Beanspot": BlockData(0x007BB411, 0x04, 224, 1, 50, DDD), #50 Coin
    "DDD Right Underground Room Top Left Lower Beanspot": BlockData(0x007BB411, 0x08, 225, 34, 1, DDD), #Defense Bean
    "DDD Right Underground Room Bottom Left Left Beanspot": BlockData(0x007BB411, 0x10, 226, 35, 1, DDD), #Speed Bean
    "DDD Right Underground Room Bottom Left Middle Beanspot": BlockData(0x007BB411, 0x20, 227, 36, 1, DDD), #Stache Bean
    "DDD Right Underground Room Bottom Left Right Beanspot": BlockData(0x007BB411, 0x40, 228, 31, 1, DDD), #Heart Bean

    "DDD Left Underground Room Above Pool Far Left Beanspot": BlockData(0x007BB412, 0x10, 229, 1, 50, DDD), #50 Coin
    "DDD Left Underground Room Above Pool Middle Left Beanspot": BlockData(0x007BB412, 0x20, 230, 1, 50, DDD), #50 Coin
    "DDD Left Underground Room Above Pool Middle Right Beanspot": BlockData(0x007BB412, 0x40, 231, 33, 1, DDD), #Power Bean
    "DDD Left Underground Room Above Pool Far Right Beanspot": BlockData(0x007BB412, 0x80, 232, 34, 1, DDD), #Defense Bean
    "DDD Left Underground Room Below Pool Far Left Beanspot": BlockData(0x007BB413, 0x01, 233, 1, 50, DDD), #50 Coin
    "DDD Left Underground Room Below Pool Middle Left Beanspot": BlockData(0x007BB413, 0x02, 234, 36, 1, DDD), #Stache Bean
    "DDD Left Underground Room Below Pool Middle Right Beanspot": BlockData(0x007BB413, 0x04, 235, 1, 50, DDD), #50 Coin
    "DDD Left Underground Room Below Pool Far Right Beanspot": BlockData(0x007BB413, 0x08, 236, 32, 1, DDD), #Bros. Bean
    "DDD Left Underground Room Bottom Middle Far Left Beanspot": BlockData(0x007BB413, 0x10, 237, 1, 50, DDD), #50 Coin
    "DDD Left Underground Room Bottom Middle Middle Left Beanspot": BlockData(0x007BB413, 0x20, 238, 1, 50, DDD), #50 Coin
    "DDD Left Underground Room Bottom Middle Middle Right Beanspot": BlockData(0x007BB413, 0x40, 239, 35, 1, DDD), #Speed Bean
    "DDD Left Underground Room Bottom Middle Far Right Beanspot": BlockData(0x007BB413, 0x80, 240, 36, 1, DDD), #Stache Bean

    #TT (Twinsy Tropics) 250-469
    #TT Blocks 250-349
    "f_island_01_1": BlockData(0x007BB41F, 0x40, 250, 1, 50, TT), #50 Coin
    "f_island_01_2": BlockData(0x007BB41F, 0x80, 251, 1, 10, TT), #10 Coin
    "f_island_01_3": BlockData(0x007BB420, 0x01, 252, 1, 5, TT), #5 Coin
    "f_island_01_4": BlockData(0x007BB420, 0x02, 253, 11, 3, TT), #Super Mushroom x3
    "f_island_01_5": BlockData(0x007BB420, 0x04, 254, 1, 10, TT), #10 Coin
 
    "f_island_02_1": BlockData(0x007BB420, 0x80, 255, None, 1, TT), #Anti-air Boots (Gear)
    "f_island_02_2": BlockData(0x007BB421, 0x01, 256, 1, 100, TT), #100 Coin
    "f_island_02_3": BlockData(0x007BB421, 0x02, 257, None, 1, TT), #Counter Belt (Gear)
    "f_island_02_4": BlockData(0x007BB421, 0x04, 258, 1, 10, TT), #10 Coin
 
    "f_island_03_1": BlockData(0x007BB422, 0x20, 259, 1, 5, TT), #5 Coin
 
    "f_island_04_2": BlockData(0x007BB423, 0x02, 260, 11, 3, TT), #Super Mushroom x3
    "f_island_04_1": BlockData(0x007BB423, 0x10, 261, 1, 10, TT), #10 Coin
    "f_island_04_2": BlockData(0x007BB423, 0x20, 262, 1, 50, TT), #50 Coin
    "f_island_04_3": BlockData(0x007BB423, 0x80, 263, 1, 5, TT), #5 Coin
    "f_island_04_4": BlockData(0x007BB424, 0x01, 264, 1, 10, TT), #10 Coin
    "f_island_04_5": BlockData(0x007BB424, 0x02, 265, 1, 50, TT), #50 Coin
    "f_island_04_6": BlockData(0x007BB424, 0x04, 266, 1, 10, TT), #10 Coin
    "f_island_04_7": BlockData(0x007BB424, 0x08, 267, 15, 1, TT), #Super Nut
    "f_island_04_8": BlockData(0x007BB424, 0x10, 268, 23, 1, TT), #Super Candy
 
    "f_island_05_1": BlockData(0x007BB424, 0x20, 269, 17, 2, TT), #Max Nut x2
    "f_island_05_2": BlockData(0x007BB426, 0x08, 270, 1, 10, TT), #10 Coin
    "f_island_05_3": BlockData(0x007BB426, 0x40, 271, 1, 10, TT), #10 Coin
    "f_island_05_4": BlockData(0x007BB42F, 0x04, 272, None, 1, TT), #Silver Statue (Gear)
    "f_island_05_5": BlockData(0x007BB430, 0x80, 273, 1, 10, TT), #10 Coin
    "f_island_05_6": BlockData(0x007BB432, 0x10, 274, 1, 5, TT), #5 Coin
    "f_island_05_7": BlockData(0x007BB43D, 0x01, 275, 1, 10, TT), #10 Coin
    "f_island_05_8": BlockData(0x007BB43D, 0x02, 276, 1, 50, TT), #50 Coin
    "f_island_05_9": BlockData(0x007BB43D, 0x20, 277, 13, 3, TT), #Max Mushroom x3
    "f_island_05_10": BlockData(0x007BB43D, 0x40, 278, 1, 5, TT), #5 Coin
 
    "f_island_06_1": BlockData(0x007BB427, 0x10, 279, 1, 50, TT), #50 Coin
    "f_island_06_2": BlockData(0x007BB427, 0x20, 280, 1, 10, TT), #10 Coin
    "f_island_06_3": BlockData(0x007BB427, 0x40, 281, 1, 5, TT), #5 Coin
    "f_island_06_4": BlockData(0x007BB427, 0x80, 282, 19, 2, TT), #Supersyrup Jar x2
    "f_island_06_5": BlockData(0x007BB428, 0x01, 283, 1, 10, TT), #10 Coin
    "f_island_06_6": BlockData(0x007BB428, 0x02, 284, 1, 100, TT), #100 Coin
    "f_island_06_7": BlockData(0x007BB428, 0x04, 285, 1, 5, TT), #5 Coin
    "f_island_06_8": BlockData(0x007BB428, 0x08, 286, None, 1, TT), #Filler Brooch (Gear)
 
    "f_island_07_1": BlockData(0x007BB44D, 0x10, 287, 1, 50, TT), #50 Coin
    "f_island_07_2": BlockData(0x007BB44D, 0x20, 288, 1, 10, TT), #10 Coin
    "f_island_07_3": BlockData(0x007BB44D, 0x40, 289, 1, 50, TT), #50 Coin
    "f_island_07_4": BlockData(0x007BB44D, 0x80, 290, 20, 2, TT), #Ultrasyrup Jar x2
    "f_island_07_5": BlockData(0x007BB44E, 0x01, 291, 1, 50, TT), #50 Coin
    "f_island_07_6": BlockData(0x007BB44E, 0x02, 292, 1, 10, TT), #10 Coin
 
    "f_island_09_1": BlockData(0x007BB419, 0x08, 293, 1, 10, TT), #10 Coin
    "f_island_09_2": BlockData(0x007BB419, 0x10, 294, 1, 50, TT), #50 Coin
    "f_island_09_3": BlockData(0x007BB419, 0x20, 295, 1, 10, TT), #10 Coin
    "f_island_09_4": BlockData(0x007BB419, 0x40, 296, 1, 5, TT), #5 Coin
 
    "f_island_11_1": BlockData(0x007BB41A, 0x04, 297, 18, 3, TT), #Syrup Jar x3
    "f_island_11_2": BlockData(0x007BB41A, 0x08, 298, 10, 5, TT), #Mushroom x5
 
    "f_island_12_1": BlockData(0x007BB41A, 0x80, 299, 1, 5, TT), #5 Coin
    "f_island_12_2": BlockData(0x007BB41B, 0x01, 300, 1, 50, TT), #50 Coin
    "f_island_12_3": BlockData(0x007BB41B, 0x02, 301, 1, 50, TT), #50 Coin
    "f_island_12_4": BlockData(0x007BB41B, 0x04, 302, 1, 10, TT), #10 Coin
    "f_island_12_5": BlockData(0x007BB43C, 0x08, 303, 10, 3, TT), #Mushroom x3
    "f_island_12_6": BlockData(0x007BB43C, 0x10, 304, None, 1, TT), #Rally Wear (Gear)
 
    "f_island_13_1": BlockData(0x007BB44B, 0x04, 305, 1, 100, TT), #100 Coin
    "f_island_13_2": BlockData(0x007BB44B, 0x08, 306, 28, 1, TT), #Double 1-Up Mushroom
    "f_island_13_3": BlockData(0x007BB44B, 0x10, 307, 1, 50, TT), #50 Coin
    "f_island_13_4": BlockData(0x007BB44B, 0x20, 308, 1, 100, TT), #100 Coin
    "f_island_13_5": BlockData(0x007BB44C, 0x80, 309, 1, 50, TT), #50 Coin
    "f_island_13_6": BlockData(0x007BB44D, 0x01, 310, 1, 10, TT), #10 Coin
    "f_island_13_7": BlockData(0x007BB44D, 0x02, 311, 1, 100, TT), #100 Coin
    "f_island_13_8": BlockData(0x007BB44D, 0x04, 312, 12, 2, TT), #Ultra Mushroom x2
    "f_island_13_9": BlockData(0x007BB44D, 0x08, 313, 1, 10, TT), #10 Coin
 
    "f_island_14_1": BlockData(0x007BB41C, 0x04, 314, 26, 3, TT), #1-Up Mushroom x3
 
    "f_island_15_1": BlockData(0x007BB41C, 0x08, 315, 14, 2, TT), #Nut x2
    "f_island_15_2": BlockData(0x007BB41C, 0x10, 316, 1, 10, TT), #10 Coin
    "f_island_15_3": BlockData(0x007BB41C, 0x20, 317, 1, 5, TT), #5 Coin
    "f_island_15_4": BlockData(0x007BB41C, 0x40, 318, 1, 10, TT), #10 Coin
 
    "f_island_16_1": BlockData(0x007BB41D, 0x20, 319, None, 1, TT), #Bare Boots (Gear)
    "f_island_16_2": BlockData(0x007BB41D, 0x40, 320, 1, 50, TT), #50 Coin
    "f_island_16_3": BlockData(0x007BB41D, 0x80, 321, 1, 5, TT), #5 Coin
    "f_island_16_4": BlockData(0x007BB41E, 0x01, 322, 1, 50, TT), #50 Coin
    "f_island_16_5": BlockData(0x007BB41E, 0x02, 323, 22, 1, TT), #Candy
    "f_island_16_6": BlockData(0x007BB41F, 0x08, 324, 14, 2, TT), #Nut x2
    "f_island_16_7": BlockData(0x007BB41F, 0x10, 325, 1, 10, TT), #10 Coin
    "f_island_16_8": BlockData(0x007BB41F, 0x20, 326, 28, 1, TT), #Double 1-Up Mushroom
 
    "f_island_17_1": BlockData(0x007BB44E, 0x04, 327, 1, 50, TT), #50 Coin
    "f_island_17_2": BlockData(0x007BB44E, 0x08, 328, 1, 10, TT), #10 Coin
    "f_island_17_3": BlockData(0x007BB44E, 0x10, 329, 1, 50, TT), #50 Coin
    "f_island_17_4": BlockData(0x007BB44E, 0x20, 330, 16, 1, TT), #Ultra Nut
    "f_island_17_5": BlockData(0x007BB44E, 0x40, 331, 1, 100, TT), #100 Coin
 
    "f_island_18_1": BlockData(0x007BB450, 0x10, 332, 1, 50, TT), #50 Coin
    "f_island_18_2": BlockData(0x007BB450, 0x20, 333, 1, 50, TT), #50 Coin
    "f_island_18_3": BlockData(0x007BB450, 0x40, 334, 1, 10, TT), #10 Coin
    "f_island_18_4": BlockData(0x007BB450, 0x80, 335, None, 1, TT), #Retribution Wear DX (Gear)
 
    "f_island_19_1": BlockData(0x007BB464, 0x20, 336, None, 1, TT), #Rally Belt (Gear)
    "f_island_19_2": BlockData(0x007BB464, 0x40, 337, 1, 10, TT), #10 Coin
 
    "f_island_20_1": BlockData(0x007BB451, 0x20, 338, 1, 50, TT), #50 Coin
    "f_island_20_2": BlockData(0x007BB451, 0x40, 339, 1, 50, TT), #50 Coin
    "f_island_20_3": BlockData(0x007BB451, 0x80, 340, 1, 100, TT), #100 Coin
    "f_island_20_4": BlockData(0x007BB452, 0x01, 341, 1, 50, TT), #50 Coin
    "f_island_20_5": BlockData(0x007BB452, 0x02, 342, 24, 1, TT), #Ultra Candy
    "f_island_20_6": BlockData(0x007BB452, 0x20, 343, None, 1, TT), #Counter Charge Gloves (Gear)
    "f_island_20_7": BlockData(0x007BB452, 0x40, 344, 1, 50, TT), #50 Coin

    #TT Beanspots 350-469
    "f_island_01_b1": BlockData(0x007BB420, 0x08, 350, 31, 1, TT), #Heart Bean
    "f_island_01_b2": BlockData(0x007BB420, 0x10, 351, 32, 1, TT), #Bros. Bean
    "f_island_01_b3": BlockData(0x007BB420, 0x20, 352, 1, 50, TT), #50 Coin
    "f_island_01_b4": BlockData(0x007BB420, 0x40, 353, 34, 1, TT), #Defense Bean
 
    "f_island_02_b1": BlockData(0x007BB421, 0x08, 354, 1, 50, TT), #50 Coin
    "f_island_02_b2": BlockData(0x007BB421, 0x10, 355, 36, 1, TT), #Stache Bean
    "f_island_02_b3": BlockData(0x007BB421, 0x20, 356, 31, 1, TT), #Heart Bean
    "f_island_02_b4": BlockData(0x007BB421, 0x40, 357, 32, 1, TT), #Bros. Bean
    "f_island_02_b5": BlockData(0x007BB421, 0x80, 358, 33, 1, TT), #Power Bean
    "f_island_02_b6": BlockData(0x007BB422, 0x01, 359, 34, 1, TT), #Defense Bean
    "f_island_02_b7": BlockData(0x007BB422, 0x02, 360, 1, 50, TT), #50 Coin
 
    "f_island_03_b1": BlockData(0x007BB422, 0x04, 361, 1, 50, TT), #50 Coin
    "f_island_03_b2": BlockData(0x007BB422, 0x08, 362, 35, 1, TT), #Speed Bean
    "f_island_03_b3": BlockData(0x007BB422, 0x10, 363, 36, 1, TT), #Stache Bean
 
    "f_island_04_b1": BlockData(0x007BB422, 0x80, 364, 1, 50, TT), #50 Coin
    "f_island_04_b2": BlockData(0x007BB423, 0x01, 365, 32, 1, TT), #Bros. Bean
    "f_island_04_b3": BlockData(0x007BB423, 0x04, 366, 1, 50, TT), #50 Coin
    "f_island_04_b4": BlockData(0x007BB423, 0x08, 367, 1, 50, TT), #50 Coin
    "f_island_04_b5": BlockData(0x007BB423, 0x40, 368, 1, 50, TT), #50 Coin
 
    "f_island_05_b1": BlockData(0x007BB425, 0x01, 369, 32, 1, TT), #Bros. Bean
    "f_island_05_b2": BlockData(0x007BB425, 0x02, 370, 1, 50, TT), #50 Coin
    "f_island_05_b3": BlockData(0x007BB426, 0x01, 371, 35, 1, TT), #Speed Bean
    "f_island_05_b4": BlockData(0x007BB426, 0x02, 372, 36, 1, TT), #Stache Bean
    "f_island_05_b5": BlockData(0x007BB426, 0x04, 373, 34, 1, TT), #Defense Bean
    "f_island_05_b6": BlockData(0x007BB426, 0x10, 374, 1, 50, TT), #50 Coin
    "f_island_05_b7": BlockData(0x007BB426, 0x20, 375, 1, 50, TT), #50 Coin
    "f_island_05_b8": BlockData(0x007BB426, 0x80, 376, 31, 1, TT), #Heart Bean
    "f_island_05_b9": BlockData(0x007BB432, 0x08, 377, 1, 50, TT), #50 Coin
    "f_island_05_b10": BlockData(0x007BB436, 0x20, 378, 34, 1, TT), #Defense Bean
    "f_island_05_b11": BlockData(0x007BB442, 0x04, 379, 1, 50, TT), #50 Coin
    "f_island_05_b12": BlockData(0x007BB46A, 0x08, 380, 32, 1, TT), #Bros. Bean
    "f_island_05_b13": BlockData(0x007BB46A, 0x10, 381, 33, 1, TT), #Power Bean
 
    "f_island_06_b1": BlockData(0x007BB429, 0x08, 382, 35, 1, TT), #Speed Bean
    "f_island_06_b2": BlockData(0x007BB429, 0x10, 383, 36, 1, TT), #Stache Bean
    "f_island_06_b3": BlockData(0x007BB429, 0x20, 384, 1, 50, TT), #50 Coin
    "f_island_06_b4": BlockData(0x007BB429, 0x40, 385, 32, 1, TT), #Bros. Bean
    "f_island_06_b5": BlockData(0x007BB429, 0x80, 386, 1, 50, TT), #50 Coin
    "f_island_06_b6": BlockData(0x007BB42A, 0x02, 387, 34, 1, TT), #Defense Bean
    "f_island_06_b7": BlockData(0x007BB435, 0x10, 388, 35, 1, TT), #Speed Bean
 
    "f_island_09_b1": BlockData(0x007BB419, 0x80, 389, 1, 50, TT), #50 Coin
    "f_island_09_b2": BlockData(0x007BB41A, 0x01, 390, 32, 1, TT), #Bros. Bean
    "f_island_09_b3": BlockData(0x007BB41A, 0x02, 391, 33, 1, TT), #Power Bean
 
    "f_island_11_b1": BlockData(0x007BB41A, 0x10, 392, 34, 1, TT), #Defense Bean
    "f_island_11_b2": BlockData(0x007BB41A, 0x20, 393, 35, 1, TT), #Speed Bean
    "f_island_11_b3": BlockData(0x007BB41A, 0x40, 394, 36, 1, TT), #Stache Bean
 
    "f_island_12_b1": BlockData(0x007BB41B, 0x08, 395, 1, 50, TT), #50 Coin
    "f_island_12_b2": BlockData(0x007BB41B, 0x10, 396, 1, 50, TT), #50 Coin
    "f_island_12_b3": BlockData(0x007BB41B, 0x20, 397, 33, 1, TT), #Power Bean
    "f_island_12_b4": BlockData(0x007BB41B, 0x40, 398, 1, 50, TT), #50 Coin
    "f_island_12_b5": BlockData(0x007BB41B, 0x80, 399, 1, 50, TT), #50 Coin
    "f_island_12_b6": BlockData(0x007BB41C, 0x01, 400, 36, 1, TT), #Stache Bean
    "f_island_12_b7": BlockData(0x007BB41C, 0x02, 401, 31, 1, TT), #Heart Bean
 
    "f_island_13_b1": BlockData(0x007BB44C, 0x40, 402, 31, 1, TT), #Heart Bean
 
    "f_island_15_b1": BlockData(0x007BB41C, 0x80, 403, 31, 1, TT), #Heart Bean
    "f_island_15_b2": BlockData(0x007BB41D, 0x01, 404, 1, 50, TT), #50 Coin
    "f_island_15_b3": BlockData(0x007BB41D, 0x02, 405, 33, 1, TT), #Power Bean
    "f_island_15_b4": BlockData(0x007BB41D, 0x04, 406, 34, 1, TT), #Defense Bean
    "f_island_15_b5": BlockData(0x007BB41D, 0x08, 407, 35, 1, TT), #Speed Bean
    "f_island_15_b6": BlockData(0x007BB41D, 0x10, 408, 36, 1, TT), #Stache Bean
 
    "f_island_16_b1": BlockData(0x007BB41E, 0x04, 409, 31, 1, TT), #Heart Bean
    "f_island_16_b2": BlockData(0x007BB41E, 0x08, 410, 1, 50, TT), #50 Coin
    "f_island_16_b3": BlockData(0x007BB41E, 0x10, 411, 33, 1, TT), #Power Bean
    "f_island_16_b4": BlockData(0x007BB41E, 0x20, 412, 34, 1, TT), #Defense Bean
    "f_island_16_b5": BlockData(0x007BB41E, 0x40, 413, 35, 1, TT), #Speed Bean
    "f_island_16_b6": BlockData(0x007BB41E, 0x80, 414, 36, 1, TT), #Stache Bean
    "f_island_16_b7": BlockData(0x007BB41F, 0x01, 415, 31, 1, TT), #Heart Bean
    "f_island_16_b8": BlockData(0x007BB41F, 0x02, 416, 32, 1, TT), #Bros. Bean
    "f_island_16_b9": BlockData(0x007BB41F, 0x04, 417, 1, 50, TT), #50 Coin
 
    "f_island_17_b1": BlockData(0x007BB44E, 0x80, 418, 31, 1, TT), #Heart Bean
    "f_island_17_b2": BlockData(0x007BB44F, 0x01, 419, 1, 50, TT), #50 Coin
    "f_island_17_b3": BlockData(0x007BB44F, 0x02, 420, 1, 50, TT), #50 Coin
    "f_island_17_b4": BlockData(0x007BB44F, 0x04, 421, 1, 50, TT), #50 Coin
    "f_island_17_b5": BlockData(0x007BB44F, 0x08, 422, 35, 1, TT), #Speed Bean
    "f_island_17_b6": BlockData(0x007BB44F, 0x10, 423, 1, 50, TT), #50 Coin
    "f_island_17_b7": BlockData(0x007BB44F, 0x20, 424, 31, 1, TT), #Heart Bean
    "f_island_17_b8": BlockData(0x007BB44F, 0x40, 425, 1, 50, TT), #50 Coin
    "f_island_17_b9": BlockData(0x007BB44F, 0x80, 426, 33, 1, TT), #Power Bean
    "f_island_17_b10": BlockData(0x007BB450, 0x01, 427, 34, 1, TT), #Defense Bean
    "f_island_17_b11": BlockData(0x007BB450, 0x02, 428, 35, 1, TT), #Speed Bean
    "f_island_17_b12": BlockData(0x007BB450, 0x04, 429, 1, 50, TT), #50 Coin
    "f_island_17_b13": BlockData(0x007BB450, 0x08, 430, 1, 50, TT), #50 Coin
 
    "f_island_18_b1": BlockData(0x007BB451, 0x01, 431, 1, 50, TT), #50 Coin
    "f_island_18_b2": BlockData(0x007BB451, 0x02, 432, 1, 50, TT), #50 Coin
    "f_island_18_b3": BlockData(0x007BB451, 0x04, 433, 1, 50, TT), #50 Coin
    "f_island_18_b4": BlockData(0x007BB462, 0x10, 434, 1, 50, TT), #50 Coin
    "f_island_18_b5": BlockData(0x007BB462, 0x20, 435, 35, 1, TT), #Speed Bean
    "f_island_18_b6": BlockData(0x007BB462, 0x40, 436, 36, 1, TT), #Stache Bean
    "f_island_18_b7": BlockData(0x007BB462, 0x80, 437, 1, 50, TT), #50 Coin
    "f_island_18_b8": BlockData(0x007BB463, 0x01, 438, 32, 1, TT), #Bros. Bean
    "f_island_18_b9": BlockData(0x007BB463, 0x02, 439, 33, 1, TT), #Power Bean
    "f_island_18_b10": BlockData(0x007BB463, 0x04, 440, 34, 1, TT), #Defense Bean
    "f_island_18_b11": BlockData(0x007BB463, 0x08, 441, 35, 1, TT), #Speed Bean
    "f_island_18_b12": BlockData(0x007BB463, 0x10, 442, 1, 50, TT), #50 Coin
    "f_island_18_b13": BlockData(0x007BB463, 0x20, 443, 31, 1, TT), #Heart Bean
    "f_island_18_b14": BlockData(0x007BB463, 0x40, 444, 1, 50, TT), #50 Coin
    "f_island_18_b15": BlockData(0x007BB463, 0x80, 445, 1, 50, TT), #50 Coin
    "f_island_18_b16": BlockData(0x007BB464, 0x01, 446, 34, 1, TT), #Defense Bean
    "f_island_18_b17": BlockData(0x007BB464, 0x02, 447, 1, 50, TT), #50 Coin
    "f_island_18_b18": BlockData(0x007BB464, 0x04, 448, 36, 1, TT), #Stache Bean
    "f_island_18_b19": BlockData(0x007BB464, 0x08, 449, 1, 50, TT), #50 Coin
    "f_island_18_b20": BlockData(0x007BB464, 0x10, 450, 32, 1, TT), #Bros. Bean
 
    "f_island_19_b1": BlockData(0x007BB451, 0x08, 451, 1, 50, TT), #50 Coin
    "f_island_19_b2": BlockData(0x007BB451, 0x10, 452, 1, 50, TT), #50 Coin
    "f_island_19_b3": BlockData(0x007BB464, 0x80, 453, 1, 50, TT), #50 Coin
    "f_island_19_b4": BlockData(0x007BB465, 0x01, 454, 1, 50, TT), #50 Coin
    "f_island_19_b5": BlockData(0x007BB465, 0x02, 455, 1, 50, TT), #50 Coin
    "f_island_19_b6": BlockData(0x007BB465, 0x04, 456, 1, 50, TT), #50 Coin
    "f_island_19_b7": BlockData(0x007BB465, 0x08, 457, 1, 50, TT), #50 Coin
    "f_island_19_b8": BlockData(0x007BB465, 0x10, 458, 36, 1, TT), #Stache Bean
    "f_island_19_b9": BlockData(0x007BB465, 0x20, 459, 1, 50, TT), #50 Coin
    "f_island_19_b10": BlockData(0x007BB465, 0x40, 460, 34, 1, TT), #Defense Bean
    "f_island_19_b11": BlockData(0x007BB465, 0x80, 461, 1, 50, TT), #50 Coin
    "f_island_19_b12": BlockData(0x007BB466, 0x01, 462, 36, 1, TT), #Stache Bean
    "f_island_19_b13": BlockData(0x007BB466, 0x02, 463, 31, 1, TT), #Heart Bean
    "f_island_19_b14": BlockData(0x007BB466, 0x04, 464, 32, 1, TT), #Bros. Bean
 
    "f_island_20_b1": BlockData(0x007BB452, 0x04, 465, 1, 50, TT), #50 Coin
    "f_island_20_b2": BlockData(0x007BB452, 0x08, 466, 35, 1, TT), #Speed Bean
    "f_island_20_b3": BlockData(0x007BB452, 0x10, 467, 33, 1, TT), #Power Bean
    "f_island_20_b4": BlockData(0x007BB475, 0x02, 468, 1, 50, TT), #50 Coin
    "f_island_20_b5": BlockData(0x007BB475, 0x04, 469, 32, 1, TT), #Bros. Bean

    #GW (Gloomy Woods) 470-559
    #GW Blocks 470-529
    "f_forest_01_1": BlockData(0x007BB430, 0x02, 470, 1, 5, GW), #5 Coin
    "f_forest_01_2": BlockData(0x007BB430, 0x04, 471, 11, 2, GW), #Super Mushroom x2
    "f_forest_01_3": BlockData(0x007BB430, 0x08, 472, 1, 50, GW), #50 Coin
    "f_forest_01_4": BlockData(0x007BB430, 0x10, 473, 1, 50, GW), #50 Coin
    "f_forest_01_5": BlockData(0x007BB46A, 0x20, 474, 1, 10, GW), #10 Coin
    "f_forest_01_6": BlockData(0x007BB474, 0x02, 475, None, 1, GW), #Filler Wear DX (Gear)
 
    "f_forest_02_1": BlockData(0x007BB431, 0x04, 476, None, 1, GW), #Origami Boots (Gear)
    "f_forest_02_2": BlockData(0x007BB431, 0x08, 477, 1, 10, GW), #10 Coin
    "f_forest_02_3": BlockData(0x007BB431, 0x10, 478, 1, 10, GW), #10 Coin
    "f_forest_02_4": BlockData(0x007BB431, 0x20, 479, None, 1, GW), #Koopa Troopa Wear (Gear)
    "f_forest_02_5": BlockData(0x007BB43F, 0x02, 480, 1, 10, GW), #10 Coin
 
    "f_forest_03_1": BlockData(0x007BB432, 0x01, 481, 1, 5, GW), #5 Coin
    "f_forest_03_2": BlockData(0x007BB432, 0x02, 482, 1, 50, GW), #50 Coin
    "f_forest_03_3": BlockData(0x007BB432, 0x04, 483, 1, 5, GW), #5 Coin
    "f_forest_03_4": BlockData(0x007BB46B, 0x01, 484, 19, 2, GW), #Supersyrup Jar x2
 
    "f_forest_04_1": BlockData(0x007BB432, 0x80, 485, 1, 5, GW), #5 Coin
    "f_forest_04_2": BlockData(0x007BB433, 0x01, 486, 1, 10, GW), #10 Coin
    "f_forest_04_3": BlockData(0x007BB433, 0x02, 487, 1, 50, GW), #50 Coin
    "f_forest_04_4": BlockData(0x007BB433, 0x04, 488, None, 1, GW), #Silver Statue (Gear)
 
    "f_forest_05_1": BlockData(0x007BB434, 0x08, 489, 1, 10, GW), #10 Coin
    "f_forest_05_2": BlockData(0x007BB434, 0x10, 490, 1, 5, GW), #5 Coin
    "f_forest_05_3": BlockData(0x007BB434, 0x20, 491, None, 1, GW), #Filler Gloves (Gear)
 
    "f_forest_06_1": BlockData(0x007BB42F, 0x10, 492, 12, 3, GW), #Ultra Mushroom x3
    "f_forest_06_2": BlockData(0x007BB434, 0x40, 493, 1, 100, GW), #100 Coin
    "f_forest_06_3": BlockData(0x007BB434, 0x80, 494, 24, 1, GW), #Ultra Candy
    "f_forest_06_4": BlockData(0x007BB435, 0x01, 495, 1, 50, GW), #50 Coin
    "f_forest_06_5": BlockData(0x007BB435, 0x02, 496, 15, 2, GW), #Super Nut x2
    "f_forest_06_6": BlockData(0x007BB435, 0x04, 497, 1, 5, GW), #5 Coin
 
    "f_forest_07_1": BlockData(0x007BB458, 0x20, 498, 16, 1, GW), #Ultra Nut
    "f_forest_07_2": BlockData(0x007BB46C, 0x10, 499, 20, 2, GW), #Ultrasyrup Jar x2
    "f_forest_07_3": BlockData(0x007BB471, 0x40, 500, 1, 100, GW), #100 Coin
    "f_forest_07_4": BlockData(0x007BB475, 0x08, 501, 1, 50, GW), #50 Coin
 
    "f_forest_08_1": BlockData(0x007BB455, 0x40, 502, None, 1, GW), #Flame Hammer DX (Gear)
    "f_forest_08_2": BlockData(0x007BB470, 0x02, 503, 1, 50, GW), #50 Coin
 
    "f_forest_09_1": BlockData(0x007BB455, 0x04, 504, 1, 10, GW), #10 Coin
    "f_forest_09_2": BlockData(0x007BB455, 0x08, 505, 1, 100, GW), #100 Coin
    "f_forest_09_3": BlockData(0x007BB455, 0x10, 506, 12, 2, GW), #Ultra Mushroom x2
    "f_forest_09_4": BlockData(0x007BB455, 0x20, 507, 1, 50, GW), #50 Coin
 
    "f_forest_10_1": BlockData(0x007BB456, 0x04, 508, 16, 1, GW), #Ultra Nut
    "f_forest_10_2": BlockData(0x007BB456, 0x10, 509, 1, 50, GW), #50 Coin
    "f_forest_10_3": BlockData(0x007BB456, 0x20, 510, 1, 50, GW), #50 Coin
    "f_forest_10_4": BlockData(0x007BB456, 0x40, 511, 1, 10, GW), #10 Coin
    "f_forest_10_5": BlockData(0x007BB46B, 0x40, 512, 1, 50, GW), #50 Coin
    "f_forest_10_6": BlockData(0x007BB46F, 0x40, 513, 27, 1, GW), #1-Up DX
 
    "f_forest_11_1": BlockData(0x007BB457, 0x01, 514, 1, 50, GW), #50 Coin
    "f_forest_11_2": BlockData(0x007BB457, 0x10, 515, 28, 2, GW), #Double 1-Up Mushroom x2
    "f_forest_11_3": BlockData(0x007BB46F, 0x80, 516, 1, 50, GW), #50 Coin
    "f_forest_11_4": BlockData(0x007BB473, 0x40, 517, 1, 50, GW), #50 Coin
    "f_forest_11_5": BlockData(0x007BB474, 0x04, 518, 1, 10, GW), #10 Coin
 
    "f_forest_12_1": BlockData(0x007BB458, 0x80, 519, 1, 50, GW), #50 Coin
    "f_forest_12_2": BlockData(0x007BB459, 0x01, 520, 1, 10, GW), #10 Coin
    "f_forest_12_3": BlockData(0x007BB459, 0x02, 521, 1, 100, GW), #100 Coin
    "f_forest_12_4": BlockData(0x007BB459, 0x04, 522, 16, 1, GW), #Ultra Nut
    "f_forest_12_5": BlockData(0x007BB459, 0x08, 523, 1, 50, GW), #50 Coin
    "f_forest_12_6": BlockData(0x007BB459, 0x10, 524, 1, 10, GW), #10 Coin
    "f_forest_12_7": BlockData(0x007BB459, 0x20, 525, None, 1, GW), #Filler Brooch DX (Gear)

    #GW Beanspots 530-559
    "f_forest_03_b1": BlockData(0x007BB431, 0x40, 530, 1, 50, GW), #50 Coin
    "f_forest_03_b2": BlockData(0x007BB431, 0x80, 531, 32, 1, GW), #Bros. Bean
    "f_forest_03_b3": BlockData(0x007BB441, 0x01, 532, 36, 1, GW), #Stache Bean
    "f_forest_03_b4": BlockData(0x007BB441, 0x02, 533, 1, 50, GW), #50 Coin
    "f_forest_03_b5": BlockData(0x007BB46A, 0x40, 534, 1, 50, GW), #50 Coin
    "f_forest_03_b6": BlockData(0x007BB46A, 0x80, 535, 34, 1, GW), #Defense Bean
    "f_forest_03_b7": BlockData(0x007BB46B, 0x02, 536, 35, 1, GW), #Speed Bean
 
    "f_forest_06_b1": BlockData(0x007BB42F, 0x08, 537, 1, 50, GW), #50 Coin
    "f_forest_06_b2": BlockData(0x007BB435, 0x20, 538, 1, 50, GW), #50 Coin
    "f_forest_06_b3": BlockData(0x007BB436, 0x08, 539, 31, 1, GW), #Heart Bean
    "f_forest_06_b4": BlockData(0x007BB436, 0x10, 540, 33, 1, GW), #Power Bean
 
    "f_forest_07_b1": BlockData(0x007BB454, 0x20, 541, 34, 1, GW), #Defense Bean
    "f_forest_07_b2": BlockData(0x007BB454, 0x40, 542, 1, 100, GW), #100 Coin
    "f_forest_07_b3": BlockData(0x007BB457, 0x08, 543, 36, 1, GW), #Stache Bean
 
    "f_forest_09_b1": BlockData(0x007BB453, 0x04, 544, 1, 100, GW), #100 Coin
    "f_forest_09_b2": BlockData(0x007BB453, 0x08, 545, 31, 1, GW), #Heart Bean
    "f_forest_09_b3": BlockData(0x007BB456, 0x01, 546, 32, 1, GW), #Bros. Bean
 
    "f_forest_11_b1": BlockData(0x007BB458, 0x04, 547, 1, 50, GW), #50 Coin
    "f_forest_11_b2": BlockData(0x007BB458, 0x08, 548, 1, 50, GW), #50 Coin
    "f_forest_11_b3": BlockData(0x007BB458, 0x40, 549, 33, 1, GW), #Power Bean
    "f_forest_11_b4": BlockData(0x007BB469, 0x04, 550, 35, 1, GW), #Speed Bean

    #MB (Mount Brrr) 560-729
    #MB Blocks 560-619
    "f_mount_01_1": BlockData(0x007BB437, 0x20, 560, 1, 50, MB), #50 Coin
    "f_mount_01_2": BlockData(0x007BB437, 0x40, 561, None, 1, MB), #Singular Hammer (Gear)
    "f_mount_01_3": BlockData(0x007BB437, 0x80, 562, 1, 100, MB), #100 Coin
    "f_mount_01_4": BlockData(0x007BB438, 0x01, 563, 1, 10, MB), #10 Coin
    "f_mount_01_5": BlockData(0x007BB438, 0x02, 564, 1, 50, MB), #50 Coin
    "f_mount_01_6": BlockData(0x007BB438, 0x04, 565, 17, 1, MB), #Max Nut
    "f_mount_01_7": BlockData(0x007BB438, 0x08, 566, 1, 5, MB), #5 Coin
 
    "f_mount_02_1": BlockData(0x007BB43C, 0x02, 567, 1, 50, MB), #50 Coin
    "f_mount_02_2": BlockData(0x007BB43C, 0x04, 568, 1, 50, MB), #50 Coin
    "f_mount_02_3": BlockData(0x007BB455, 0x80, 569, 28, 1, MB), #Double 1-Up Mushroom
    "f_mount_02_4": BlockData(0x007BB473, 0x08, 570, 1, 100, MB), #100 Coin
 
    "f_mount_03_1": BlockData(0x007BB47D, 0x02, 571, None, 1, MB), #Paper SPEED Bracelet (Gear)
 
    "f_mount_04_1": BlockData(0x007BB43F, 0x20, 572, 1, 50, MB), #50 Coin
    "f_mount_04_2": BlockData(0x007BB43F, 0x40, 573, 1, 50, MB), #50 Coin
    "f_mount_04_3": BlockData(0x007BB43F, 0x80, 574, 1, 5, MB), #5 Coin
    "f_mount_04_4": BlockData(0x007BB440, 0x01, 575, 1, 50, MB), #50 Coin
 
    "f_mount_05_1": BlockData(0x007BB441, 0x10, 576, 1, 100, MB), #100 Coin
    "f_mount_05_2": BlockData(0x007BB448, 0x02, 577, None, 1, MB), #Metal Gloves (Gear)
    "f_mount_05_3": BlockData(0x007BB448, 0x04, 578, 1, 50, MB), #50 Coin
    "f_mount_05_4": BlockData(0x007BB448, 0x08, 579, 1, 5, MB), #5 Coin
    "f_mount_05_5": BlockData(0x007BB448, 0x10, 580, 1, 10, MB), #10 Coin
    "f_mount_05_6": BlockData(0x007BB474, 0x80, 581, 15, 2, MB), #Super Nut x2
    "f_mount_05_7": BlockData(0x007BB475, 0x01, 582, 11, 3, MB), #Super Mushroom x3
 
    "f_mount_06_1": BlockData(0x007BB436, 0x40, 583, 1, 50, MB), #50 Coin
    "f_mount_06_2": BlockData(0x007BB436, 0x80, 584, 1, 10, MB), #10 Coin
    "f_mount_06_3": BlockData(0x007BB442, 0x02, 585, 1, 50, MB), #50 Coin
 
    "f_mount_07_1": BlockData(0x007BB442, 0x08, 586, 1, 50, MB), #50 Coin
    "f_mount_07_2": BlockData(0x007BB442, 0x10, 587, 1, 10, MB), #10 Coin
    "f_mount_07_3": BlockData(0x007BB453, 0x10, 588, 11, 3, MB), #Super Mushroom x3
    "f_mount_07_4": BlockData(0x007BB456, 0x08, 589, 1, 50, MB), #50 Coin
    "f_mount_07_5": BlockData(0x007BB46B, 0x80, 590, 1, 5, MB), #5 Coin
 
    "f_mount_08_1": BlockData(0x007BB442, 0x80, 591, 1, 50, MB), #50 Coin
    "f_mount_08_2": BlockData(0x007BB443, 0x01, 592, 27, 3, MB), #1-Up DX x3
    "f_mount_08_3": BlockData(0x007BB449, 0x20, 593, 1, 50, MB), #50 Coin
    "f_mount_08_4": BlockData(0x007BB454, 0x10, 594, 1, 5, MB), #5 Coin
 
    "f_mount_09_1": BlockData(0x007BB443, 0x40, 595, 1, 50, MB), #50 Coin
 
    "f_mount_10_1": BlockData(0x007BB44B, 0x01, 596, None, 1, MB), #Paper POW Bracelet (Gear)
 
    "f_mount_11_1": BlockData(0x007BB46C, 0x40, 597, 1, 50, MB), #50 Coin
    "f_mount_11_2": BlockData(0x007BB47A, 0x08, 598, 1, 10, MB), #10 Coin
 
    "f_mount_12_1": BlockData(0x007BB45C, 0x40, 599, 1, 100, MB), #100 Coin
    "f_mount_12_2": BlockData(0x007BB45C, 0x80, 600, 13, 2, MB), #Max Mushroom x2
    "f_mount_12_3": BlockData(0x007BB45D, 0x01, 601, 1, 50, MB), #50 Coin
    "f_mount_12_4": BlockData(0x007BB45D, 0x02, 602, 1, 10, MB), #10 Coin
    "f_mount_12_5": BlockData(0x007BB45D, 0x04, 603, None, 1, MB), #Boost Wear DX (Gear)
    "f_mount_12_6": BlockData(0x007BB45D, 0x08, 604, 1, 50, MB), #50 Coin
    "f_mount_12_7": BlockData(0x007BB46D, 0x04, 605, 1, 50, MB), #50 Coin
 
    "f_mount_13_1": BlockData(0x007BB45D, 0x10, 606, 1, 100, MB), #100 Coin
    "f_mount_13_2": BlockData(0x007BB45D, 0x20, 607, 21, 2, MB), #Max Syrup Jar x2
    "f_mount_13_3": BlockData(0x007BB45D, 0x40, 608, 1, 10, MB), #10 Coin
 
    "f_mount_14_1": BlockData(0x007BB444, 0x20, 609, 1, 100, MB), #100 Coin
    "f_mount_14_2": BlockData(0x007BB449, 0x40, 610, 1, 100, MB), #100 Coin
    "f_mount_14_3": BlockData(0x007BB46E, 0x01, 611, 1, 10, MB), #10 Coin
    "f_mount_14_4": BlockData(0x007BB46E, 0x02, 612, 25, 1, MB), #Max Candy

    #MB Beanspots 620-729
    "f_mount_01_b1": BlockData(0x007BB437, 0x01, 620, 1, 50, MB), #50 Coin
    "f_mount_01_b2": BlockData(0x007BB437, 0x02, 621, 32, 1, MB), #Bros. Bean
    "f_mount_01_b3": BlockData(0x007BB437, 0x04, 622, 1, 50, MB), #50 Coin
    "f_mount_01_b4": BlockData(0x007BB437, 0x08, 623, 34, 1, MB), #Defense Bean
    "f_mount_01_b5": BlockData(0x007BB437, 0x10, 624, 35, 1, MB), #Speed Bean
 
    "f_mount_02_b1": BlockData(0x007BB43A, 0x02, 625, 31, 1, MB), #Heart Bean
    "f_mount_02_b2": BlockData(0x007BB43A, 0x04, 626, 1, 50, MB), #50 Coin
    "f_mount_02_b3": BlockData(0x007BB43A, 0x08, 627, 33, 1, MB), #Power Bean
    "f_mount_02_b4": BlockData(0x007BB43A, 0x10, 628, 1, 50, MB), #50 Coin
    "f_mount_02_b5": BlockData(0x007BB43A, 0x20, 629, 35, 1, MB), #Speed Bean
    "f_mount_02_b6": BlockData(0x007BB43A, 0x40, 630, 36, 1, MB), #Stache Bean
    "f_mount_02_b7": BlockData(0x007BB43A, 0x80, 631, 31, 1, MB), #Heart Bean
    "f_mount_02_b8": BlockData(0x007BB43B, 0x01, 632, 32, 1, MB), #Bros. Bean
    "f_mount_02_b9": BlockData(0x007BB43B, 0x02, 633, 33, 1, MB), #Power Bean
    "f_mount_02_b10": BlockData(0x007BB43B, 0x04, 634, 34, 1, MB), #Defense Bean
    "f_mount_02_b11": BlockData(0x007BB43B, 0x08, 635, 1, 50, MB), #50 Coin
    "f_mount_02_b12": BlockData(0x007BB43B, 0x10, 636, 36, 1, MB), #Stache Bean
    "f_mount_02_b13": BlockData(0x007BB43B, 0x20, 637, 1, 50, MB), #50 Coin
    "f_mount_02_b14": BlockData(0x007BB43B, 0x40, 638, 32, 1, MB), #Bros. Bean
    "f_mount_02_b15": BlockData(0x007BB43B, 0x80, 639, 1, 50, MB), #50 Coin
    "f_mount_02_b16": BlockData(0x007BB43C, 0x01, 640, 35, 1, MB), #Speed Bean
    "f_mount_02_b17": BlockData(0x007BB46B, 0x04, 641, 34, 1, MB), #Defense Bean
 
    "f_mount_03_b1": BlockData(0x007BB43C, 0x20, 642, 1, 50, MB), #50 Coin
    "f_mount_03_b2": BlockData(0x007BB43C, 0x40, 643, 34, 1, MB), #Defense Bean
    "f_mount_03_b3": BlockData(0x007BB43D, 0x08, 644, 1, 50, MB), #50 Coin
    "f_mount_03_b4": BlockData(0x007BB43D, 0x10, 645, 32, 1, MB), #Bros. Bean
    "f_mount_03_b5": BlockData(0x007BB43E, 0x02, 646, 1, 50, MB), #50 Coin
    "f_mount_03_b6": BlockData(0x007BB43E, 0x04, 647, 33, 1, MB), #Power Bean
    "f_mount_03_b7": BlockData(0x007BB43E, 0x08, 648, 31, 1, MB), #Heart Bean
    "f_mount_03_b8": BlockData(0x007BB43E, 0x10, 649, 35, 1, MB), #Speed Bean
    "f_mount_03_b9": BlockData(0x007BB43E, 0x20, 650, 1, 50, MB), #50 Coin
    "f_mount_03_b10": BlockData(0x007BB43E, 0x40, 651, 1, 50, MB), #50 Coin
    "f_mount_03_b11": BlockData(0x007BB453, 0x40, 652, 1, 50, MB), #50 Coin
    "f_mount_03_b12": BlockData(0x007BB453, 0x80, 653, 36, 1, MB), #Stache Bean
    "f_mount_03_b13": BlockData(0x007BB454, 0x08, 654, 1, 50, MB), #50 Coin
    "f_mount_03_b14": BlockData(0x007BB454, 0x80, 655, 35, 1, MB), #Speed Bean
    "f_mount_03_b15": BlockData(0x007BB457, 0x20, 656, 36, 1, MB), #Stache Bean
    "f_mount_03_b16": BlockData(0x007BB47B, 0x10, 657, 33, 1, MB), #Power Bean
    "f_mount_03_b17": BlockData(0x007BB47B, 0x20, 658, 34, 1, MB), #Defense Bean
 
    "f_mount_04_b1": BlockData(0x007BB43E, 0x01, 659, 1, 50, MB), #50 Coin
    "f_mount_04_b2": BlockData(0x007BB43F, 0x10, 660, 36, 1, MB), #Stache Bean
    "f_mount_04_b3": BlockData(0x007BB441, 0x08, 661, 1, 50, MB), #50 Coin
    "f_mount_04_b4": BlockData(0x007BB443, 0x10, 662, 34, 1, MB), #Defense Bean
    "f_mount_04_b5": BlockData(0x007BB444, 0x40, 663, 35, 1, MB), #Speed Bean
    "f_mount_04_b6": BlockData(0x007BB457, 0x02, 664, 1, 50, MB), #50 Coin
 
    "f_mount_05_b1": BlockData(0x007BB440, 0x02, 665, 31, 1, MB), #Heart Bean
    "f_mount_05_b2": BlockData(0x007BB440, 0x04, 666, 1, 50, MB), #50 Coin
    "f_mount_05_b3": BlockData(0x007BB440, 0x08, 667, 33, 1, MB), #Power Bean
    "f_mount_05_b4": BlockData(0x007BB440, 0x10, 668, 1, 50, MB), #50 Coin
    "f_mount_05_b5": BlockData(0x007BB440, 0x20, 669, 35, 1, MB), #Speed Bean
    "f_mount_05_b6": BlockData(0x007BB440, 0x40, 670, 36, 1, MB), #Stache Bean
    "f_mount_05_b7": BlockData(0x007BB440, 0x80, 671, 31, 1, MB), #Heart Bean
    "f_mount_05_b8": BlockData(0x007BB446, 0x20, 672, 34, 1, MB), #Defense Bean
    "f_mount_05_b9": BlockData(0x007BB446, 0x40, 673, 35, 1, MB), #Speed Bean
    "f_mount_05_b10": BlockData(0x007BB46B, 0x10, 674, 32, 1, MB), #Bros. Bean
    "f_mount_05_b11": BlockData(0x007BB46B, 0x20, 675, 33, 1, MB), #Power Bean
 
    "f_mount_06_b1": BlockData(0x007BB441, 0x20, 676, 36, 1, MB), #Stache Bean
    "f_mount_06_b2": BlockData(0x007BB441, 0x40, 677, 32, 1, MB), #Bros. Bean
    "f_mount_06_b3": BlockData(0x007BB448, 0x20, 678, 31, 1, MB), #Heart Bean
    "f_mount_06_b4": BlockData(0x007BB47A, 0x80, 679, 1, 50, MB), #50 Coin
    "f_mount_06_b5": BlockData(0x007BB47B, 0x01, 680, 34, 1, MB), #Defense Bean
    "f_mount_06_b6": BlockData(0x007BB47B, 0x08, 681, 1, 50, MB), #50 Coin
 
    "f_mount_08_b1": BlockData(0x007BB456, 0x80, 682, 31, 1, MB), #Heart Bean
    "f_mount_08_b2": BlockData(0x007BB468, 0x40, 683, 1, 50, MB), #50 Coin
    "f_mount_08_b3": BlockData(0x007BB46C, 0x08, 684, 1, 50, MB), #50 Coin
 
    "f_mount_09_b1": BlockData(0x007BB443, 0x80, 685, 1, 50, MB), #50 Coin
    "f_mount_09_b2": BlockData(0x007BB444, 0x01, 686, 32, 1, MB), #Bros. Bean
    "f_mount_09_b3": BlockData(0x007BB444, 0x02, 687, 1, 50, MB), #50 Coin
    "f_mount_09_b4": BlockData(0x007BB444, 0x04, 688, 34, 1, MB), #Defense Bean
    "f_mount_09_b5": BlockData(0x007BB444, 0x08, 689, 1, 50, MB), #50 Coin
    "f_mount_09_b6": BlockData(0x007BB446, 0x80, 690, 32, 1, MB), #Bros. Bean
    "f_mount_09_b7": BlockData(0x007BB457, 0x04, 691, 36, 1, MB), #Stache Bean
    "f_mount_09_b8": BlockData(0x007BB45A, 0x04, 692, 1, 50, MB), #50 Coin
 
    "f_mount_11_b1": BlockData(0x007BB469, 0x40, 693, 1, 50, MB), #50 Coin
    "f_mount_11_b2": BlockData(0x007BB46C, 0x80, 694, 1, 50, MB), #50 Coin
    "f_mount_11_b3": BlockData(0x007BB478, 0x80, 695, 36, 1, MB), #Stache Bean
    "f_mount_11_b4": BlockData(0x007BB479, 0x01, 696, 31, 1, MB), #Heart Bean
    "f_mount_11_b5": BlockData(0x007BB479, 0x02, 697, 32, 1, MB), #Bros. Bean
    "f_mount_11_b6": BlockData(0x007BB479, 0x08, 698, 1, 50, MB), #50 Coin
    "f_mount_11_b7": BlockData(0x007BB479, 0x10, 699, 1, 100, MB), #100 Coin
    "f_mount_11_b8": BlockData(0x007BB479, 0x20, 700, 1, 50, MB), #50 Coin
    "f_mount_11_b9": BlockData(0x007BB479, 0x40, 701, 35, 1, MB), #Speed Bean
    "f_mount_11_b10": BlockData(0x007BB479, 0x80, 702, 33, 1, MB), #Power Bean
    "f_mount_11_b11": BlockData(0x007BB47A, 0x01, 703, 32, 1, MB), #Bros. Bean
    "f_mount_11_b12": BlockData(0x007BB47A, 0x02, 704, 31, 1, MB), #Heart Bean
    "f_mount_11_b13": BlockData(0x007BB47A, 0x04, 705, 1, 100, MB), #100 Coin
 
    "f_mount_12_b1": BlockData(0x007BB45C, 0x08, 706, 36, 1, MB), #Stache Bean
    "f_mount_12_b2": BlockData(0x007BB46D, 0x02, 707, 1, 100, MB), #100 Coin
 
    "f_mount_13_b1": BlockData(0x007BB44A, 0x80, 708, 1, 100, MB), #100 Coin
    "f_mount_13_b2": BlockData(0x007BB45D, 0x80, 709, 1, 50, MB), #50 Coin
    "f_mount_13_b3": BlockData(0x007BB45E, 0x01, 710, 32, 1, MB), #Bros. Bean
    "f_mount_13_b4": BlockData(0x007BB45E, 0x20, 711, 31, 1, MB), #Heart Bean
    "f_mount_13_b5": BlockData(0x007BB45E, 0x40, 712, 1, 50, MB), #50 Coin
    "f_mount_13_b6": BlockData(0x007BB45E, 0x80, 713, 33, 1, MB), #Power Bean
    "f_mount_13_b7": BlockData(0x007BB469, 0x20, 714, 1, 50, MB), #50 Coin
    "f_mount_13_b8": BlockData(0x007BB46A, 0x02, 715, 36, 1, MB), #Stache Bean
    "f_mount_13_b9": BlockData(0x007BB46D, 0x01, 716, 34, 1, MB), #Defense Bean
    "f_mount_13_b10": BlockData(0x007BB46D, 0x08, 717, 1, 50, MB), #50 Coin
    "f_mount_13_b11": BlockData(0x007BB46D, 0x10, 718, 35, 1, MB), #Speed Bean
 
    "f_mount_14_b1": BlockData(0x007BB45F, 0x01, 719, 1, 100, MB), #100 Coin
    "f_mount_14_b2": BlockData(0x007BB45F, 0x02, 720, 31, 1, MB), #Heart Bean
    "f_mount_14_b3": BlockData(0x007BB46D, 0x20, 721, 34, 1, MB), #Defense Bean
    "f_mount_14_b4": BlockData(0x007BB46D, 0x40, 722, 35, 1, MB), #Speed Bean
    "f_mount_14_b5": BlockData(0x007BB46D, 0x80, 723, 33, 1, MB), #Power Bean

    #NBC (Neo Bowser's Castle) 730-
    #NBC Blocks 730-769
    "f_koopa_neo_02_1": BlockData(0x007BB45F, 0x40, 730, 1, 100, NBC), #100 Coin
    "f_koopa_neo_02_2": BlockData(0x007BB45F, 0x80, 731, 21, 2, NBC), #Max Syrup Jar x2
    "f_koopa_neo_02_3": BlockData(0x007BB460, 0x01, 732, 1, 100, NBC), #100 Coin
    "f_koopa_neo_02_4": BlockData(0x007BB460, 0x02, 733, 1, 10, NBC), #10 Coin
    "f_koopa_neo_02_5": BlockData(0x007BB460, 0x04, 734, 1, 100, NBC), #100 Coin
    "f_koopa_neo_02_6": BlockData(0x007BB460, 0x08, 735, 1, 10, NBC), #10 Coin
 
    "f_koopa_neo_03_1": BlockData(0x007BB472, 0x80, 736, None, 1, NBC), #Gold Statue (Gear)
    "f_koopa_neo_03_2": BlockData(0x007BB473, 0x01, 737, 1, 100, NBC), #100 Coin
 
    "f_koopa_neo_04_1": BlockData(0x007BB470, 0x80, 738, 13, 2, NBC), #Max Mushroom x2
    "f_koopa_neo_04_2": BlockData(0x007BB471, 0x01, 739, 1, 100, NBC), #100 Coin
    "f_koopa_neo_04_3": BlockData(0x007BB473, 0x02, 740, 1, 10, NBC), #10 Coin
    "f_koopa_neo_04_4": BlockData(0x007BB473, 0x04, 741, 1, 100, NBC), #100 Coin
 
    "f_koopa_neo_05_1": BlockData(0x007BB460, 0x40, 742, 27, 2, NBC), #1-Up DX x2
    "f_koopa_neo_05_2": BlockData(0x007BB460, 0x80, 743, 1, 50, NBC), #50 Coin
    "f_koopa_neo_05_3": BlockData(0x007BB469, 0x80, 744, 25, 1, NBC), #Max Candy
    "f_koopa_neo_05_4": BlockData(0x007BB470, 0x08, 745, 1, 50, NBC), #50 Coin
    "f_koopa_neo_05_5": BlockData(0x007BB470, 0x10, 746, None, 1, NBC), #Angel Wear (Gear)
 
    "f_koopa_neo_06_1": BlockData(0x007BB470, 0x20, 747, 1, 100, NBC), #100 Coin
    "f_koopa_neo_06_2": BlockData(0x007BB470, 0x40, 748, None, 1, NBC), #Golden Wear (Gear)
    "f_koopa_neo_06_3": BlockData(0x007BB471, 0x80, 749, 1, 100, NBC), #100 Coin
    "f_koopa_neo_06_4": BlockData(0x007BB472, 0x01, 750, 1, 50, NBC), #50 Coin
 
    "f_koopa_neo_07_1": BlockData(0x007BB461, 0x08, 751, 1, 100, NBC), #100 Coin
    "f_koopa_neo_07_2": BlockData(0x007BB461, 0x10, 752, None, 1, NBC), #Gold Statue (Gear)
 
    "f_koopa_neo_08_1": BlockData(0x007BB461, 0x20, 753, 25, 1, NBC), #Max Candy
    "f_koopa_neo_08_2": BlockData(0x007BB461, 0x40, 754, 28, 2, NBC), #Double 1-Up Mushroom x2
    "f_koopa_neo_08_3": BlockData(0x007BB475, 0x10, 755, 27, 1, NBC), #1-Up DX
    "f_koopa_neo_08_4": BlockData(0x007BB475, 0x20, 756, 13, 1, NBC), #Max Mushroom
 
    "f_koopa_neo_12_1": BlockData(0x007BB461, 0x80, 757, 21, 2, NBC), #Max Syrup Jar x2
    "f_koopa_neo_12_2": BlockData(0x007BB462, 0x01, 758, None, 1, NBC), #Bundling Boots DX (Gear)
    "f_koopa_neo_12_3": BlockData(0x007BB472, 0x20, 759, 1, 50, NBC), #50 Coin
    "f_koopa_neo_12_4": BlockData(0x007BB472, 0x40, 760, 1, 100, NBC), #100 Coin
 
    "f_koopa_neo_13_1": BlockData(0x007BB449, 0x80, 761, 17, 2, NBC), #Max Nut x2
    "f_koopa_neo_13_2": BlockData(0x007BB462, 0x04, 762, None, 1, NBC), #Perfect Bro Gloves (Gear)
    "f_koopa_neo_13_3": BlockData(0x007BB474, 0x08, 763, 1, 10, NBC), #10 Coin
    "f_koopa_neo_13_4": BlockData(0x007BB474, 0x10, 764, 1, 100, NBC), #100 Coin

    #NBC Beanspots
    "f_koopa_neo_05_b1": BlockData(0x007BB460, 0x10, 770, 32, 1, NBC), #Bros. Bean
    "f_koopa_neo_05_b2": BlockData(0x007BB460, 0x20, 771, 36, 1, NBC), #Stache Bean
    "f_koopa_neo_05_b3": BlockData(0x007BB471, 0x02, 772, 33, 1, NBC), #Power Bean
    "f_koopa_neo_05_b4": BlockData(0x007BB471, 0x04, 773, 1, 100, NBC), #100 Coin
    "f_koopa_neo_05_b5": BlockData(0x007BB471, 0x08, 774, 35, 1, NBC), #Speed Bean
    "f_koopa_neo_05_b6": BlockData(0x007BB471, 0x10, 775, 36, 1, NBC), #Stache Bean
    "f_koopa_neo_05_b7": BlockData(0x007BB471, 0x20, 776, 31, 1, NBC), #Heart Bean

    "f_koopa_neo_07_b1": BlockData(0x007BB45E, 0x02, 777, 35, 1, NBC), #Speed Bean
    "f_koopa_neo_07_b2": BlockData(0x007BB461, 0x04, 778, 34, 1, NBC), #Defense Bean
    "f_koopa_neo_07_b3": BlockData(0x007BB472, 0x02, 779, 31, 1, NBC), #Heart Bean
    "f_koopa_neo_07_b4": BlockData(0x007BB472, 0x04, 780, 32, 1, NBC), #Bros. Bean
    "f_koopa_neo_07_b5": BlockData(0x007BB472, 0x08, 781, 33, 1, NBC), #Power Bean
    "f_koopa_neo_07_b6": BlockData(0x007BB472, 0x10, 782, 34, 1, NBC), #Defense Bean
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
