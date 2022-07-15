"""A module defining Pokemon cards"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Tuple

from model.collections import Card


class PokemonType(Enum):
    WATER = 1
    FIRE = 2
    ELECTRIC = 3
    GRASS = 4


@dataclass(frozen=True)
class PokemonCard(Card):
    name: str
    type: Tuple[PokemonType]
    weakness: Tuple[PokemonType]
    hp: int
    evolve_from: PokemonCard = None

    # def __eq__(self, other: PokemonCard):
    #     return self.name == other.name

    # def __hash__(self):
    #     return hash(self.name)
