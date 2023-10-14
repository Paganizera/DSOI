from history.base_message import BaseMessage

class ChatHistory:
    def __init__(self):
        self.__messages: list[BaseMessage] = []

    @property 
    def messages(self) -> list[BaseMessage]:
        return self.__messages
    
    @messages.setter
    def messages(self, messages: list[BaseMessage])->None:
        self.__messages = messages

    def add_message(self, message: BaseMessage) -> None:
        self.__messages.append(message)
