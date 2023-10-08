from controllers_abstract import ControllersAbstract
from user import User
from users_display import UsersDisplay


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
        self.__app.open_screen()

    def open_screen(self) -> None:
        options_logged = {
            '1': self.logout,
            '2': self.update,
            '3': self.remove,
            '4': self.exit
        }
        options_not_logged = {
            '1': self.login,
            '2': self.sign_in,
            '3': self.exit
        }
        while True:
            if self.__current_user is None:
                option = self.__display.show_options()
                options_not_logged[option]()
            else:
                option = self.__display.show_options_logged()
                options_logged[option]()
            self.__display.enter_to_continue()
                
    def login(self) -> None:
        nickname, password = self.__display.get_data()
        flag = False
        for user in self.__users:
            if user.nickname == nickname and user.password == password:
                self.__current_user = user
                flag = True
                break
        if not flag:
            self.__display.show_message('User not found')
        else:
            self.__display.show_message('User logged')
    
    def logout(self) -> None:
        if self.__current_user is None:
            self.__display.show_message('User not logged')
        else:
            self.__current_user = None
            self.__display.show_message('User logged out')
    
    def sign_in(self) -> None:
        nickname, password = self.__display.get_data()
        user = User(nickname, password)
        flag = True
        for _user in self.__users:
            if user == _user:
                flag = False
                break
        if not flag:
            self.__display.show_message('User already exists')
        else:
            self.__users.append(user)
            self.__current_user = user
            self.__display.show_message('User created')

    def update(self) -> None:
        if self.__current_user is None:
            self.__display.show_message('User not logged')
        else:
            nickname, password = self.__display.get_data()
            self.__current_user.nickname = nickname
            self.__current_user.password = password
            self.__display.show_message('User updated')

    def remove(self) -> None:
        if self.__current_user is None:
            self.__display.show_message('User not logged')
        else:
            if self.__display.y_n_question('Are you sure you want to delete your account?'):
                if not self.__do_password_validation():
                    self.__display.show_message('Invalid password')
                    return

                self.__users.remove(self.__current_user)
                self.__current_user = None
                self.__display.show_message('User removed successfully')
    
    def __do_password_validation(self) -> bool:
        password = self.__display.get_current_password()
        if password != self.__current_user.password:
            return False
        return True