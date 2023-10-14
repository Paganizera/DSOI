from uuid import UUID, uuid4


class User:
    def __init__(self, nickname: str, password: str) -> None:
        self.__check_nickname(nickname)
        self.__check_password(password)
        self.__nickname = nickname
        self.__password = hash(password)
        self.__id = uuid4()

    @property
    def nickname(self) -> str:
        return self.__nickname

    @nickname.setter
    def nickname(self, nickname: str) -> None:
        self.__check_nickname(nickname)
        self.__nickname = nickname
    
    @property
    def password(self) -> str:
        return self.__password

    @password.setter
    def password(self, password: str) -> None:
        self.__check_password(password)
        self.__password = password
    
    @property
    def id(self) -> UUID:
        return self.__id

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, User):
            return False
        return self.__id == other.id or self.__nickname == other.nickname

    def __check_nickname(self, nickname: str) -> None:
        if not isinstance(nickname, str):
            raise TypeError('Nickname must be a string')
        if len(nickname) < 3:
            raise ValueError('Nickname must be at least 3 characters long')

    def __check_password(self, password: str) -> None:
        if not isinstance(password, str):
            raise TypeError('Password must be a string')
        if len(password) < 6:
            raise ValueError('Password must be at least 6 characters long')
