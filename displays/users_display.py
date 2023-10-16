from .display_abstract import DisplayAbstract
from getpass import getpass
from errors.custom_errors import InvalidOptionError
from uuid import UUID


class UsersDisplay(DisplayAbstract):
    #   Inheritances the method from parent class
    def show_display_header(self) -> None:
        return super().show_display_header("Users Menu")

    #   Options pannel
    def show_options(self) -> str:
        self.show_display_header()
        print("\t1 - Login")
        print("\t2 - Sign in")
        print("\t3 - Exit")
        option = input("Option: ").strip()

        #   Handle input errors
        if not self.is_valid_input(option, range(1, 4)):
            raise InvalidOptionError()
        return option

    #   Options pannels when the user is logged in
    def show_options_logged(self) -> str:
        self.show_display_header()
        print("\t1 - Logout")
        print("\t2 - Update user info")
        print("\t3 - Show user data")
        print("\t4 - Delete user")
        print("\t5 - Go to main menu")
        option = input("Option: ").strip()

        #   Handle input errors
        if not self.is_valid_input(option, range(1, 6)):
            raise InvalidOptionError()
        return option

    #   Gets a nickname and a password, then returns
    #   them as a tuple
    def get_data(self) -> tuple[str, str]:
        nickname = input("Nickname: ").strip()
        password = getpass("Password: ").strip()
        return nickname, password

    #   Returns current password
    def get_current_password(self) -> str:
        return getpass("Current password: ")

    #   Gets the user's info for displaying it
    def show_user_data(self, nickname: str, id: UUID) -> None:
        print(f"\tNickname: '{nickname}'")
        print(f"\tId      : '{id}'")
