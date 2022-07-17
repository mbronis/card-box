from __future__ import annotations

from collections import Counter
from typing import List, Set, Type

import src.model.exceptions as model_exceptions
from src.model.card import Card


class Deck:
    """Class representing a deck build from cards of the same type."""

    def __init__(self, cards: List[Card]) -> None:
        self.card_type: Type = type(cards[0])
        self._validate_cards(cards)
        self.cards = cards

    def _validate_cards(self, cards: List[Card]) -> None:
        if not all(isinstance(card, self.card_type) for card in cards):
            raise model_exceptions.CardsTypeMissmatch(self.card_type)

    def add(self, cards: List[Card]) -> None:
        self._validate_cards(cards)
        self.cards.extend(cards)

    def remove(self, cards: List[Card]) -> None:
        for card in cards:
            self.cards.remove(card)

    # def filter(self, **kwargs) -> Deck:
    #     """Creates a new deck by filtering cards with passed arguemnts."""
    #     pass

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
