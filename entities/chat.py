from uuid import UUID, uuid4
from history.chat_history import ChatHistory
from errors.custom_errors import UserNotFoundError


class Chat:
    #   Constructor
    def __init__(self, name: str, creator_user_id: UUID) -> None:
        self.__check_name(name)
        self.__check_user_id(creator_user_id)
        self.__name: str = name
        self.__creator_user_id: UUID = creator_user_id
        self.__id: UUID = uuid4()
        self.__users: list[UUID] = []
        self.__chat_history = ChatHistory()

    # Getters and setters
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str) -> None:
        if not isinstance(name, str):
            raise TypeError(f"Expected str, got {type(name)}")
        self.__name = name

    @property
    def creator_user_id(self) -> UUID:
        return self.__creator_user_id

    @property
    def id(self) -> UUID:
        return self.__id

    @property
    def users(self) -> list[UUID]:
        return self.__users

    @property
    def chat_history(self) -> ChatHistory:
        return self.__chat_history

    #   Private function to avaliate wheter
    #   the chat name is valid or not
    def __check_name(self, name: str):
        if not isinstance(name, str):
            raise TypeError("Name must be a string")
        if len(name) < 3:
            raise ValueError("Name must be at least 3 characters long")

    #   Avaliates wheter the current user is valid or not
    def __check_user_id(self, user_id: UUID):
        if not isinstance(user_id, UUID):
            raise TypeError("User ID must be a UUID object")

    #   Checks wheter there's duplicated instances
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Chat):
            return False
        return self.__id == other.id and self.__name == other.name

    #   Checks if the chat contains an especific user
    def user_in_chat(self, user_id: UUID) -> bool:
        self.__check_user_id(user_id)
        for _id in self.__users:
            if _id == user_id:
                return True
        return False

    #   Change the nickname of the creator user
    #   or the "ADMININSTRATOR" one
    def change_creator_user_id(self) -> None:
        for _id in self.__users:
            if _id != self.__creator_user_id:
                self.__creator_user_id = _id
                return

    #   Add a new user to the chat
    def add_user(self, user_id: UUID) -> None:
        self.__check_user_id(user_id)
        self.__users.append(user_id)

    #   Remove an user to the chat
    def remove_user(self, user_id: UUID) -> None:
        self.__check_user_id(user_id)
        #   Checks wheter there's the user or not
        if user_id not in self.__users:
            raise UserNotFoundError()
        self.__users.remove(user_id)
