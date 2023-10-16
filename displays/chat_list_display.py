from .display_abstract import DisplayAbstract
from entities.chat import Chat
from errors.custom_errors import InvalidOptionError


class ChatListDisplay(DisplayAbstract):
    #   Uses the parent's method for showing the header
    def show_display_header(self) -> None:
        return super().show_display_header("Chat List Menu")

    #   Shows available options
    def show_options(self) -> str:
        self.show_display_header()
        print("\t1 - Add chat")
        print("\t2 - Open chat")
        print("\t3 - Your chats")
        print("\t4 - Browse chats")
        print("\t5 - Exit")
        option = input("Option: ").strip()

        #   Handle input errors
        if not self.is_valid_input(option, range(1, 6)):
            raise InvalidOptionError()
        return option

    #   Display format for showing chats
    def __show_chats(self, chats: list[Chat]):
        for n, chat in enumerate(chats):
            print(f"\t{n+1} - {chat.name} ({len(chat.users)} users)")

    #   Shows all chats options and then returns the choosen one
    def get_chat_index(self, chats: list[Chat]) -> int:
        while True:
            print("Chats:\n")
            #   Show all chats
            self.__show_chats(chats)
            index = input("\nSelect the chat you want to join (0 to cancel): ").strip()
            #   Evaluate the input
            if index == "0":
                return -1
            if not self.is_valid_input(index, range(1, len(chats) + 1)):
                raise InvalidOptionError()
            else:
                #   Returns the adjusted index
                index = int(index) - 1
                return index

    #   Shows all chats where the current user is
    #   For it to choose a chat
    def get_user_chat_index(self, chats: list[Chat]) -> int:
        while True:
            #   Shows all chats
            self.show_user_chats(chats)
            index = input("\nSelect the chat you want to open (0 to cancel): ").strip()
            #   Evaluate the input
            if index == "0":
                return -1
            if not self.is_valid_input(index, range(1, len(chats) + 1)):
                raise InvalidOptionError()
            #   Returns the adjusted index
            index = int(index) - 1
            return index

    #   Show all chats where the user is in
    def show_user_chats(self, chats: list[Chat]) -> None:
        print("Your chats:")
        self.__show_chats(chats)

    #   Changes the chat's name
    def get_new_chat_name(self) -> str:
        return input("Chat name: ").strip()
