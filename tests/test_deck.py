import pytest
import src.model.exceptions as model_exceptions
from src.model.deck import Deck

from tests.fixtures import get_test_cards, get_test_deck


def test_creating_deck(get_test_cards, get_test_deck):
    card_a1, *_ = get_test_cards
    deck = get_test_deck

    assert card_a1 in deck
    assert len(deck) == 3


def test_creating_deck_with_missmatch_card_types_raises_error(get_test_cards):
    card_a1, _, card_b1 = get_test_cards

    with pytest.raises(model_exceptions.CardsTypeMissmatch):
        _ = Deck(cards_type=type(card_a1), cards=[card_a1, card_b1])


def test_adding_cards_to_deck(get_test_cards, get_test_deck):
    card_a1, card_a2, _ = get_test_cards
    deck = get_test_deck

    deck.add([card_a1, card_a2])

    assert len(deck) == 5


def test_adding_missmatch_type_card_raises_error(get_test_cards, get_test_deck):
    *_, card_b1 = get_test_cards
    deck = get_test_deck

    with pytest.raises(model_exceptions.CardsTypeMissmatch):
        deck.add([card_b1])


def test_removing_cards_from_deck(get_test_cards, get_test_deck):
    card_a1, card_a2, _ = get_test_cards
    deck = get_test_deck

    deck.remove([card_a1, card_a2])

    assert card_a1 in deck
    assert card_a2 not in deck
    assert len(deck) == 1


def test_deck_filter(get_test_deck):
    deck = get_test_deck

    deck_filtered = deck.filter(name="foo")

    assert len(deck) == 3
    assert len(deck_filtered) == 2


def test_deck_filter_excluded_all(get_test_deck):
    deck = get_test_deck
    deck_filtered = deck.filter(name="baz")

    assert len(deck) == 3
    assert len(deck_filtered) == 0


def test_deck_filter_with_empty_argument(get_test_deck):
    deck = get_test_deck
    deck_filtered = deck.filter(name="")

    assert len(deck) == 3
    assert len(deck_filtered) == 0


def test_deck_filter_with_not_existing_argument(get_test_deck):
    deck = get_test_deck
    deck_filtered = deck.filter(bad_argument_name="foo")

    assert len(deck) == 3
    assert len(deck_filtered) == 0


def test_deck_shuffle(get_test_deck):
    deck = get_test_deck
    deck_cards = [card for card in deck.cards]

    deck.shuffle()

    assert sorted(deck.cards) == sorted(deck_cards)


def test_deck_draw(get_test_cards, get_test_deck):
    _, card, _ = get_test_cards
    deck = get_test_deck
    card_drawn = deck.draw()

    assert len(deck) == 2
    assert card_drawn == card


def test_deck_draw_from_empty_deck_raises_error(get_test_deck):
    deck = get_test_deck
    for _ in range(len(deck)):
        _ = deck.draw()

    with pytest.raises(model_exceptions.DrawFromEmptyDeck):
        _ = deck.draw()
