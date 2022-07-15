import pytest
from src.model.collections import Deck, Encyclopedia
from src.model.exceptions import AddingWrongTypeCardToEncyclopediaError

from tests.fixtures import get_test_cards


def test_creating_encyclopedia_fails_on_wrong_card_type(get_test_cards):
    card_type_a, _, card_type_b = get_test_cards

    encyclopedia = Encyclopedia(card_type=card_type_a.__class__)

    with pytest.raises(AddingWrongTypeCardToEncyclopediaError):
        encyclopedia.add({card_type_b})


def test_adding_cards_to_encyclopedia(get_test_cards):
    card_type_a1, card_type_a2, _ = get_test_cards

    encyclopedia = Encyclopedia(card_type=card_type_a1.__class__)
    encyclopedia.add({card_type_a1, card_type_a2})

    assert card_type_a1 in encyclopedia
    assert card_type_a2 in encyclopedia
    assert len(encyclopedia) == 2


def test_encyclopedia_has_always_single_card_instance(get_test_cards):
    card_type_a1, *_ = get_test_cards

    encyclopedia = Encyclopedia(card_type=card_type_a1.__class__)
    encyclopedia.add({card_type_a1, card_type_a1})

    assert len(encyclopedia) == 1


def test_removing_cards_from_encyclopedia(get_test_cards):
    card_type_a1, card_type_a2, _ = get_test_cards

    encyclopedia = Encyclopedia(card_type=card_type_a1.__class__)
    encyclopedia.add({card_type_a1})

    encyclopedia.remove({card_type_a2})
    assert card_type_a1 in encyclopedia
    assert len(encyclopedia) == 1

    encyclopedia.remove({card_type_a1})
    assert card_type_a1 not in encyclopedia
    assert len(encyclopedia) == 0


def test_creating_deck(get_test_cards):
    card_a1, card_a2, _ = get_test_cards

    encyclopedia = Encyclopedia(card_type=card_a1.__class__)
    encyclopedia.add({card_a1, card_a2})

    deck = Deck(encyclopedia=encyclopedia, cards=[card_a1, card_a1, card_a2])

    assert len(deck) == 3


def test_creating_deck_from_encyclopedia(get_test_cards):
    card_a1, card_a2, _ = get_test_cards

    encyclopedia = Encyclopedia(card_type=card_a1.__class__)
    encyclopedia.add({card_a1, card_a2})

    deck = Deck.from_encyclopedia(encyclopedia=encyclopedia)

    assert len(deck) == 2
