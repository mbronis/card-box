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
    deck_name = "test_deck"
    deck = Deck(ref=deck_name, cards_type=CardsA, cards=[card_a1, card_a2])

    repo = PickleRepository(tmp_path)
    repo.add(deck)

    with open(os.path.join(tmp_path, "decks.pkl"), "rb") as f:
        loaded_repo = pickle.load(f)

        assert deck_name in loaded_repo
