from .display_abstract import DisplayAbstract
from controllers.controllers_abstract import ControllersAbstract
from errors.custom_errors import InvalidOptionError

class MainDisplay(DisplayAbstract):
    def __init__(self, controller: ControllersAbstract) -> None:
        if not isinstance(controller, ControllersAbstract):
            raise TypeError(f"Expected ControllersAbstract, got {type(controller)}")
        
        super().__init__(controller)
    
    #   Option pannel for the mais display
    def show_options(self) -> str:
        self.show_display_header('Main Menu')
        print('\t1 - Users Menu')
        print('\t2 - Chats Menu')
        print('\t3 - Exit')
        option = input('Option: ')
        
        #   Handle miss inputs
        if not self.is_valid_input(option, range(1, 4)):
            raise InvalidOptionError()
        return option
