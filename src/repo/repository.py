from abc import ABC, abstractmethod

from src.model.deck import Deck


class AbstractRepository(ABC):
    @abstractmethod
    def add(self, deck: Deck):
        raise NotImplementedError

    @abstractmethod
    def add(self, reference: str) -> Deck:
        raise NotImplementedError
