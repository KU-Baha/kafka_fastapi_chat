from dataclasses import dataclass, field

from domain.entities.base import BaseEntity
from domain.values.chat import Text, Title


@dataclass(eq=True, unsafe_hash=True)
class Message(BaseEntity):
    text: Text


@dataclass(eq=True, unsafe_hash=True)
class Chat(BaseEntity):
    title: Title
    messages: list[Message] = field(
        default_factory=list,
        kw_only=True
    )

    def add_message(self, message: Message):
        self.messages.append(message)
