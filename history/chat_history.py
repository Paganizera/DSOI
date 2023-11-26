from history.base_message import BaseMessage
from .text_message import TextMessage
from .image_message import ImageMessage
from entities.user import User


class ChatHistory:
    def __init__(self):
        self.__messages: list[BaseMessage] = []

    @property
    def messages(self) -> list[BaseMessage]:
        return self.__messages

    @messages.setter
    def messages(self, messages: list[BaseMessage]) -> None:
        self.__messages = messages

    def add_text_message(self, content: str, user: User) -> bool:
        if isinstance(content, str) and isinstance(user, User):
            msg = TextMessage(content, user)
            self.__messages.append(msg)
            return True
        return False

    def add_image_message(self, path: str, filename: str, user: User) -> bool:
        if isinstance(path, str) and isinstance(user, User):
            msg = ImageMessage(path, filename, user)
            self.__messages.append(msg)
            return True
        return False
