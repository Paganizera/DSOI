import os.path
from .controllers_abstract import ControllersAbstract
from entities.chat import Chat
from entities.user import User
from displays.chat_list_display import ChatListDisplay
from displays.chat_messages_display import ChatMessagesDisplay
from errors.custom_errors import InvalidOptionError
from history.text_message import TextMessage
from history.video_message import VideoMessage
from history.image_message import ImageMessage
from daos.chat_dao import ChatDAO

class ChatsController(ControllersAbstract):
    #   Instantiating the class's constructor and also
    #   Setting it's first atributtes
    def __init__(self, app: ControllersAbstract) -> None:
        if not isinstance(app, ControllersAbstract):
            raise TypeError(f"Expected ControllersAbstract, got {type(app)}")
        self.__dao: ChatDao()
        self.__current_chat: Chat | None = None
        self.__chat_list_display = ChatListDisplay()
        self.__chat_messages_display = ChatMessagesDisplay()
        self.__app = app

    # Getter
    @property
    def chats(self) -> list[Chat]:
        return self.__dao.get_all()

    # Getter
    @property
    def current_chat(self) -> Chat | None:
        return self.__current_chat

    #   Private function that analyzis wheter
    #   A Chat is or not in the chat list
    def __chat_in_list(self, chat: Chat) -> bool:
        for c in self.__dao.get_all():
            if c == chat:
                return True
        return False

    #   Private function that get's all chats where
    #   The current user is in
    def __get_chats_user_is_in(self) -> list[Chat]:
        chats = []
        for chat in self.__dao.get_all():
            if chat.user_in_chat(self.__app.get_current_user()):
                chats.append(chat)
        return chats

    #   Screen manipulation
    def open_screen(self) -> None:
        chat_list_options = {
            "1": self.add_chat,
            "2": self.open_my_chat,
            "3": self.your_chats,
            "4": self.browse_chats,
            "5": self.exit,
        }
        chat_options = {
            "1": self.send_text_message,
            "2": self.send_video_message,
            "3": self.send_image_message,
            "4": self.chat_history,
            "5": self.close_chat,
            "6": self.remove_user_from_chat,
        }
        #   While True makes the code to keep running
        #   For the purpouse of making avaiable to
        #   Use it for more than one function for a chat
        while True:
            if self.__current_chat is None:
                #   Selection pannel for chat options when there is no
                #   Active Chat
                try:
                    option = self.__chat_list_display.show_options()
                except InvalidOptionError as e:
                    #   Catch error and then show it to the user
                    self.__chat_list_display.show_error(str(e))
                else:
                    #   If there is no error, run the choosen function
                    chat_list_options[option]()
            else:
                #   Selection pannel for an active chat
                try:
                    option = self.__chat_messages_display.show_options(
                        self.__current_chat
                    )
                except InvalidOptionError as e:
                    self.__chat_messages_display.show_error(str(e))
                else:
                    chat_options[option]()
            self.__chat_list_display.enter_to_continue()

    #   Return screen
    def exit(self) -> None:
        self.__app.open_screen()

    #   Add a chat by setting a chatname that doesn't exists
    def add_chat(self) -> None:
        name = self.__chat_list_display.get_new_chat_name()
        try:
            #   Instantiates a new chat
            chat = Chat(name, self.__app.get_current_user())
        except Exception as e:
            self.__chat_list_display.show_error(str(e))
            return
        #   If there is already a chat that equals the new one
        #   Returns an error
        if self.__chat_in_list(chat):
            self.__chat_list_display.show_error("Chat already exists")
            return
        #   Auto add the current user to the new chat
        #   And then append it to the chat list
        chat.add_user(self.__app.get_current_user())
        self.__dao.get_all().add(chat)
        self.__chat_list_display.show_message("Chat created")

    #   Setts a current chat by a choosen one
    def open_my_chat(self) -> None:
        chats = self.__get_chats_user_is_in()
        #   Handle the case where there's no chats to open
        if chats == []:
            self.__chat_list_display.show_message("No chats to open")
            return
        #   Handle miss inputs
        try:
            index = self.__chat_list_display.get_user_chat_index(chats)
        except InvalidOptionError as e:
            self.__chat_list_display.show_error(str(e))
            return
        if index == -1:
            return
        #   Open the selected chat by setting it as the
        #   Current Chat one
        self.__current_chat = chats[index]
        self.__chat_messages_display.show_message("Chat opened")

    # Chats have user, user should have chats
    def your_chats(self) -> None:
        chats = self.__get_chats_user_is_in()
        if chats == []:
            #   Returns no chat if the list is empty
            self.__chat_list_display.show_message("No chats to show")
            return
        #   Return all chats when the list is not empty
        self.__chat_list_display.show_user_chats(chats)

    def browse_chats(self) -> None:
        if self.__dao.get_all() == []:
            self.__chat_list_display.show_message("No chats to show")
            return
        try:
            index = self.__chat_list_display.get_chat_index(self.__dao.get_all())
        except InvalidOptionError as e:
            self.__chat_list_display.show_error(str(e))
            return
        if index == -1:  # operation canceled
            return
        chat = self.__dao.get_all()[index]
        if chat.user_in_chat(self.__app.get_current_user()):
            self.__chat_list_display.show_message("You are already in this chat")
            return
        chat.add_user(self.__app.get_current_user())
        self.__chat_list_display.show_message("Chat joined")

    #   We need to validate path, because as we aren't dealing
    #   With GUI yet, we can't properly show images on terminal
    def validate_path(self, path: str) -> bool:
        return os.path.isfile(path)

    #   We get a message and then add it to the current
    #   Chat's history
    def send_text_message(self) -> None:
        user = self.__app.get_current_user()
        if not isinstance(user, User):
            raise TypeError(f"Expected User, got {type(user)}")
        if not self.__current_chat.user_in_chat(user):
            raise Exception("User not found")
        content = self.__chat_messages_display.get_input_text()
        message = TextMessage(content, user)
        self.__current_chat.chat_history.add_message(message)

    #   Instead of getting a txt message, we must get
    #   A file's path so we can use it later when
    #   GUI is meant
    def send_video_message(self) -> None:
        user = self.__app.get_current_user()
        if not isinstance(user, User):
            raise TypeError(f"Expected User, got {type(user)}")
        if not self.__current_chat.user_in_chat(user):
            raise Exception("User not found")
        #   Here we precreate the media's path for making it
        #   Easier to the user for just texting the file's name
        path = "./media/video/"
        path += self.__chat_messages_display.get_inputfile_name()
        #   We validate the path, if it's not valid we raise
        #   A custom Exception
        if not self.validate_path(path):
            self.__chat_messages_display.show_message("No file found")
        else:
            #   If the message is valid, we create a new VideoMessage
            #   And add it to the Chat's history
            message = VideoMessage(path, user)
            self.__current_chat.chat_history.add_message(message)

    #   This function is almost the same as send_video_message
    #   But we change the precreated path to the images folder
    def send_image_message(self) -> None:
        user = self.__app.get_current_user()
        if not isinstance(user, User):
            raise TypeError(f"Expected User, got {type(user)}")
        if not self.__current_chat.user_in_chat(user):
            raise Exception("User not found")
        path = "./media/image/"
        path += self.__chat_messages_display.get_inputfile_name()
        if not self.validate_path(path):
            self.__chat_messages_display.show_message("No file found")
        else:
            #   If the message is valid, we create a new VideoMessage
            #   And add it to the Chat's history
            message = ImageMessage(path, user)
            self.__current_chat.chat_history.add_message(message)

    #   This function is responsable for updating the messages's
    #   When an user isn't found anymore
    def update_chat(self) -> None:
        users = self.__app.get_all_users()
        #   We get all messages from the ChatHistory related class
        chat_messages = self.__current_chat.chat_history.messages
        #   For each message, it's analyzed wheter the message
        #   Has no user or the user isn't found anymore
        for message in chat_messages:
            flag = False
            if message.user == None:
                pass
            for user in users:
                if user == message.user:
                    flag = True
                    pass
            #   If the user isn't here, we make the message's
            #   User None
            if flag == False:
                message.user = None
        #   Finally we make the current messages from the
        #   ChatHistory class the updated ones
        self.__current_chat.chat_history.messages = chat_messages

    #   This function is responsable for displaying
    #   All the messages from a chat
    def chat_history(self) -> None:
        #   Firstly we must update the message list
        self.update_chat()
        chat = self.current_chat
        #   Then just needs to show on display
        self.__chat_messages_display.show_messages(chat)

    #   Closing the current chat by setting it to None
    def close_chat(self) -> None:
        self.__current_chat = None
        self.__chat_list_display.show_message("Chat closed")

    #   Removes a user from a chat by evaluating wheter it is
    #   The creator user, an abitrary user os the last in the
    #   Current chat
    def remove_user_from_chat(self) -> None:
        curr_user = self.__app.get_current_user()
        chat = self.__current_chat
        #   Removing not creator user from chat
        if chat.creator_user != curr_user:
            chat.remove_user(curr_user)
            self.__chat_messages_display.show_message("User removed from chat")
        #   When there is no user on a chat, it's removed from
        #   The chat list
        elif len(chat.users) == 1:
            if self.__chat_messages_display.y_n_question(
                "You are the only user in this chat. Do you want to remove it?"
            ):
                self.__dao.get_all().remove(chat)
                self.__chat_messages_display.show_message("Chat removed")
            else:
                self.__chat_messages_display.show_message("Chat not removed")
                return
        #   When you're a creator user you must change the current
        #   "ADM" user, then you might exit chat
        else:
            chat.change_creator_user()
            chat.remove_user(curr_user)
            self.__chat_messages_display.show_message("User removed from chat")
        self.__current_chat = None
