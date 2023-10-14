from .base_message import BaseMessage
from entities.user import User


class TextMessage(BaseMessage):
    def __init__(self, text: str, user: User):
        if not isinstance(user, User):
            raise TypeError(f"Expected User, got {type(user)}")
        super().__init__(user)
        self.__text = text

    @property
    def text(self) -> str:
        return self.__text
