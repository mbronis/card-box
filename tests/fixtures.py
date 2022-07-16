from dataclasses import dataclass
from typing import Tuple

import pytest
from src.model.card import Card


@pytest.fixture(scope="session")
def get_test_cards():
    @dataclass(frozen=True)
    class TestCardsA(Card):
        name: str
        hp: int
        powers: Tuple

    @dataclass(frozen=True)
    class TestCardsB(Card):
        name: str
        hp: int
        powers: Tuple

    card_type_a1 = TestCardsA(id=1, name="foo", hp=1, powers=("foo",))
    card_type_a2 = TestCardsA(id=2, name="bar", hp=2, powers=("foo", "bar"))
    card_type_b = TestCardsB(id=3, name="baz", hp=3, powers=tuple())

    return card_type_a1, card_type_a2, card_type_b
