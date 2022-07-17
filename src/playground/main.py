import os
from dataclasses import dataclass
from typing import Set, Tuple

print(os.getcwd())

from src.model.card import Card
from src.model.deck import Deck


@dataclass(frozen=True)
class PlayCards(Card):
    suite: str
    int_attr: int
    arr_attr: Tuple


if __name__ == "__main__":

    card_a = TestCardsA(id=1, name="foo", arr=(1,))
    card_b = TestCardsA(id=2, name="bar", arr=(1,))
    card_c = TestCardsA(id=3, name="baz", arr=(1,))

    codex = Encyclopedia(TestCardsA)
    codex.add({card_a, card_b, card_c})

    deck = Deck(encyclopedia=codex, cards=[card_a, card_a, card_b, card_c])

    print(deck)

    codex_deck = Deck.from_encyclopedia(codex)
    print(codex_deck)
