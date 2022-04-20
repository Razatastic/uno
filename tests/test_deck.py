from collections import Counter

from uno.card import CardType, Color
from uno.deck import Deck


def test_number_of_total_cards():
    assert len(Deck()) == 108


def test_number_of_regular_cards():
    card_count_by_color = Counter([c for c in Color])

    for card in Deck().get_cards():
        if card.card_type == CardType.REGULAR:
            card_count_by_color[card.color] += 1

    total_count = 0
    for count in card_count_by_color.items():
        color_count = count[1] - 1  # Need to subtract 1 because Counter initializes at 1 instead of 0
        assert color_count == 19
        total_count += color_count

    assert total_count == 76


def test_number_of_special_cards():
    deck = Deck()
    count = len([i for i in deck.get_cards() if i.card_type is not CardType.REGULAR])
    assert count == 32
