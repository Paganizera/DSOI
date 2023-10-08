from controllers_abstract import ControllersAbstract
from entities.chat import Chat
from displays.chat_list_display import ChatListDisplay
from displays.chat_messages_display import ChatMessagesDisplay


class ChatsController(ControllersAbstract):
    def __init__(self, app: ControllersAbstract) -> None:
        if not isinstance(app, ControllersAbstract):
            raise TypeError(f"Expected ControllersAbstract, got {type(app)}")
        self.__chats: list[Chat] = []
        self.__current_chat: Chat | None = None
        self.__chat_list_display = ChatListDisplay(self)
        self.__chat_messages_display = ChatMessagesDisplay(self)
        self.__app = app 

    @property
    def chats(self) -> list[Chat]:
        return self.__chats
    
    @property
    def current_chat(self) -> Chat | None:
        return self.__current_chat
    
    def open_screen(self) -> None:
        chat_list_options = {
            '1': self.add_chat,
            '2': self.remove_chat,
            '3': self.open_chat,
            '4': self.exit
        }
        chat_options = {
            '1': self.add_user_to_chat,
            '2': self.remove_user_from_chat,
            '3': self.send_message,
            '4': self.chat_history,
            '4': self.close_chat,
        }
        while True:
            if self.__current_chat is None:
                option = self.__chat_list_display.show_options()
                chat_list_options[option]()
            else:
                option = self.__chat_messages_display.show_options()
                chat_options[option]()
            self.__display.enter_to_continue()

    def exit(self) -> None:
       self.__app.open_screen()

    def add_chat(self) -> None:
        pass

    def remove_chat(self) -> None:
        pass

    def open_chat(self) -> None:
        pass

    def close_chat(self) -> None:
        self.__current_chat = None

    def add_user_to_chat(self) -> None:
        pass

    def remove_user_from_chat(self) -> None:
        pass

    def send_message(self) -> None:
        pass
    
    def chat_history(self) -> None:
        pass
