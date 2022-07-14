from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from typing import List, Set, Type

import src.model.exceptions as model_exceptions


@dataclass(frozen=True)
class Card:
    """Base class representing a card instance"""

    name: str


class Encyclopedia:
    """Class representing collection of all cards of the same type"""

    def __init__(self, card_type: Type) -> None:
        self.card_type = card_type
        self.cards: Set[Card] = set()

    def __contains__(self, card: Card) -> bool:
        return card in self.cards

    def __len__(self) -> int:
        return len(self.cards)

    def _validate_cards(self, cards: Set[Card]) -> None:
        if not all(isinstance(card, self.card_type) for card in cards):
            raise model_exceptions.AddingWrongTypeCardToEncyclopediaError(self.card_type)

    def add(self, cards: Set[Card]) -> None:
        self._validate_cards(cards)
        self.cards = self.cards.union(cards)

    def remove(self, cards: Set[Card]) -> None:
        self.cards = self.cards.difference(cards)


class Deck:
    """Class representing deck build from cards of the same type"""

    def __init__(self, encyclopedia: Encyclopedia, cards: List[Card]) -> None:
        if not all(isinstance(card, encyclopedia.card_type) for card in cards):
            raise model_exceptions.CreatingDeckWithBadCardTypes(encyclopedia.card_type)
        self.card_type: Type = encyclopedia.card_type
        self.cards = cards

    @classmethod
    def from_encyclopedia(cls, encyclopedia: Encyclopedia) -> Deck:
        return Deck(encyclopedia=encyclopedia, cards=encyclopedia.cards)

    def __str__(self):
        text = f"A deck of {self.card_type.__name__}:"
        cards_count = Counter(self.cards)
        for card, count in cards_count.items():
            text += f"\n\t{card.name}: {count}"

        return text

    def __contains__(self, card: Card) -> bool:
        return card in self.cards

    def __len__(self) -> int:
        return len(self.cards)


if __name__ == "__main__":

    @dataclass(frozen=True)
    class TestCardsA(Card):
        name: str

    card_a = TestCardsA(name="foo")
    card_b = TestCardsA(name="bar")
    card_c = TestCardsA(name="baz")

    codex = Encyclopedia(TestCardsA)
    codex.add({card_a, card_b, card_c})

    deck = Deck(encyclopedia=codex, cards=[card_a, card_a, card_b, card_c])

    print(deck)

    codex_deck = Deck.from_encyclopedia(codex)
    print(codex_deck)
