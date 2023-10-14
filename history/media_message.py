from .base_message import BaseMessage
from entities.user import User

class MediaMessage(BaseMessage):
    def __init__(self, path: str, user: User):
        super().__init__(user)
        self.__path = path
    
    @property
    def path(self) -> str:
        return self.__path
