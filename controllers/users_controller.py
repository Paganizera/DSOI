from entities.user import User
from daos.user_dao import UserDAO
from displays.users_display import UsersDisplay
from errors.custom_errors import ClosedProgramWindowError
from .controllers_abstract import ControllersAbstract


class UsersController(ControllersAbstract):
    def __init__(self, app: ControllersAbstract) -> None:
        if not isinstance(app, ControllersAbstract):
            raise TypeError(f"Expected ControllersAbstract, got {type(app)}")
        self.__current_user: None | User = None
        self.__dao = UserDAO()
        self.__display = UsersDisplay()
        self.__app = app

    #   Getters
    @property
    def current_user(self) -> None | User:
        return self.__current_user

    def get_users(self) -> list[User]:
        return self.__dao.get_all()

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
            "logout": self.logout,
            "update": self.update,
            "show": self.show_user_data,
            "delete": self.remove,
            "exit": self.exit,
        }
        options_not_logged = {
            "login": self.login,
            "signup": self.sign_up,
            "exit": self.exit,
        }
        #   Uses while to keep the code running
        while True:
            if self.__current_user is None:
                #   Handle input miss inputs
                try:
                    option = self.__display.show_options()
                except ClosedProgramWindowError as e:
                    self.__app.exit()
                else:
                    #   Runs the choosen function
                    options_not_logged[option]()
            else:
                #   Handle input miss inputs
                try:
                    option = self.__display.show_options_logged()
                except ClosedProgramWindowError as e:
                    self.__app.exit()
                else:
                    #   Runs the choosen function
                    options_logged[option]()

    #   Private function responsable for validanting passwords
    def __do_password_validation(self) -> bool:
        try:
            password = self.__display.get_current_password()
        except ClosedProgramWindowError:  # if the window was closed
            return False  # then the validation fails
        return User.hash256(password) == self.__current_user.password

    #   Login function that checks wheter the inputed that is
    #   a valid one and set the current user if the inputs
    #   matches with the users list
    def login(self) -> None:
        try:
            nickname, password = self.__display.get_data()
        except ClosedProgramWindowError:  # if the window was closed
            return  # then we return to the user menu
        flag = False
        #   Analyzes if the nickname and password's hash matches
        #   With the inputed data
        for user in self.get_users():
            if user.nickname == nickname and user.password == User.hash256(password):
                self.__current_user = user
                flag = True
                break
        #   Handle wheter the user was or wasn't found
        if not flag:
            self.__display.show_error("User not found")
        else:
            self.__display.show_message("User logged")

    #   Remove the current user by setting it to None
    def logout(self) -> None:
        #   Handle with error
        if self.__current_user is None:
            self.__display.show_error("User not logged")
            return
        #   Logs out
        self.__current_user = None
        self.__display.show_message("User logged out")

    #   Here we instantiate a new user to our users list
    def sign_up(self) -> None:
        try:
            nickname, password = self.__display.get_data()
        except ClosedProgramWindowError:  # if the window was closed
            return  # then we return to the user menu
        #   Handle input error and instantiations ones's
        #   as well
        try:
            user = User(nickname, password)
        except Exception as e:
            self.__display.show_error(str(e))
            return
        flag = True
        #   Checks for duplicated user
        for _user in self.get_users():
            if user == _user:
                flag = False
                break
        if not flag:
            self.__display.show_error("User already exists")
            return
        #   If the user has valid inputs after the analyzis
        #   Then instantiate it and set it as the new
        #   current user, which means it's auto logged in
        self.__dao.add(user)
        self.__current_user = user
        self.__display.show_message("User created")

    #   Update's the data from the current user as desired
    def update(self) -> None:
        if self.__current_user is None:
            self.__display.show_error("User not logged in")
            return
        #   In order to update the values we get the new data
        #   And analyzes the password
        if not self.__do_password_validation():
            self.__display.show_error("Invalid password")
            return
        #   Updates the user
        try:
            nickname, password = self.__display.get_data()
        except ClosedProgramWindowError:  # if the window was closed
            return  # then we return to the user menu
        try:
            self.__current_user.check_nickname(nickname)
            self.__current_user.check_password(password)
        except Exception as e:
            self.__display.show_error(str(e))
            return
        for user in self.get_users():
            if user.nickname == nickname and user.id != self.__current_user.id:
                self.__display.show_error("Nickname already exists")
                break
        else:
            self.__current_user.nickname = nickname
            self.__current_user.password = password
            self.__display.show_message("User updated")

    #   Delete the user from the user list
    def remove(self) -> None:
        if self.__current_user is None:
            self.__display.show_error("User not logged in")
            return
        #   Checks whether the user want's or not to
        #   delete it's acount
        if not self.__display.y_n_question(
            "Are you sure you want to delete your account?"
        ):
            return
        #   Makes a password validation
        if not self.__do_password_validation():
            self.__display.show_error("Invalid password")
            return
        #   Removes the user from the users list
        #   and also setts the current user as None
        self.__dao.remove(self.__current_user.id)
        self.__current_user = None
        self.__display.show_message("User removed successfully")

    #   responsable for sending user's data to display
    def show_user_data(self) -> None:
        curr = self.__current_user
        #   If there's no current user
        if curr is None:
            self.__display.show_error("User not logged")
            return
        #   Validate passwords
        if not self.__do_password_validation():
            self.__display.show_error("Invalid password")
            return
        #   Show user's id and nickname
        self.__display.show_user_data(curr.nickname, curr.id)
