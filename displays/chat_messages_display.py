from .display_abstract import DisplayAbstract
from entities.chat import Chat
from errors.custom_errors import InvalidOptionError
from history.image_message import ImageMessage
from history.video_message import VideoMessage
from history.text_message import TextMessage


class ChatMessagesDisplay(DisplayAbstract):
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
        if not self.is_valid_input(option, range(1, 7)):
            raise InvalidOptionError()
        return option

    #   Shows all messages from the current chat's ChatHistory
    def show_messages(self, chat: Chat) -> None:
        messages = chat.chat_history.messages
        #   Different prints wheter the user who sent
        #   Still has an account or has no more
        #   And also analyzes the messagetype
        for message in messages:
            if message.user == None:
                nickname = "Deleted User"
            else:
                nickname = message.user.nickname
            hour = str(message.timestamp.hour).zfill(2)
            minute = str(message.timestamp.minute).zfill(2)
            prefix = f"[{hour}:{minute}] {nickname}:"
            #   Text message print
            if isinstance(message, TextMessage):
                print(f"{prefix} {message.text}")
            #   Video message print
            elif isinstance(message, (VideoMessage, ImageMessage)):
                print(f"{prefix} {message.path}")

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
