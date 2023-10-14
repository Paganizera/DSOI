from .display_abstract import DisplayAbstract
from controllers.controllers_abstract import ControllersAbstract
from entities.chat import Chat
from errors.custom_errors import InvalidOptionError


class ChatMessagesDisplay(DisplayAbstract):
    def __init__(self, controller: ControllersAbstract) -> None:
        if not isinstance(controller, ControllersAbstract):
            raise TypeError(
                f"Expected ControllersAbstract, got {type(controller)}")

        super().__init__(controller)

    def show_display_header(self, chat: Chat) -> None:
        return super().show_display_header(f'Chat: {chat.name} ({len(chat.users)} users) [id: {chat.id}]')

    def show_options(self, chat: Chat) -> str:
        self.show_display_header(chat)
        print('\t1 - Send text message')
        print('\t2 - Send media message')
        print('\t3 - Chat history')
        print('\t4 - Close chat')
        print('\t5 - Exit chat')
        option = input('Option: ').strip()

        if not self.is_valid_input(option, range(1, 5)):
            raise InvalidOptionError()
        return option

    def show_messages(self, chat: Chat) -> None:
        pass

    def get_input_text(self) -> str:
        print("Insert the message to send")
        message = input().strip()
        return message

    def get_inputfile_name(self)-> str:
        print("Insert the name of the file to send")
        print("The extension of the file is needed")
        print("Such as example.png")
        media_name = input().strip()
        return media_name