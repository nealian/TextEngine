__author__ = 'DragonAxe'

from entity import Entity
from enum import Enum

class Item(Entity):
    def __init__(self, description, verbose_description):
        this.type = Item_types.Rock
        super().__init__(description, verbose_description)

class Item_types(Enum):
    Desk = 1
    Stapler = 2
    Paper = 3
    Rock = 4
    Scissors = 5
    Mouse pad = 6
    Bag = 7
    Backpack = 8
