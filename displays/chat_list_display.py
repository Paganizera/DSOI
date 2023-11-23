from .display_abstract import DisplayAbstract
from entities.chat import Chat
from errors.custom_errors import InvalidOptionError
import PySimpleGUI as sg
from . import data
from errors.custom_errors import ClosedProgramWindowError
class ChatListDisplay(DisplayAbstract):
    def __main__(self) -> None:
        super().__init__()

    #   Shows available options
    def init_components(self) -> None:
        layout = [
            [sg.Text("ChatList", size=(50, 1), justification="center", font=data.FONT_TITLE, relief=sg.RELIEF_RIDGE)],
            [sg.Radio("Add Chat", "RADIO1", default=True, size=(10, 1), font=data.FONT, key="-ADDCHAT-")],
            [sg.Radio("Open Chat", "RADIO1", default=True, size=(10, 1), font=data.FONT, key="-OPENCHAT-")],
            [sg.Radio("Your Chats", "RADIO1", default=True, size=(10, 1), font=data.FONT, key="-YOURCHATS-")],
            [sg.Radio("Browse Chats", "RADIO1", default=True, size=(12, 1), font=data.FONT, key="-BROWSECHATS-")],
            [sg.Radio("Exit", "RADIO1", default=True, size=(10, 1), font=data.FONT, key="-EXIT-")],
            [sg.Button("Ok", size=(10, 1), font=data.FONT)]
        ]
        self.__window = sg.Window("Users Menu", layout, size=(data.HEIGHT, data.WIDTH), finalize=True)


    def show_options(self) -> str:
        self.init_components()
        while True:
            event, values = self.__window.read()
            if event == "Ok":
                if values["-ADDCHAT-"]:
                    retval = 'addchat'
                elif values["-OPENCHAT-"]:
                    retval = 'openchat'
                elif values["-YOURCHATS-"]:
                    retval = 'yourchats'
                elif values["-BROWSECHATS-"]:
                    retval = 'browsechats'
                elif values["-EXIT-"]:
                    retval = 'exit'
                break
            elif event == sg.WIN_CLOSED:
                raise ClosedProgramWindowError()
        self.__window.close()
        #self.close()  # isn't working
        return retval

    #   Shows all chats options and then returns the choosen one
    def get_chat_index(self, chats: list[Chat]) -> int:
        chat_names = [x.name for x in chats]
        lst = sg.Listbox(chat_names, size=(20, 4), font=('Arial Bold', 14), auto_size_text=True, enable_events=True, expand_x=True, select_mode=sg.LISTBOX_SELECT_MODE_BROWSE,  key='-LIST-')
        layout = [
            [lst],
            [sg.Button("Cancel", size=(10, 1), font=data.FONT),sg.Button("Submit", size=(10, 1), font=data.FONT)],
        ]
        self.__window = sg.Window("ChatList", layout, size=(data.HEIGHT, data.WIDTH), finalize=True)
        while True:
            event, values = self.__window.read()
            if event == "-LIST-":
                for chat in chats:
                    if chat.name == values[event][0]:
                        tmp = chats.index(chat)
            if event == "Submit":
                if tmp is not None:
                    retval = tmp
                    break
            if event == 'Cancel':
                retval = -1
                break
            if event in (sg.WIN_CLOSED, 'Exit'):
                break
        self.__window.close()
        return retval

    #   Shows all chats where the current user is
    #   For it to choose a chat
    def get_user_chat_index(self, chats: list[Chat]) -> int:
        chat_names = [x.name for x in chats]
        lst = sg.Listbox(chat_names, size=(20, 4), font=('Arial Bold', 14), auto_size_text=True, enable_events=True, expand_x=True, select_mode=sg.LISTBOX_SELECT_MODE_BROWSE ,key='-LIST-')
        layout = [
            [lst],
            [sg.Button("Cancel", size=(10, 1), font=data.FONT), sg.Button("Open", size=(10, 1), font=data.FONT)]
        ]
        self.__window = sg.Window("ChatList", layout, size=(data.HEIGHT, data.WIDTH), finalize=True)
        tmp = None
        while True:
            event, values = self.__window.read()
            if event == "-LIST-":
                for chat in chats:
                    if chat.name == values[event][0]:
                        tmp = chats.index(chat)
            if event == "Open":
                if tmp is not None:
                    retval = tmp
                    break
            if event == 'Cancel':
                retval = -1
                break
            if event in (sg.WIN_CLOSED, 'Exit'):
                break
        self.__window.close()
        return retval

    #   Show all chats where the user is in
    def show_user_chats(self, chats: list[Chat]) -> None:
        chat_names = [x.name for x in chats]
        lst = sg.Listbox(chat_names, size=(20, 4), font=('Arial Bold', 14), auto_size_text=True, enable_events=True, expand_x=True, select_mode=sg.LISTBOX_SELECT_MODE_BROWSE ,key='-LIST-')
        layout = [
            [lst],
            [sg.Button("Exit", size=(10, 1), font=data.FONT), sg.Button("Info", size=(10, 1), font=data.FONT)]
        ]
        self.__window = sg.Window("ChatList", layout, size=(data.HEIGHT, data.WIDTH), finalize=True)
        tmp = None
        while True:
            event, values = self.__window.read()
            if event == "-LIST-":
                for chat in chats:
                    if chat.name == values[event][0]:
                        tmp = chat
            if event == "Info":
                if tmp is not None:
                    message = 'Chatname: '+tmp.name+'\nChatID: '+str(tmp.id)
                    super().show_message(message)
            if event == 'Exit':
                break
            if event in (sg.WIN_CLOSED, 'Exit'):
                break
        self.__window.close()

    #   Changes the chat's name
    def get_new_chat_name(self) -> str:
        layout = [
            [sg.Text("New Chat Name:", size=(15, 1), font=data.FONT), sg.InputText(key="-CHATNAME-", font=data.FONT)],
            [sg.Button("Cancel", size=(10, 1), font=data.FONT), sg.Button("Submit", size=(10, 1), font=data.FONT)]
        ]
        self.__window = sg.Window("Creating Chat", layout, size=(data.HEIGHT, data.WIDTH), finalize=True)
        while True:
            event, values = self.__window.read()
            if event == "Submit":
                retval = values["-CHATNAME-"]
                break
            elif event == sg.WIN_CLOSED:
                raise ClosedProgramWindowError()
        self.__window.close()
        #self.close()  # isn't working
        return retval
