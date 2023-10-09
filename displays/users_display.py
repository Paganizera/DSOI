from .display_abstract import DisplayAbstract
from controllers.controllers_abstract import ControllersAbstract


class UsersDisplay(DisplayAbstract):
    def __init__(self, controller: ControllersAbstract) -> None:
        if not isinstance(controller, ControllersAbstract):
            raise TypeError(f"Expected ControllersAbstract, got {type(controller)}")
        
        super().__init__(controller)

    def show_options(self) -> str:
        while True:
            self.show_display_header('Users Menu')
            print('\t1 - Login')
            print('\t2 - Sign in')
            print('\t3 - Exit')
            option = input('Option: ')
            
            if not self.is_valid_input(option, range(1, 4)):
                print('Invalid option!')
            else:
                return option

    def show_options_logged(self) -> str:
        while True:
            self.show_display_header('Users Menu')
            print('\t1 - Logout')
            print('\t2 - Update user info')
            print('\t3 - Delete user')
            print('\t4 - Go to main menu')
            option = input('Option: ').strip()

            if not self.is_valid_input(option, range(1, 5)):
                print('Invalid option!')
            else:
                return option

    def get_data(self) -> tuple[str, str]:
        nickname = input('Nickname: ').strip()
        password = input('Password: ')
        return nickname, password

    def get_current_password(self) -> str:
        return input('Current password: ')

    def show_user_data(self, nickname: str, password: str) -> None:
        print(f'Nickname: \"{nickname}\"')
        print(f'Password: \"{password}\"')
        
    def show_message(self, message: str) -> None:
        print(message)

    def y_n_question(self, msg: str) -> bool:
        while True:
            option = input(msg + ' [y/n]: ').lower().strip()
            if option == 'y':
                return True
            elif option == 'n':
                return False
            else:
                print('Invalid option!')
