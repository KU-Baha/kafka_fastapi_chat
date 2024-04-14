from dataclasses import dataclass

from domain.exceptions.chat import TitleTooLongException, EmptyValueException
from domain.values.base import BaseValueObject


@dataclass(frozen=True)
class Text(BaseValueObject):
    value: str

    def validate(self):
        if not self.value:
            raise EmptyValueException()

    def as_generic_type(self) -> str:
        return str(self.value)


@dataclass(frozen=True)
class Title(BaseValueObject):
    value: str

    def validate(self):
        if not self.value:
            raise EmptyValueException()

        if len(self.value) > 255:
            raise TitleTooLongException(self.value)

    def as_generic_type(self):
        return str(self.value)
