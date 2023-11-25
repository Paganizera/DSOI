from .media_message import MediaMessage
from entities.user import User


class VideoMessage(MediaMessage):
    def __init__(self, path: str,filename :str,  user: User):
        if not isinstance(user, User):
            raise TypeError(f"Expected User, got {type(user)}")
        super().__init__(path,filename, user)
