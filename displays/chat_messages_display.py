from .display_abstract import DisplayAbstract
from controllers.controllers_abstract import ControllersAbstract
from entities.chat import Chat
from errors.custom_errors import InvalidOptionError
from history.image_message import ImageMessage
from history.video_message import VideoMessage
from history.text_message import TextMessage

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
        print('\t2 - Send video message')
        print('\t3 - Send image message')
        print('\t4 - Chat history')
        print('\t5 - Close chat')
        print('\t6 - Exit chat')
        option = input('Option: ').strip()

        if not self.is_valid_input(option, range(1, 6)):
            raise InvalidOptionError()
        return option

    def show_messages(self, chat: Chat) -> None:
        messages = chat.chat_history.get_messages()
        for message in messages:
            #   Text message print
            if isinstance(message, TextMessage):
                if message.user == None:
                    print(f'Deleted User: {message.text}\n {message.timestamp}')
                else:
                    print(f'{message.user.nickname}: {message.text}\n {message.timestamp}')
            #   Video message print
            if isinstance(message, VideoMessage) or isinstance (message, ImageMessage):
                if message.user == None:
                    print(f'Deleted User: {message.path}\n {message.timestamp}')
                else:
                    print(f'{message.user.nickname}: {message.path}\n {message.timestamp}')

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