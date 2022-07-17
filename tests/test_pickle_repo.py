import os
import pickle
from dataclasses import dataclass
from typing import Tuple

from src.model import Card, Deck
from src.repo import PickleRepository


# using fixtures raises
# AttributeError: Can't pickle local object 'test_pickle_repo_can_add_deck.<locals>.TestCardsA'
@dataclass(frozen=True)
class CardsA(Card):
    name: str
    hp: int
    powers: Tuple


card_a1 = CardsA(name="foo", hp=1, powers=("foo",))
card_a2 = CardsA(name="bar", hp=2, powers=("foo", "bar"))


def test_pickle_repo_can_add_deck(tmp_path):
    deck_name = "deck1"
    deck = Deck(ref=deck_name, cards_type=CardsA, cards=[card_a1, card_a2])

    repo = PickleRepository(tmp_path)
    repo.add(deck)

    with open(os.path.join(tmp_path, "decks.pkl"), "rb") as f:
        loaded_repo = pickle.load(f)

        assert deck_name in loaded_repo
        assert [card_a1, card_a2] == loaded_repo[deck_name].cards


def test_pickle_repo_can_retrive_deck_with_cards(tmp_path):
    deck1_name = "deck1"
    deck1 = Deck(ref=deck1_name, cards_type=CardsA, cards=[card_a2, card_a2])

    deck2_name = "deck2"
    deck2 = Deck(ref=deck2_name, cards_type=CardsA, cards=[card_a2])

    with open(os.path.join(tmp_path, "decks.pkl"), "wb") as f:
        pickle.dump(
            {
                deck1.reference: deck1,
                deck2.reference: deck2,
            },
            f,
        )

    repo = PickleRepository(tmp_path)
    retrived_deck = repo.get(deck1_name)

    assert retrived_deck == deck1
    assert retrived_deck.cards_type == deck1.cards_type
    assert retrived_deck.cards == deck1.cards
