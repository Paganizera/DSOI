from .display_abstract import DisplayAbstract
from entities.chat import Chat
from errors.custom_errors import InvalidOptionError, ClosedProgramWindowError
from history.image_message import ImageMessage
from history.video_message import VideoMessage
from history.text_message import TextMessage
import PySimpleGUI as sg
from . import data

class ChatMessagesDisplay(DisplayAbstract):
    def __main__(self) -> None:
        super().__init__()



    def init_components(self) -> None:
        layout = [
            [sg.Text("Chat Options", size=(50, 1), justification="center", font=data.FONT_TITLE, relief=sg.RELIEF_RIDGE)],
            [sg.Radio("Add Chat", "RADIO1", default=True, size=(10, 1), font=data.FONT, key="-TEXTMESSAGE-")],
            [sg.Radio("Open Chat", "RADIO1", default=True, size=(10, 1), font=data.FONT, key="-VIDEOMESSAGE-")],
            [sg.Radio("Your Chats", "RADIO1", default=True, size=(10, 1), font=data.FONT, key="-YOURCHATS-")],
            [sg.Radio("Browse Chats", "RADIO1", default=True, size=(10, 1), font=data.FONT, key="-BROWSECHATS-")],
            [sg.Radio("Exit", "RADIO1", default=True, size=(10, 1), font=data.FONT, key="-EXIT-")],
            [sg.Button("Ok", size=(10, 1), font=data.FONT)]
        ]
        self.__window = sg.Window("Users Menu", layout, size=(data.HEIGHT, data.WIDTH), finalize=True)
    # Option pannel
    def show_options(self, chat: Chat) -> str:
        self.init_components()
        while True:
            event, values = self.__window.read()
            if event == "Ok":
                if values["-TEXTMESSAGE-"]:
                    retval = 'addchat'
                elif values["-VIDEOMESSAGE-"]:
                    retval = 'openchat'
                elif values["-IMAGEMESSAGE-"]:
                    retval = 'yourchats'
                elif values["-CHATHISTORY-"]:
                    retval = 'browsechats'
                elif values["-CLOSECHAT-"]:
                    retval = 'exit'
                elif values["EXIT"]:
                    retval = 'exit'
                break
            elif event == sg.WIN_CLOSED:
                raise ClosedProgramWindowError()
        self.__window.close()
        #self.close()  # isn't working
        return retval

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
