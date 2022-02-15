from enum import Enum


class Position(str, Enum):
    TOP = "TOP"
    MIDDLE = "MID"
    JUNGLE = "JG"
    BOTTOM = "BOT"
    SUPPORT = "SUP"


class Tier(str, Enum):
    UNRANKED = "UNRANKED"
    IRON = "IRON"
    BRONZE = "BRONZE"
    SILVER = "SILVER"
    GOLD = "GOLD"
    PLATINUM = "PLATINUM"
    DIAMOND = "DIAMOND"
    MASTER = "MASTER"
    GRANDMASTER = "GRANDMASTER"
    CHALLENGER = "CHALLENGER"
