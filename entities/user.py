from uuid import UUID, uuid4


class User:
    def __init__(self, nickname: str, password: str) -> None:
        self.__nickname = nickname
        self.__password = password
        self.__id = uuid4()
    
    @property
    def nickname(self) -> str:
        return self.__nickname

    @nickname.setter
    def nickname(self, nickname: str) -> None:
        if not isinstance(nickname, str):
            raise TypeError('Nickname must be a string')
        self.__nickname = nickname
    
    @property
    def password(self) -> str:
        return self.__password

    @password.setter
    def password(self, password: str) -> None:
        if not isinstance(password, str):
            raise TypeError('Password must be a string')
        self.__password = password
    
    @property
    def id(self) -> UUID:
        return self.__id

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, User):
            return False
        return self.__id == other.id or self.__nickname == other.nickname
