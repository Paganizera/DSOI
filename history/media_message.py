from base_message import BaseMessage


class MediaMessage(BaseMessage):
    def __init__(self, path: str):
        super().__init__()
        self.__path = path
    
    @property
    def path(self) -> str:
        return self.__path
