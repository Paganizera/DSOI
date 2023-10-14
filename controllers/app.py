from .users_controller import UsersController
from .chats_controller import ChatsController
from .controllers_abstract import ControllersAbstract
from displays.main_display import MainDisplay
from entities.user import User
from errors.custom_errors import InvalidOptionError


class App(ControllersAbstract):
    def __init__(self):
        self.__users_controller = UsersController(self)
        self.__chats_controller = ChatsController(self)
        self.__display = MainDisplay(self)
    
    def open_screen(self) -> None:
        options = {
            '1': self.__users_controller.open_screen,
            '2': self.__chats_controller.open_screen,
            '3': self.exit
        }
        while True:
            try:
                option = self.__display.show_options()
            except InvalidOptionError as e:
                self.__display.show_error(str(e))
            else:
                options[option]()
            self.__display.enter_to_continue()

    def exit(self):
        exit(0)

    def start(self) -> None:
        self.__users_controller.open_screen()

    def get_current_user(self) -> User | None:
        return self.__users_controller.current_user