import PySimpleGUI as sg
from . import data
from .display_abstract import DisplayAbstract
from errors.custom_errors import ClosedProgramWindowError


class MainDisplay(DisplayAbstract):
    #   Option pannel for the mais display
    def show_options(self) -> str:
        layout = [
            [sg.Text("Options Menu", size=(50, 1), justification="center", font=data.FONT_TITLE, relief=sg.RELIEF_RIDGE)],
            [sg.Radio("Users", "RADIO1", default=True, size=(10, 1), font=data.FONT, key="-USERS-")],
            [sg.Radio("Chats", "RADIO1", default=True, size=(10, 1), font=data.FONT, key="-CHATS-")],
            [sg.Radio("Exit", "RADIO1", default=True, size=(10, 1), font=data.FONT, key="-EXIT-")],
            [sg.Button("Ok", size=(10, 1), font=data.FONT)]
        ]
        window = sg.Window("Main Menu", layout, size=(data.HEIGHT, data.WIDTH), finalize=True)
        while True:
            event, values = window.read()
            if event == "Ok":
                if values["-USERS-"]:
                    retval = 'users'
                elif values["-CHATS-"]:
                    retval = 'chats'
                elif values["-EXIT-"]:
                    retval = 'exit'
                break
            elif event == sg.WIN_CLOSED:
                raise ClosedProgramWindowError()
        window.close()
        return retval
