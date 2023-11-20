from entities.user import User
from displays.main_display import MainDisplay
from .users_controller import UsersController
from .chats_controller import ChatsController
from .controllers_abstract import ControllersAbstract
from errors.custom_errors import ClosedProgramWindowError


class App(ControllersAbstract):
    def __init__(self):
        #   Instantiates all controllers and also the mais
        #   Display
        self.__users_controller = UsersController(self)
        self.__chats_controller = ChatsController(self)
        self.__display = MainDisplay()

    #   Open the main display
    def open_screen(self) -> None:
        options = {
            "users": self.__users_controller.open_screen,
            "chats": self.__chats_controller.open_screen,
            "exit": self.exit,
        }
        #   Keep it running for the purpouse of run
        #   More that one function
        while True:
            #   Handle input errors
            try:
                option = self.__display.show_options()
            except ClosedProgramWindowError as e:
                self.exit()
            else:
                #   Run the selected function
                options[option]()

    #   End program
    def exit(self):
        exit(0)

    #   The first function to run in this app
    def start(self) -> None:
        self.__users_controller.open_screen()

    #   Returns the current logged in user
    def get_current_user(self) -> User | None:
        return self.__users_controller.current_user

    #   Returns all users in the system
    def get_all_users(self) -> list[User]:
        return self.__users_controller.get_users()
