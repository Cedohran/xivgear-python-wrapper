from typing import List
from enum import Enum


class XIVGearSlot(str, Enum):
    WEAPON = "Weapon"
    HEAD = "Head"
    BODY = "Body"
    HAND = "Hand"
    LEGS = "Legs"
    Feet = "Feet"
    EARS = "Ears"
    NECK = "Neck"
    WRIST = "Wrist"
    RING_RIGHT = "RingRight"
    RING_LEFT = "RingLeft"


class GearTier(str, Enum):
    UNKNOWN = "UNKNOWN"
    OTHER = "OTHER"
    CRAFTED = "CRAFTED"
    TOME = "TOME"
    TOME_UPGRADED = "TOME_UPGRADED"
    EX_TRIAL = "EX_TRIAL"
    NORMAL_RAID = "NORMAL_RAID"
    SAVAGE = "SAVAGE"
    RELIC = "RELIC"


class XIVGearItem():
    def __init__(self, id: int,
                 gear_slot: XIVGearSlot,
                 materia: List[int]):
        self.id = id
        self.gear_slot = gear_slot
        self.materia = materia

