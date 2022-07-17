from abc import ABC, abstractmethod

from src.model import Deck


class AbstractRepository(ABC):
    @abstractmethod
    def add(self, deck: Deck):
        raise NotImplementedError

    @abstractmethod
    def get(self, reference: str) -> Deck:
        raise NotImplementedError
