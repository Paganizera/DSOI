from abc import ABC, abstractmethod
from subprocess import call
from platform import system
import PySimpleGUI as sg
from . import data


class DisplayAbstract(ABC):
    def __init__(self) -> None:
        self.__window: None | sg.Window = None
        sg.ChangeLookAndFeel("DarkAmber")  # test

    @abstractmethod
    def show_options() -> str:
        pass

    #@abstractmethod
    def init_components(self) -> None:
        pass
    
    # isn't working in UsersDisplay
    def close(self) -> None:
        if self.__window is not None:
            print('closing window', self.__window)
            self.__window.close()
            print('after close:', self.__window)

    def y_n_question(self, msg: str) -> bool:
        retval = sg.popup_yes_no(msg, title="Confirm", font=data.FONT)
        return retval == "Yes"

    def __clear_screen(self) -> None:
        call("cls" if system() == "Windows" else "clear", shell=True)

    def enter_to_continue(self) -> None:
        input("Press enter to continue...")

    def show_display_header(self, header: str) -> None:
        self.__clear_screen()
        n = 50
        print("-" * n)
        print("{:^{n}}".format(header, n=n))
        print("-" * n)

    def is_valid_input(self, _input: str | int, _range: range) -> bool:
        # checks the _range type
        if not isinstance(_range, range):
            return False

        # checks the _input type
        if not isinstance(_input, str):
            # checks if _input can be converted to int
            if not isinstance(_input, int):
                return False
            # checks if _input is in _range
            if _input not in _range:
                return False

        # checks if _input is numeric and in _range
        if not _input.isnumeric() or int(_input) not in _range:
            return False

        return True

    #   Used for custom messages to appear as system
    #   alerts/statuses
    def show_message(self, message: str) -> None:
        sg.popup(message, title="Message", font=data.FONT)

    def show_error(self, error: str) -> None:
        sg.popup_error(error, title="Error", font=data.FONT)
