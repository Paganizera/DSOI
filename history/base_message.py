from datetime import datetime


class BaseMessage():
    def __init__(self):
        self.__timestamp: datetime = datetime.now()

    @property
    def timestamp(self):
        return self.__timestamp
