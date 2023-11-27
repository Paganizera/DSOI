import PySimpleGUI as sg
from . import data
from .display_abstract import DisplayAbstract
from errors.custom_errors import ClosedProgramWindowError


class MainDisplay(DisplayAbstract):
    def __init__(self) -> None:
        super().__init__()

    def init_components(self) -> None:
        layout = [
            [
                sg.Text(
                    "Options Menu",
                    size=(50, 1),
                    justification="center",
                    font=data.FONT_TITLE,
                    relief=sg.RELIEF_RIDGE,
                )
            ],
            [
                sg.Radio(
                    "Users",
                    "RADIO1",
                    default=True,
                    size=(10, 1),
                    font=data.FONT,
                    key="-USERS-",
                )
            ],
            [
                sg.Radio(
                    "Chats",
                    "RADIO1",
                    default=True,
                    size=(10, 1),
                    font=data.FONT,
                    key="-CHATS-",
                )
            ],
            [
                sg.Radio(
                    "Exit",
                    "RADIO1",
                    default=True,
                    size=(10, 1),
                    font=data.FONT,
                    key="-EXIT-",
                )
            ],
            [
                sg.Column(
                    [[sg.Button("Ok", size=(10, 1), font=data.FONT)]],
                    justification="center",
                )
            ],
        ]
        self.__window = sg.Window(
            "Main Menu", layout, size=(data.HEIGHT, data.WIDTH), finalize=True
        )

    #   Option pannel for the mais display
    def show_options(self) -> str:
        self.init_components()
        while True:
            event, values = self.__window.read()
            if event == "Ok":
                if values["-USERS-"]:
                    retval = "users"
                elif values["-CHATS-"]:
                    retval = "chats"
                elif values["-EXIT-"]:
                    retval = "exit"
                break
            elif event == sg.WIN_CLOSED:
                raise ClosedProgramWindowError()
        self.__window.close()
        return retval
