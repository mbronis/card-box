from __future__ import annotations

from dataclasses import dataclass
from typing import Optional, Tuple


@dataclass(frozen=True)
class Card:
    """Base class representing a card instance."""

    def matches_all(self, **kwargs) -> bool:
        """Returns True if all arguments match with card's attributes.

        For str attributes comparison is case insensitive but must match exactly.

        For tuple attributes order does not matter and all elements must match exactly.

        Numerical attributes has to match exactly.

        Returns False if argument or attribute is empty list or str ('').
        Search with None is not supported.
        """
        for key, value in kwargs.items():
            attr = getattr(self, key, None)

            if not (attr and value):
                return False
            if self._neg_match(attr, value):
                return False

        return True

    def matches_any(self, **kwargs) -> bool:
        """Returns True if any of arguments match with card's attribute.

        For str attributes comparison is case insensitive and is enough if argument is a substring of the attribute.

        For tuple attributes order does not matter and one elements must match exactly.

        For numerical attributes it is enough that argument is equal or greater than card's attribute.

        Search for/with empty list or str ('') does not return a match.
        Search with None is not supported.
        """
        for key, value in kwargs.items():
            attr = getattr(self, key, None)

            if attr and value:
                if self._match(attr, value):
                    return True

        return False

    def _neg_match(self, attr, val) -> Optional[bool]:
        if isinstance(attr, Tuple):
            if set(attr) != set(val):
                return True
        elif isinstance(attr, str):
            if attr.lower() != val.lower():
                return True
        elif attr != val:
            return True

    def _match(self, attr, val) -> Optional[bool]:
        if isinstance(attr, Tuple):
            if any(v in attr for v in val):
                return True
        elif isinstance(attr, str):
            if val.lower() in attr.lower():
                return True
        elif isinstance(attr, int):
            if val >= attr:
                return True
        elif attr == val:
            return True

    # def __hash__(self):
    #     return hash(self.id)

    # def __eq__(self, other: Card) -> int:
    #     return self.id == other.id

    def __gt__(self, other: Card):
        # return self.id > other.id
        return str(self) > str(other)
