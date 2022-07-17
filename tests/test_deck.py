import pytest
from src.model.deck import Deck
from src.model.exceptions import CardsTypeMissmatch

from tests.fixtures import get_test_cards


def test_creating_deck(get_test_cards):
    card_a1, card_a2, _ = get_test_cards

    deck = Deck(cards=[card_a1, card_a1, card_a2])

    assert card_a1 in deck
    assert len(deck) == 3


def test_creating_deck_with_missmatch_card_types_raises_error(get_test_cards):
    card_a1, _, card_b1 = get_test_cards

    with pytest.raises(CardsTypeMissmatch):
        _ = Deck(cards=[card_a1, card_b1])


def test_adding_cards_to_deck(get_test_cards):
    card_a1, card_a2, _ = get_test_cards

    deck = Deck(cards=[card_a1, card_a1])
    deck.add([card_a1, card_a2])

    assert card_a2 in deck
    assert len(deck) == 4


def test_adding_missmatch_type_card_raises_error(get_test_cards):
    card_a1, card_a2, card_b1 = get_test_cards

    deck = Deck(cards=[card_a1, card_a2])

    with pytest.raises(CardsTypeMissmatch):
        deck.add([card_b1])


def test_removing_cards_from_deck(get_test_cards):
    card_a1, card_a2, _ = get_test_cards

    deck = Deck(cards=[card_a1, card_a1, card_a2])
    deck.remove([card_a1, card_a2])

    assert card_a1 in deck
    assert card_a2 not in deck
    assert len(deck) == 1
