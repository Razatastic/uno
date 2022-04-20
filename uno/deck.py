from .card import Color, CardType, Card


class Deck:
    def __init__(self):
        self._cards = []
        self._init()

    def _init(self):
        for color in Color:
            self._add_cards(CardType.REGULAR, color, range(10), True)
            self._add_cards(CardType.REGULAR, color, range(1, 9), True)

            self._add_cards(CardType.SKIP, color, range(2))
            self._add_cards(CardType.REVERSE, color, range(2))
            self._add_cards(CardType.DRAW_TWO, color, range(2))

        self._add_cards(CardType.WILD, None, range(4))
        self._add_cards(CardType.WILD_DRAW_FOUR, None, range(4))

    def _add_cards(self, card_type, color, value_range, include_value=False):
        for i in value_range:
            self._cards.append(
                Card(card_type, color, i) if include_value else Card(card_type, color)
            )

    def get_cards(self):
        return self._cards

    def __len__(self):
        return len(self._cards)