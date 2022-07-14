from typing import Type


class AddingWrongTypeCardToEncyclopediaError(Exception):
    def __init__(self, card_type: Type) -> None:
        message = f"All added cards shoud be of type '{ card_type.__name__}'"
        super().__init__(message)


class CreatingDeckWithBadCardTypes(Exception):
    def __init__(self, card_type: Type) -> None:
        message = f"All added cards shoud be of type '{ card_type.__name__}'"
        super().__init__(message)
