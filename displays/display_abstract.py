from abc import ABC, abstractmethod
from controllers.controllers_abstract import ControllersAbstract
from subprocess import call
from platform import system


class DisplayAbstract(ABC):
    def __init__(self, controller: ControllersAbstract):
        self.__controller = controller

    @abstractmethod
    def show_options() -> int:
        pass

    def __clear_screen(self) -> None:
        call('cls' if system() == 'Windows' else 'clear', shell=True)

    def enter_to_continue(self) -> None:
        input('Press enter to continue...')

    def show_display_header(self, header: str) -> None:
        self.__clear_screen()
        n = 50
        print('-' * n)
        print('{:^{n}}'.format(header, n=n))
        print('-' * n)

    def is_valid_input(self, _input: str, _range: range) -> bool:
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

    def y_n_question(self, msg: str) -> bool:
        while True:
            option = input(msg + ' [y/n]: ').lower().strip()
            if option == 'y':
                return True
            elif option == 'n':
                return False
            else:
                print('Invalid option!')

    def show_message(self, message: str) -> None:
        print(message)

    def show_error(self, error: str) -> None:
        print('ERROR: '+ error)
