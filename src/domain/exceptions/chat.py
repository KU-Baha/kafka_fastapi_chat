from dataclasses import dataclass


@dataclass(eq=False)
class TitleTooLongException(Exception):
    text: str

    @property
    def message(self):
        return f"Text too long: '{self.text[:255]}'"


@dataclass(eq=False)
class EmptyValueException(Exception):
    @property
    def message(self):
        return "Empty value"
