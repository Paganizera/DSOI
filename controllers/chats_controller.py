from .controllers_abstract import ControllersAbstract
from entities.chat import Chat
from entities.user import User
from displays.chat_list_display import ChatListDisplay
from displays.chat_messages_display import ChatMessagesDisplay
from errors.custom_errors import InvalidOptionError
from history.text_message import TextMessage
from history.video_message import VideoMessage
from history.image_message import ImageMessage

class ChatsController(ControllersAbstract):
    def __init__(self, app: ControllersAbstract) -> None:
        if not isinstance(app, ControllersAbstract):
            raise TypeError(f"Expected ControllersAbstract, got {type(app)}")
        self.__chats: list[Chat] = []
        self.__current_chat: Chat | None = None
        self.__chat_list_display = ChatListDisplay(self)
        self.__chat_messages_display = ChatMessagesDisplay(self)
        self.__app = app

    @property
    def chats(self) -> list[Chat]:
        return self.__chats

    @property
    def current_chat(self) -> Chat | None:
        return self.__current_chat

    def __chat_in_list(self, chat: Chat) -> bool:
        for c in self.__chats:
            if c == chat:
                return True
        return False

    def __get_chats_user_is_in(self) -> list[Chat]:
        chats = []
        for chat in self.__chats:
            if chat.user_in_chat(self.__app.get_current_user()):
                chats.append(chat)
        return chats

    def open_screen(self) -> None:
        chat_list_options = {
            '1': self.add_chat,
            # '2': self.remove_chat,
            '2': self.open_my_chat,
            '3': self.your_chats,
            '4': self.browse_chats,
            '5': self.exit
        }
        chat_options = {
            '1': self.send_message,
            '2': self.send_media_message,
            '3': self.chat_history,
            '4': self.close_chat,
            '5': self.remove_user_from_chat,
        }
        while True:
            if self.__current_chat is None:
                try:
                    option = self.__chat_list_display.show_options()
                except InvalidOptionError as e:
                    self.__chat_list_display.show_error(str(e))
                else:
                    chat_list_options[option]()
            else:
                try:
                    option = self.__chat_messages_display.show_options(
                        self.__current_chat)
                except InvalidOptionError as e:
                    self.__chat_messages_display.show_error(str(e))
                else:
                    chat_options[option]()
            self.__chat_list_display.enter_to_continue()

    def exit(self) -> None:
        self.__app.open_screen()

    def add_chat(self) -> None:
        name = self.__chat_list_display.get_new_chat_name()
        try:
            chat = Chat(name, self.__app.get_current_user())
        except Exception as e:
            self.__chat_list_display.show_error(str(e))
            return
        if self.__chat_in_list(chat):
            self.__chat_list_display.show_error('Chat already exists')
            return
        chat.add_user(self.__app.get_current_user())
        self.__chats.append(chat)
        self.__chat_list_display.show_message('Chat created')

    # removes chat from list, not from users
    # def remove_chat(self) -> None:
    #     chats = self.__get_chats_user_is_in()
    #     if chats == []:
    #         self.__chat_list_display.show_message('No chats to remove')
    #         return
    #     index = self.__chat_list_display.get_user_chat_index(chats)
    #     if index == -1:
    #         return
    #     chat = self.__chats[index]
    #     if chat.creator_user != self.__app.get_current_user():
    #         self.__chat_list_display.show_error('Only the creator can remove the chat')
    #         return
    #     del self.__chats[index]
    #     self.__chat_list_display.show_message('Chat removed')

    def open_my_chat(self) -> None:
        chats = self.__get_chats_user_is_in()
        if chats == []:
            self.__chat_list_display.show_message('No chats to open')
            return
        try:
            index = self.__chat_list_display.get_user_chat_index(chats)
        except InvalidOptionError as e:
            self.__chat_list_display.show_error(str(e))
            return
        if index == -1:
            return
        self.__current_chat = chats[index]
        self.__chat_messages_display.show_message('Chat opened')

    # Chats have user, user should have chats
    def your_chats(self) -> None:
        chats = self.__get_chats_user_is_in()
        if chats == []:
            self.__chat_list_display.show_message('No chats to show')
            return
        self.__chat_list_display.show_user_chats(chats)

    def browse_chats(self) -> None:
        if self.__chats == []:
            self.__chat_list_display.show_message('No chats to show')
            return
        try:
            index = self.__chat_list_display.get_chat_index(self.__chats)
        except InvalidOptionError as e:
            self.__chat_list_display.show_error(str(e))
            return
        if index == -1:  # operation canceled
            return
        chat = self.__chats[index]
        if chat.user_in_chat(self.__app.get_current_user()):
            self.__chat_list_display.show_message(
                'You are already in this chat')
            return
        chat.add_user(self.__app.get_current_user())
        self.__chat_list_display.show_message('Chat joined')

    # WE NEED TO VALIDATE MESSAGE FILES, BECAUSE AS WE CAN SEND TXT
    # AND ALSO MEDIA FILES, WE MUST' VALIDATE THEIR INTEGRITY

        # idk if this is the best way to do this
    def send_text_message(self, user: User) -> None:
        if not isinstance(user, User):
            raise TypeError(f"Expected User, got {type(user)}")
        if user not in self.__current_chat.__users:
            raise Exception('User not found')
        content = self.__chat_messages_display.get_input_text()
        message = TextMessage(content, user)
        self.current_chat.__chat_history.add_message(message)
    
    def send_video_message(self, user:User)->None:
        if not isinstance(user, User):
            raise TypeError(f"Expected User, got {type(user)}")
        if user not in self.__current_chat.__users:
            raise Exception('User not found')
        path = self.__chat_messages_display.get_input_path()
        if self.__validate_path(path):
            pass
        #print(self.__create_message_prefix(user) + message)
    '''    
    def send_image_message(self, user: User) -> None:
        if not isinstance(user, User):
            raise TypeError(f"Expected User, got {type(user)}")
        if user not in self.__users:
            raise Exception('User not found')
        path = ...
        message = ImageMessage(path)
        #print(self.__create_message_prefix(user) + message)
    
    def send_video_message(self, user: User) -> None:
        if not isinstance(user, User):
            raise TypeError(f"Expected User, got {type(user)}")
        if user not in self.__users:
            raise Exception('User not found')
        path = ...
        message = VideoMessage(path)
        #print(self.__create_message_prefix(user) + message)
    '''

    def chat_history(self) -> None:
        pass

    def close_chat(self) -> None:
        self.__current_chat = None
        self.__chat_list_display.show_message('Chat closed')

    def remove_user_from_chat(self) -> None:
        curr_user = self.__app.get_current_user()
        chat = self.__current_chat
        if chat.creator_user != curr_user:
            chat.remove_user(curr_user)
            self.__chat_messages_display.show_message('User removed from chat')
        elif len(chat.users) == 1:
            if self.__chat_messages_display.y_n_question('You are the only user in this chat. Do you want to remove it?'):
                self.__chats.remove(chat)
                self.__chat_messages_display.show_message('Chat removed')
            else:
                self.__chat_messages_display.show_message('Chat not removed')
                return
        else:
            chat.change_creator_user()
            chat.remove_user(curr_user)
            self.__chat_messages_display.show_message('User removed from chat')
        self.__current_chat = None
