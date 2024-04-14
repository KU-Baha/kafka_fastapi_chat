from dataclasses import dataclass

from domain.events.base import BaseEvent


@dataclass(kw_only=True)
class NewMessageReceivedEvent(BaseEvent):
    chat_oid: str
    message_oid: str
    message_text: str


