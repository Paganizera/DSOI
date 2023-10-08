from base_message import BaseMessage


class ChatHistory:
    def __init__(self):
        self.__messages: list[BaseMessage] = []
        self.__buffer: list[BaseMessage] = []

    def add_message_to_buffer(self, message: BaseMessage) -> None:
        if not isinstance(message, BaseMessage):
            raise TypeError(f"Expected BaseMessage, got {type(message)}")
        self.__buffer.append(message)
    
    def get_and_clear_buffer(self) -> list[BaseMessage]:
        tmp = self.__buffer[:]
        self.__buffer = []
        return tmp

    def get_messages(self) -> list[BaseMessage]:
        return self.__messages
