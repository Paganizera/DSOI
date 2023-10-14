from .display_abstract import DisplayAbstract
from controllers.controllers_abstract import ControllersAbstract
from entities.chat import Chat
from errors.custom_errors import InvalidOptionError

class ChatListDisplay(DisplayAbstract):
    def __init__(self, controller: ControllersAbstract) -> None:
        if not isinstance(controller, ControllersAbstract):
            raise TypeError(f"Expected ControllersAbstract, got {type(controller)}")
        
        super().__init__(controller)
        
    def __show_chats(self, chats: list[Chat]):
        for n, chat in enumerate(chats):
            print(f'\t{n+1} - {chat.name} ({len(chat.users)} users)')

    def show_display_header(self) -> None:
        return super().show_display_header('Chat List Menu')
    
    def show_options(self) -> str:
        self.show_display_header()
        print('\t1 - Add chat')
        print('\t2 - Open chat')
        print('\t3 - Your chats')
        print('\t4 - Browse chats')
        print('\t5 - Exit')
        option = input('Option: ').strip()

        if not self.is_valid_input(option, range(1, 6)):
            raise InvalidOptionError()
        return option

    def get_chat_index(self, chats: list[Chat]) -> int:
        while True:
            print('Chats:\n')
            self.__show_chats(chats)
            index = input('\nSelect the chat you want to join (0 to cancel): ').strip()

            if index == '0':
                return -1
            if not self.is_valid_input(index, range(1, len(chats)+1)):
                raise InvalidOptionError()
            else:
                index = int(index) - 1  # Adjusting to list index
                return index

    def get_user_chat_index(self, chats: list[Chat]) -> int:
        while True:
            self.show_user_chats(chats)
            index = input('\nSelect the chat you want to open (0 to cancel): ').strip()
            if index == '0':
                return -1
            if not self.is_valid_input(index, range(1, len(chats)+1)):
                raise InvalidOptionError()
            index = int(index) - 1  # Adjusting to list index
            return index

    def show_user_chats(self, chats: list[Chat]) -> None:
        print('Your chats:')
        self.__show_chats(chats)

    def get_new_chat_name(self) -> str:
        return input('Chat name: ').strip()
