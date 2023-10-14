from history.base_message import BaseMessage

class ChatHistory:
    def __init__(self):
        self.__messages: list[BaseMessage] = []

    def get_messages(self) -> list[BaseMessage]:
        return self.__messages

    def add_message(self, message: BaseMessage) -> None:
        self.__messages.append(message)
