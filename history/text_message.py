from base_message import BaseMessage


class TextMessage(BaseMessage):
    def __init__(self, text: str):
        super().__init__()
        self.__text = text
    
    @property
    def text(self) -> str:
        return self.__text
