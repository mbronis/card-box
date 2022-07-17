from typing import Type


class CardsTypeMissmatch(Exception):
    def __init__(self, card_type: Type) -> None:
        message = f"All cards shoud be of type '{ card_type.__name__}'"
        super().__init__(message)
