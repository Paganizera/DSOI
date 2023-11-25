from uuid import UUID, uuid4
import hashlib

class User:
    #   Constructor
    def __init__(self, nickname: str, password: str) -> None:
        self.check_nickname(nickname)
        self.check_password(password)
        self.__nickname = nickname
        self.__password = User.hash256(password)
        self.__id = uuid4()

    #   Getters and Setters
    @property
    def nickname(self) -> str:
        return self.__nickname

    @nickname.setter
    def nickname(self, nickname: str) -> None:
        self.check_nickname(nickname)
        self.__nickname = nickname

    @property
    def password(self) -> int:
        return self.__password

    @password.setter
    def password(self, password: str) -> None:
        self.check_password(password)
        self.__password = User.hash256(password)

    @property
    def id(self) -> UUID:
        return self.__id

    @staticmethod
    def hash256(pw: str) -> str:
        return hashlib.sha256(pw.encode()).hexdigest()

    #   Avaliates duplicated users
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, User):
            return False
        return self.__id == other.id or self.__nickname == other.nickname

    #   Avaliates if the username is a valid one
    def check_nickname(self, nickname: str) -> None:
        if not isinstance(nickname, str):
            raise TypeError("Nickname must be a string")
        if len(nickname) < 3:
            raise ValueError("Nickname must be at least 3 characters long")

    #   Avaliates if the conditions for the password are met
    def check_password(self, password: str) -> None:
        if not isinstance(password, str):
            raise TypeError("Password must be a string")
        if len(password) < 6:
            raise ValueError("Password must be at least 6 characters long")
