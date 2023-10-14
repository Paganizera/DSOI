from datetime import datetime
from entities.user import User


class BaseMessage:
    def __init__(self, user: User):
        self.__timestamp: datetime = datetime.now()
        self.__user = user

    @property
    def timestamp(self):
        return self.__timestamp

    @property
    def user(self):
        return self.__user

    @user.setter
    def user(self, user):
        self.__user = user
