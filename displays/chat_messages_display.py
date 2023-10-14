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
            raise TypeError(f"Expected ControllersAbstract, got {type(controller)}")

        super().__init__(controller)

    def show_display_header(self, chat: Chat) -> None:
        return super().show_display_header(
            f"Chat: {chat.name} ({len(chat.users)} users) [id: {chat.id}]"
        )

    # Option pannel
    def show_options(self, chat: Chat) -> str:
        self.show_display_header(chat)
        print("\t1 - Send text message")
        print("\t2 - Send video message")
        print("\t3 - Send image message")
        print("\t4 - Chat history")
        print("\t5 - Close chat")
        print("\t6 - Exit chat")
        option = input("Option: ").strip()
        #   Validate input
        if not self.is_valid_input(option, range(1, 6)):
            raise InvalidOptionError()
        return option

    #   Shows all messages from the current chat's ChatHistory
    def show_messages(self, chat: Chat) -> None:
        messages = chat.chat_history.messages
        #   Different prints wheter the user who sent
        #   Still has an account or has no more
        #   And also analyzes the messagetype
        for message in messages:
            #   Text message print
            if isinstance(message, TextMessage):
                if message.user == None:
                    print(
                        f"Deleted User: {message.text} at {message.timestamp.hour}:{message.timestamp.minute}"
                    )
                else:
                    print(
                        f"{message.user.nickname}: {message.text} at {message.timestamp.hour}:{message.timestamp.minute}"
                    )
            #   Video message print
            if isinstance(message, VideoMessage) or isinstance(message, ImageMessage):
                if message.user == None:
                    print(
                        f"Deleted User: {message.path} at {message.timestamp.hour}:{message.timestamp.minute}"
                    )
                else:
                    print(
                        f"{message.user.nickname}: {message.path} at {message.timestamp.hour}:{message.timestamp.minute}"
                    )

    #   Used for custom messages to appear as system
    #   alerts/statuses
    def show_message(self, message: str) -> None:
        print(message)

    #   Get the text content to send
    def get_input_text(self) -> str:
        print("Insert the message to send")
        message = input().strip()
        return message

    # Get the media's name that the user wants to send
    def get_inputfile_name(self) -> str:
        print("\tInsert the name of the file to send")
        print("\tThe extension of the file is needed")
        print("\tSuch as example.png")
        media_name = input().strip()
        return media_name
