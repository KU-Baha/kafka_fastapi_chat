from dataclasses import dataclass, field

from domain.entities.base import BaseEntity
from domain.events.chat import NewMessageReceivedEvent
from domain.values.chat import Text, Title


@dataclass(eq=True, kw_only=True)
class Message(BaseEntity):
    text: Text


@dataclass(eq=True, unsafe_hash=True, kw_only=True)
class Chat(BaseEntity):
    title: Title
    messages: list[Message] = field(
        default_factory=list
    )

    def add_message(self, message: Message):
        self.messages.append(message)
        self.register_event(NewMessageReceivedEvent(
            chat_oid=self.oid,
            message_oid=message.oid,
            message_text=message.text.as_generic_type()
        ))
