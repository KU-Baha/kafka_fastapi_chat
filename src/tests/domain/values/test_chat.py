from datetime import datetime

import pytest
from faker import Faker

from domain.entities.chat import Message, Chat
from domain.exceptions.chat import TitleTooLongException, EmptyValueException
from domain.values.chat import Text, Title

faker = Faker()


def test_create_message():
    text = Text(faker.text())
    message = Message(text=text)

    assert message.text == text
    assert message.created_at.date() == datetime.today().date()


def test_create_message_text_empty():
    with pytest.raises(EmptyValueException):
        text = Text("")
        Message(text=text)


def test_create_chat():
    title = Title(faker.text())
    chat = Chat(title=title)

    assert chat.title == title
    assert chat.messages == []
    assert chat.created_at.date() == datetime.today().date()


def test_create_chat_title_empty():
    with pytest.raises(EmptyValueException):
        title = Title("")
        Chat(title=title, messages=[])


def test_create_chat_title_too_long():
    with pytest.raises(TitleTooLongException):
        title = Title("a" * 256)
        Chat(title=title, messages=[])


def test_add_chat_message():
    text = Text(faker.text())
    message = Message(text=text)

    title = Title(faker.text())
    chat = Chat(title=title, messages=[])

    chat.add_message(message)

    assert message in chat.messages
