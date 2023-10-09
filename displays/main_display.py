from .display_abstract import DisplayAbstract
from controllers.controllers_abstract import ControllersAbstract
from errors.custom_errors import invalid_option_error

class MainDisplay(DisplayAbstract):
    def __init__(self, controller: ControllersAbstract) -> None:
        if not isinstance(controller, ControllersAbstract):
            raise TypeError(f"Expected ControllersAbstract, got {type(controller)}")
        
        super().__init__(controller)

    def show_options(self) -> str:
        while True:
            self.show_display_header('Main Menu')
            print('\t1 - Users Menu')
            print('\t2 - Chats Menu')
            print('\t3 - Exit')
            option = input('Option: ')

            if not self.is_valid_input(option, range(1, 4)):
                raise invalid_option_error()
            else:
                return option
