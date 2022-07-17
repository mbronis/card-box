from typing import Type


class CardsTypeMissmatch(Exception):
    """Exception raised when trying to impose multiple card types into single deck."""

    def __init__(self, card_type: Type) -> None:
        message = f"All cards shoud be of type '{ card_type.__name__}'"
        super().__init__(message)


class DrawFromEmptyDeck(Exception):
    """Exception raised when drawing from empty deck."""

    def __init__(self) -> None:
        message = f"Can not draw from an empty deck."
        super().__init__(message)
