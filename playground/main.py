import os
from dataclasses import dataclass
from enum import Enum, auto

print(os.getcwd())

from src.model import Card, Deck
from src.repo import PickleRepository


class Suits(Enum):
    Clubs = auto()
    Diamonds = auto()
    Hearts = auto()
    Spades = auto()


@dataclass(frozen=True)
class PlayCards(Card):
    suite: Suits
    rank: int


if __name__ == "__main__":

    ace_of_spades = PlayCards(suite=Suits.Spades, rank=14)
    queen_of_hearts = PlayCards(suite=Suits.Hearts, rank=12)

    deck = Deck(
        ref="cards",
        cards_type=PlayCards,
        cards=[
            ace_of_spades,
            queen_of_hearts,
        ],
    )

    print("-------------> deck")
    print(deck)
    print(deck.__class__.__name__)
    print(deck.__dict__)
    print(str(deck))
    print("-------------> card")
    print(queen_of_hearts)
    print(queen_of_hearts.__dict__)
    print(queen_of_hearts.__class__.__name__)
    print(str(queen_of_hearts))
    # print(asdict(queen_of_hearts))

    print("-------------> repo")
    repo = PickleRepository()
    repo.add(deck)

    print(repo.decks.keys())
