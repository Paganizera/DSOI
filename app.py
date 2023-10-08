from users_controller import UsersController
from chats_controller import ChatsController
from controllers_abstract import ControllersAbstract
from main_display import MainDisplay


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
            option = self.__display.show_options()
            options[option]()
            self.__display.enter_to_continue()

    def exit(self):
        exit(0)

    def start(self) -> None:
        self.__users_controller.open_screen()
