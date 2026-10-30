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
    doopdoopdunes = Region("Doop Doop Dunes", world.player, world.multiworld)
    twinsytropics = Region("Twinsy Tropics", world.player, world.multiworld)
    gloomywoods = Region("Gloomy Woods", world.player, world.multiworld)
    mountbrrr = Region("Mount Brrr", world.player, world.multiworld)
    neocastle = Region("Neo Bowser's Castle", world.player, world.multiworld)

    regions = [
        peachcastle,
        sunbeamplains,
        doopdoopdunes,
        twinsytropics,
        gloomywoods,
        mountbrrr,
        neocastle,
    ]

    world.multiworld.regions += regions

def connect_regions(world: PJWorld) -> None:
    peachcastle = world.get_region("Peach's Castle")
    sunbeamplains = world.get_region("Sunbeam Plains")
    doopdoopdunes = world.get_region("Doop Doop Dunes")
    twinsytropics = world.get_region("Twinsy Tropics")
    gloomywoods = world.get_region("Gloomy Woods")
    mountbrrr = world.get_region("Mount Brrr")
    neocastle = world.get_region("Neo Bowser's Castle")

    peachcastle.connect(sunbeamplains, "Peach's Castle to Sunbeam Plains")
    sunbeamplains.connect(doopdoopdunes, "Sunbeam Plains to Doop Doop Dunes")
    sunbeamplains.connect(gloomywoods, "Sunbeam Plains to Gloomy Woods")
    doopdoopdunes.connect(sunbeamplains, "Doop Doop Dunes to Sunbeam Plains")
    doopdoopdunes.connect(twinsytropics, "Doop Doop Dunes to Twinsy Tropics")
    doopdoopdunes.connect(mountbrrr, "Doop Doop Dunes to Mount Brrr")
    twinsytropics.connect(doopdoopdunes, "Twinsy Tropics to Doop Doop Dunes")
    gloomywoods.connect(sunbeamplains, "Gloomy Woods to Sunbeam Plains")
    gloomywoods.connect(mountbrrr, "Gloomy Woods to Mount Brrr")
    mountbrrr.connect(doopdoopdunes, "Mount Brrr to Doop Doop Dunes")
    mountbrrr.connect(gloomywoods, "Mount Brrr to Gloomy Woods")
    mountbrrr.connect(neocastle, "Mount Brrr to Neo Bowser's Castle")
    neocastle.connect(mountbrrr, "Neo Bowser's Castle to Mount Brrr")

