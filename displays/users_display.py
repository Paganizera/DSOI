from uuid import UUID
import PySimpleGUI as sg
from . import data
from .display_abstract import DisplayAbstract
from errors.custom_errors import ClosedProgramWindowError

class UsersDisplay(DisplayAbstract):
    def __main__(self) -> None:
        super().__init__()
    
    def init_components(self) -> None:
        layout = [
            [sg.Text("Options Menu", size=(50, 1), justification="center", font=data.FONT_TITLE, relief=sg.RELIEF_RIDGE)],
            [sg.Radio("Login", "RADIO1", default=True, size=(10, 1), font=data.FONT, key="-LOGIN-")],
            [sg.Radio("Sign in", "RADIO1", default=True, size=(10, 1), font=data.FONT, key="-SIGNIN-")],
            [sg.Radio("Exit", "RADIO1", default=True, size=(10, 1), font=data.FONT, key="-EXIT-")],
            [sg.Button("Ok", size=(10, 1), font=data.FONT)]
        ]
        self.__window = sg.Window("Users Menu", layout, size=(data.HEIGHT, data.WIDTH), finalize=True)

    def show_options(self) -> str:
        self.init_components()
        while True:
            event, values = self.__window.read()
            if event == "Ok":
                if values["-LOGIN-"]:
                    retval = 'login'
                elif values["-SIGNIN-"]:
                    retval = 'signin'
                elif values["-EXIT-"]:
                    retval = 'exit'
                break
            elif event == sg.WIN_CLOSED:
                raise ClosedProgramWindowError()
        self.__window.close()
        #self.close()  # isn't working
        return retval

    def init_components_logged(self) -> None:
        layout = [
            [sg.Text("Options Menu", size=(50, 1), justification="center", font=data.FONT_TITLE, relief=sg.RELIEF_RIDGE)],
            [sg.Radio("Logout", "RADIO1", default=True, size=(20, 1), font=data.FONT, key="-LOGOUT-")],
            [sg.Radio("Update user info", "RADIO1", default=True, size=(20, 1), font=data.FONT, key="-UPDATE-")],
            [sg.Radio("Show user data", "RADIO1", default=True, size=(20, 1), font=data.FONT, key="-SHOW-")],
            [sg.Radio("Delete user", "RADIO1", default=True, size=(20, 1), font=data.FONT, key="-DELETE-")],
            [sg.Radio("Go to main menu", "RADIO1", default=True, size=(20, 1), font=data.FONT, key="-EXIT-")],
            [sg.Button("Ok", size=(10, 1), font=data.FONT)]
        ]
        self.__window = sg.Window("Logged Users Menu", layout, size=(data.HEIGHT, data.WIDTH), finalize=True)

    def show_options_logged(self) -> None:
        self.init_components_logged()
        while True:
            event, values = self.__window.read()
            if event == "Ok":
                if values["-LOGOUT-"]:
                    retval = 'logout'
                elif values["-UPDATE-"]:
                    retval = 'update'
                elif values["-SHOW-"]:
                    retval = 'show'
                elif values["-DELETE-"]:
                    retval = 'delete'
                elif values["-EXIT-"]:
                    retval = 'exit'
                break
            elif event == sg.WIN_CLOSED:
                raise ClosedProgramWindowError()
        self.__window.close()
        #self.close()  # isn't working
        return retval

    #   Gets a nickname and a password, then returns
    #   them as a tuple
    def get_data(self) -> tuple[str, str]:
        layout = [
            [sg.Text("Nickname:", size=(15, 1), font=data.FONT), sg.InputText(key="-NICKNAME-", font=data.FONT)],
            [sg.Text("Password:", size=(15, 1), font=data.FONT), sg.InputText(key="-PASSWORD-", font=data.FONT, password_char="*")],
            [sg.Button("Ok", size=(10, 1), font=data.FONT)]
        ]
        self.__window = sg.Window("Get User Data", layout, size=(data.HEIGHT, data.WIDTH), finalize=True)
        while True:
            event, values = self.__window.read()
            if event == "Ok":
                retval = (values["-NICKNAME-"], values["-PASSWORD-"])
                break
            elif event == sg.WIN_CLOSED:
                raise ClosedProgramWindowError()
        self.__window.close()
        #self.close()  # isn't working
        return retval

    #   Returns current password
    def get_current_password(self) -> str:
        layout = [
            [sg.Text("Password:", size=(15, 1), font=data.FONT), sg.InputText(key="-PASSWORD-", font=data.FONT, password_char="*")],
            [sg.Button("Ok", size=(10, 1), font=data.FONT)]
        ]
        self.__window = sg.Window("Get Current Password", layout, size=(data.HEIGHT, data.WIDTH), finalize=True)
        while True:
            event, values = self.__window.read()
            if event == "Ok":
                retval = values["-PASSWORD-"]
                break
            elif event == sg.WIN_CLOSED:
                raise ClosedProgramWindowError()
        self.__window.close()
        #self.close()  # isn't working
        return retval

    #   Gets the user's info for displaying it
    def show_user_data(self, nickname: str, id: UUID) -> None:
        layout = [
            [sg.Text(f"Nickname: {nickname}", size=(50, 1), justification="center", font=data.FONT)],
            [sg.Text(f"Id: {id}", size=(50, 1), justification="center", font=data.FONT)],
            [sg.Button("Ok", size=(10, 1), font=data.FONT)]
        ]
        self.__window = sg.Window("User Data", layout, size=(data.HEIGHT, data.WIDTH), finalize=True)
        while True:
            event, values = self.__window.read()
            if event == "Ok":
                break
            elif event == sg.WIN_CLOSED:
                raise ClosedProgramWindowError()
        self.__window.close()
        #self.close()  # isn't working
