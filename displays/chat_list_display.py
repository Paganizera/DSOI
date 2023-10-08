from display_abstract import DisplayAbstract
from controllers.controllers_abstract import ControllersAbstract
from entities.chat import Chat


class ChatListDisplay(DisplayAbstract):
    def __init__(self, controller: ControllersAbstract) -> None:
        if not isinstance(controller, ControllersAbstract):
            raise TypeError(f"Expected ControllersAbstract, got {type(controller)}")
        
        super().__init__(controller)
        
    def show_options(self) -> str:
        while True:
            self.show_display_header('Chat List Menu')
            print('\t1 - Add chat')
            print('\t2 - Remove chat')
            print('\t3 - Open chat')
            print('\t4 - Exit')
            option = input('Option: ')

            if not self.is_valid_input(option, range(1, 5)):
                print('Invalid option!')
            else:
                return option


    def show_chats(chats: list[Chat]) -> None:
        pass

    def remove_chat():
        pass

    def get_new_chat_name() -> str:
        pass
