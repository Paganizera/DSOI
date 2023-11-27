from abc import ABC, abstractmethod
import PySimpleGUI as sg
from . import data


class DisplayAbstract(ABC):
    @abstractmethod
    def __init__(self) -> None:
        self.__window: None | sg.Window = None
        sg.ChangeLookAndFeel("DarkAmber")

    def close(self) -> None:
        if self.__window is not None:
            self.__window.close()

    def y_n_question(self, msg: str) -> bool:
        retval = sg.popup_yes_no(msg, title="Confirm", font=data.FONT)
        return retval == "Yes"

    #   Used for custom messages to appear as system
    #   alerts/statuses
    def show_message(self, message: str) -> None:
        sg.popup(message, title="Message", font=data.FONT)

    def show_error(self, error: str) -> None:
        sg.popup_error(error, title="Error", font=data.FONT)
