from typing import List
from data_structures.xiv_gear_item import XIVGearItem


class XIVGearSet():
    def __init__(self, name: str,
                 description: str,
                 items: List[XIVGearItem],
                 food: int):
        self.name = name
        self.description = description
        self.items = items
        self.food = food

