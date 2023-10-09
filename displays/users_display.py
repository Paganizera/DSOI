from .display_abstract import DisplayAbstract
from controllers.controllers_abstract import ControllersAbstract
from getpass import getpass
from errors.custom_errors import invalid_option_error

class UsersDisplay(DisplayAbstract):
    def __init__(self, controller: ControllersAbstract) -> None:
        if not isinstance(controller, ControllersAbstract):
            raise TypeError(f"Expected ControllersAbstract, got {type(controller)}")
        
        super().__init__(controller)

    def show_display_header(self) -> None:
        return super().show_display_header('Users Menu')

    def show_options(self) -> str:
        while True:
            self.show_display_header()
            print('\t1 - Login')
            print('\t2 - Sign in')
            print('\t3 - Exit')
            option = input('Option: ').strip()
            
            if not self.is_valid_input(option, range(1, 4)):
                raise invalid_option_error()
            else:
                return option

    def show_options_logged(self) -> str:
        while True:
            self.show_display_header()
            print('\t1 - Logout')
            print('\t2 - Update user info')
            print('\t3 - Show user data')
            print('\t4 - Delete user')
            print('\t5 - Go to main menu')
            option = input('Option: ').strip()

            if not self.is_valid_input(option, range(1, 6)):
                raise invalid_option_error()
            else:
                return option

    def get_data(self) -> tuple[str, str]:
        nickname = input('Nickname: ').strip()
        password = getpass('Password: ')
        return nickname, password

    def get_current_password(self) -> str:
        return getpass('Current password: ')

    def show_user_data(self, nickname: str, password: str) -> None:
        print(f'Nickname: \"{nickname}\"')
        print(f'Password: \"{password}\"')
