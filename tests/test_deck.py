from collections import Counter

from uno.card import CardType, Color
from uno.deck import Deck


def test_number_of_total_cards():
    assert len(Deck()) == 108


def test_number_of_regular_cards():
    counts = Counter([c for c in Color])

    for card in Deck().get_cards():
        if card.card_type == CardType.REGULAR:
            counts[card.color] += 1

    total_count = 0
    for count in counts.items():
        assert count[1] == 19
        total_count += count[1]

    assert total_count == 76


def test_number_of_special_cards():
    deck = Deck()
    count = len([i for i in deck.get_cards() if i.card_type is not CardType.REGULAR])
    assert count == 32
