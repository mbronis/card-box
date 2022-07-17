import os
import pickle
from typing import Dict
from warnings import warn

from src.model.deck import Deck
from src.repo.abstract_repo import AbstractRepository


class PickleRepository(AbstractRepository):
    def __init__(self, dir: str = "./data") -> None:
        self.path = os.path.join(dir, "decks.pkl")
        self.decks = self._load_data()

    def _load_data(self) -> Dict[str, Deck]:
        try:
            with open(self.path, "rb") as f:
                decks = pickle.load(f)
        except FileNotFoundError:
            decks = {}

        return decks

    def _save_data(self):
        with open(self.path, "wb") as f:
            pickle.dump(self.decks, f)

    def add(self, deck: Deck):
        self.decks.update({deck.reference: deck})
        self._save_data()

    def get(self, reference: str) -> Deck:
        return self.decks[reference]
