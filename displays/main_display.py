from .display_abstract import DisplayAbstract
from errors.custom_errors import InvalidOptionError


class MainDisplay(DisplayAbstract):
    #   Option pannel for the mais display
    def show_options(self) -> str:
        self.show_display_header("Main Menu")
        print("\t1 - Users Menu")
        print("\t2 - Chats Menu")
        print("\t3 - Exit")
        option = input("Option: ").strip()

        #   Handle miss inputs
        if not self.is_valid_input(option, range(1, 4)):
            raise InvalidOptionError()
        return option
