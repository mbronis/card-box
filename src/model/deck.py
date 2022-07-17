from __future__ import annotations

import random
from collections import Counter
from typing import List, Type

import src.model.exceptions as model_exceptions
from src.model.card import Card


class Deck:
    """Class representing a deck build from cards of the same type."""

    def __init__(self, cards_type: Type, cards: List[Card]) -> None:
        self.cards_type = cards_type
        self._validate_cards(cards)
        self.cards = cards

    def _validate_cards(self, cards: List[Card]) -> None:
        if not all(isinstance(card, self.cards_type) for card in cards):
            raise model_exceptions.CardsTypeMissmatch(self.cards_type)

    def add(self, cards: List[Card]) -> None:
        self._validate_cards(cards)
        self.cards.extend(cards)

    def remove(self, cards: List[Card]) -> None:
        for card in cards:
            self.cards.remove(card)

    def filter(self, **kwargs) -> Deck:
        """Returns a new deck created with cards that matche all passed arguemtns."""
        filtered_cards = [card for card in self.cards if card.matches_all(**kwargs)]

        return Deck(cards_type=self.cards_type, cards=filtered_cards)

    def shuffle(self) -> None:
        random.shuffle(self.cards)

    def draw(self) -> None:
        try:
            return self.cards.pop()
        except IndexError:
            raise model_exceptions.DrawFromEmptyDeck()

    # def __str__(self):
    #     text = f"A deck of {self.cards_type.__name__}:"
    #     cards_count = Counter(self.cards)
    #     for card, count in cards_count.items():
    #         text += f"\n\t{card.name}: {count}"

    #     return text

    def __contains__(self, card: Card) -> bool:
        return card in self.cards

    def __len__(self) -> int:
        return len(self.cards)
