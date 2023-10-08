from uuid import UUID, uuid4
from user import User
from text_message import TextMessage
from video_message import VideoMessage
from image_message import ImageMessage


class Chat:
    def __init__(self, name: str, creator_user: User) -> None:
        if not isinstance(name, str):
            raise TypeError(f"Expected str, got {type(name)}")
        if not isinstance(creator_user, User):
            raise TypeError(f"Expected User, got {type(creator_user)}")
        self.__name: str = name
        self.__creator_user: User = creator_user
        self.__id = uuid4()
        self.__users: list[User] = []

    @property
    def name(self) -> str:
        return self.__name
    
    @name.setter
    def name(self, name: str) -> None:
        if not isinstance(name, str):
            raise TypeError(f"Expected str, got {type(name)}")
        self.__name = name

    @property
    def creator_user(self) -> User:
        return self.__creator_user
    
    @property
    def id(self) -> UUID:
        return self.__id
    
    def add_user(self, user: User) -> None:
        if not isinstance(user, User):
            raise TypeError(f"Expected User, got {type(user)}")
        self.__users.append(user)
    
    def remove_user(self, user: User) -> None:
        if not isinstance(user, User):
            raise TypeError(f"Expected User, got {type(user)}")
        if user not in self.__users:
            raise Exception('User not found')
        self.__users.remove(user)

    # Maybe this should be in a message display
    def __create_message_prefix(self, user: User) -> str:
        if not isinstance(user, User):
            raise TypeError(f"Expected User, got {type(user)}")
        return f"{user.nickname}: "
    
    # idk if this is the best way to do this
    def send_text_message(self, user: User) -> None:
        if not isinstance(user, User):
            raise TypeError(f"Expected User, got {type(user)}")
        if user not in self.__users:
            raise Exception('User not found')
        content = ... # get message from display
        message = TextMessage(content)
        #print(self.__create_message_prefix(user) + message)
    
    def send_image_message(self, user: User) -> None:
        if not isinstance(user, User):
            raise TypeError(f"Expected User, got {type(user)}")
        if user not in self.__users:
            raise Exception('User not found')
        path = ...
        message = ImageMessage(path)
        #print(self.__create_message_prefix(user) + message)
    
    def send_video_message(self, user: User) -> None:
        if not isinstance(user, User):
            raise TypeError(f"Expected User, got {type(user)}")
        if user not in self.__users:
            raise Exception('User not found')
        path = ...
        message = VideoMessage(path)
        #print(self.__create_message_prefix(user) + message)
