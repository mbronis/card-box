from __future__ import annotations
from dataclasses import dataclass
from typing import Optional, Set, Tuple


@dataclass(frozen=True)
class Card:
    """Base class representing a card instance."""

    id: int

    def __hash__(self):
        return hash(self.id)

    def __eq__(self, other: Card) -> int:
        return self.id == other.id

    def __gt__(self, other: Card):
        return self.id > other.id

    def matches_all(self, **kwargs) -> bool:
        """Returns True if all arguments match with card's attributes."""
        for key, value in kwargs.items():
            attr = getattr(self, key, None)

            if attr is None or self._neg_match(attr, value):
                return False

        return True

    def _neg_match(self, attr, val) -> Optional[bool]:
        if isinstance(attr, Tuple):
            if set(attr) != set(val):
                return True
        elif isinstance(attr, str):
            if attr.lower() != val.lower():
                return True
        elif attr != val:
            return True
