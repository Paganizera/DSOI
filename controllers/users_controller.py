from .controllers_abstract import ControllersAbstract
from entities.user import User
from displays.users_display import UsersDisplay
from errors.custom_errors import InvalidOptionError


class UsersController(ControllersAbstract):
    def __init__(self, app: ControllersAbstract) -> None:
        if not isinstance(app, ControllersAbstract):
            raise TypeError(f"Expected ControllersAbstract, got {type(app)}")
        self.__current_user: None | User = None
        self.__users: list[User] = []
        self.__display = UsersDisplay(self)
        self.__app = app
    
    @property
    def current_user(self) -> None | User:
        return self.__current_user
    
    @property
    def users(self) -> list[User]:
        return self.__users

    def exit(self) -> None:
        if self.__current_user is None:
            # A user should not be able to go back to the main menu if he 
            # is not logged in, hence we exit the program
            self.__app.exit()
        self.__app.open_screen()

    def open_screen(self) -> None:
        options_logged = {
            '1': self.logout,
            '2': self.update,
            '3': self.show_user_data,
            '4': self.remove,
            '5': self.exit
        }
        options_not_logged = {
            '1': self.login,
            '2': self.sign_in,
            '3': self.exit
        }
        while True:
            if self.__current_user is None:
                try:
                    option = self.__display.show_options()
                except InvalidOptionError as e:
                    self.__display.show_error(str(e))
                else:
                    options_not_logged[option]()
            else:
                try:
                    option = self.__display.show_options_logged()
                except InvalidOptionError as e:
                    self.__display.show_error(str(e))
                else:
                    options_logged[option]()
            self.__display.enter_to_continue()

    def __do_password_validation(self) -> bool:
        password = self.__display.get_current_password()
        return hash(password) == self.__current_user.password
    
    def login(self) -> None:
        nickname, password = self.__display.get_data()
        flag = False
        for user in self.__users:
            if user.nickname == nickname and user.password == hash(password):
                self.__current_user = user
                flag = True
                break
        if not flag:
            self.__display.show_error('User not found')
        else:
            self.__display.show_message('User logged')
    
    def logout(self) -> None:
        if self.__current_user is None:
            self.__display.show_error('User not logged')
            return
        self.__current_user = None
        self.__display.show_message('User logged out')
    
    def sign_in(self) -> None:
        nickname, password = self.__display.get_data()
        try:
            user = User(nickname, password)
        except Exception as e:
            self.__display.show_error(str(e))
            return
        flag = True
        for _user in self.__users:
            if user == _user:
                flag = False
                break
        if not flag:
            self.__display.show_error('User already exists')
            return
        self.__users.append(user)
        self.__current_user = user
        self.__display.show_message('User created')

    def update(self) -> None:
        if self.__current_user is None:
            self.__display.show_error('User not logged in')
            return
        nickname, password = self.__display.get_data()
        self.__current_user.nickname = nickname
        self.__current_user.password = password
        self.__display.show_message('User updated')

    def remove(self) -> None:
        if self.__current_user is None:
            self.__display.show_error('User not logged in')
            return
        if not self.__display.y_n_question('Are you sure you want to delete your account?'):
            return
        if not self.__do_password_validation():
            self.__display.show_error('Invalid password')
            return
        self.__users.remove(self.__current_user)
        del self.__current_user
        self.__current_user = None
        self.__display.show_message('User removed successfully')
    
    def show_user_data(self) -> None:
        curr = self.__current_user
        if curr is None:
            self.__display.show_error('User not logged')
            return
        if not self.__do_password_validation():
            self.__display.show_error('Invalid password')
            return
        self.__display.show_user_data(curr.nickname, curr.id)
