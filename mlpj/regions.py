from __future__ import annotations
from typing import TYPE_CHECKING

from BaseClasses import Entrance, Region

if TYPE_CHECKING:
    from .world import PJWorld

def create_and_connect_regions(world: PJWorld) -> None:
    create_all_regions(world)
    connect_regions(world)

def create_all_regions(world: PJWorld) -> None:
    peachcastle = Region("Peach's Castle", world.player, world.multiworld)
    sunbeamplains = Region("Sunbeam Plains", world.player, world.multiworld)

    regions = [
        peachcastle,
        sunbeamplains,
    ]

    world.multiworld.regions += regions

def connect_regions(world: PJWorld) -> None:
    peachcastle = world.get_region("Peach's Castle")
    sunbeamplains = world.get_region("Sunbeam Plains")

    peachcastle.connect(sunbeamplains, "Peach's Castle to Sunbeam Plains")
    
