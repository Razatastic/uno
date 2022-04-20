from enum import Enum


class CardType(Enum):
    REGULAR = "REGULAR"
    DRAW_TWO = "DRAW TWO"
    REVERSE = "REVERSE"
    SKIP = "SKIP"
    WILD = "WILD"
    WILD_DRAW_FOUR = "WILD DRAW FOUR"


class Color(Enum):
    RED = "RED"
    BLUE = "BLUE"
    GREEN = "GREEN"
    YELLOW = "YELLOW"


class Card:
    def __init__(self, card_type, color=None, value=None):
        self.card_type = card_type
        self.color = color
        self.value = value

    def __repr__(self):
        res = f"{self.card_type.value}"
        if self.color: res += f"::{self.color.value}"
        if self.value: res += f"::{self.value}"
        return "(" + res + ")"
