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
    
    #   Getters
    @property
    def current_user(self) -> None | User:
        return self.__current_user
    
    @property
    def users(self) -> list[User]:
        return self.__users

    #   Returns from the current screen
    def exit(self) -> None:
        if self.__current_user is None:
            # A user should not be able to go back to the main menu if he 
            # is not logged in, hence we exit the program
            self.__app.exit()
        self.__app.open_screen()

    #   Screen manipulation
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
        #   Uses while to keep the code running
        while True:
            if self.__current_user is None:
                #   Handle input miss inputs
                try:
                    option = self.__display.show_options()
                except InvalidOptionError as e:
                    self.__display.show_error(str(e))
                else:
                    #   Runs the choosen function
                    options_not_logged[option]()
            else:
                #   Handle input miss inputs
                try:
                    option = self.__display.show_options_logged()
                except InvalidOptionError as e:
                    self.__display.show_error(str(e))
                else:
                    #   Runs the choosen function
                    options_logged[option]()
            self.__display.enter_to_continue()

    #   Private function responsable for validanting passwords
    def __do_password_validation(self) -> bool:
        password = self.__display.get_current_password()
        return hash(password) == self.__current_user.password
    
    #   Login function that checks wheter the inputed that is 
    #   a valid one and set the current user if the inputs
    #   matches with the users list
    def login(self) -> None:
        nickname, password = self.__display.get_data()
        flag = False
        #   Analyzes if the nickname and password's hash matches
        #   With the inputed data
        for user in self.__users:
            if user.nickname == nickname and user.password == hash(password):
                self.__current_user = user
                flag = True
                break
        #   Handle wheter the user was or wasn't found
        if not flag:
            self.__display.show_error('User not found')
        else:
            self.__display.show_message('User logged')
    

    #   Remove the current user by setting it to None
    def logout(self) -> None:
        #   Handle with error
        if self.__current_user is None:
            self.__display.show_error('User not logged')
            return
        #   Logs out
        self.__current_user = None
        self.__display.show_message('User logged out')
    
    #   Here we instantiate a new user to our users list
    def sign_in(self) -> None:
        nickname, password = self.__display.get_data()
        #   Handle input error and instantiations ones's
        #   as well
        try:
            user = User(nickname, password)
        except Exception as e:
            self.__display.show_error(str(e))
            return
        flag = True
        #   Checks for duplicated user
        for _user in self.__users:
            if user == _user:
                flag = False
                break
        if not flag:
            self.__display.show_error('User already exists')
            return
        #   If the user has valid inputs after the analyzis
        #   Then instantiate it and set it as the new
        #   current user, which means it's auto logged in
        self.__users.append(user)
        self.__current_user = user
        self.__display.show_message('User created')

    #   Update's the data from the current user as desired
    def update(self) -> None:
        if self.__current_user is None:
            self.__display.show_error('User not logged in')
            return
        #   In order to update the values we get the new data
        #   And analyzes the password
        if not self.__do_password_validation():
            self.__display.show_error('Invalid password')
            return
        #   Updates the user
        nickname, password = self.__display.get_data()
        self.__current_user.nickname = nickname
        self.__current_user.password = password
        self.__display.show_message('User updated')

    #   Delete the user from the user list
    def remove(self) -> None:
        if self.__current_user is None:
            self.__display.show_error('User not logged in')
            return
        #   Checks whether the user want's or not to 
        #   delete it's acount
        if not self.__display.y_n_question('Are you sure you want to delete your account?'):
            return
        #   Makes a password validation
        if not self.__do_password_validation():
            self.__display.show_error('Invalid password')
            return
        #   Removes the user from the users list
        #   and also setts the current user as None
        self.__users.remove(self.__current_user)
        self.__current_user = None
        self.__display.show_message('User removed successfully')
    
    #   responsable for sending user's data to display
    def show_user_data(self) -> None:
        curr = self.__current_user
        #   If there's no current user
        if curr is None:
            self.__display.show_error('User not logged')
            return
        #   Validate passwords
        if not self.__do_password_validation():
            self.__display.show_error('Invalid password')
            return
        #   Show user's id and nickname
        self.__display.show_user_data(curr.nickname, curr.id)
