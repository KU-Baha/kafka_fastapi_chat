from dataclasses import dataclass


@dataclass(eq=False)
class TextTooLongException(Exception):
    text: str

    @property
    def message(self):
        return f"Text too long: '{self.text[:255]}'"
