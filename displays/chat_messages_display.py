from .display_abstract import DisplayAbstract
from controllers.controllers_abstract import ControllersAbstract
from entities.chat import Chat


class ChatMessagesDisplay(DisplayAbstract):
    def __init__(self, controller: ControllersAbstract) -> None:
        if not isinstance(controller, ControllersAbstract):
            raise TypeError(f"Expected ControllersAbstract, got {type(controller)}")
        
        super().__init__(controller)
    
    def show_display_header(self, chat: Chat) -> None:
        return super().show_display_header(f'Chat: {chat.name} ({len(chat.users)} users) [id: {chat.id}]')

    def show_options(self, chat: Chat) -> str:
        while True:
            self.show_display_header(chat)
            print('\t1 - Send message')
            print('\t2 - Chat history')
            print('\t3 - Close chat')
            print('\t4 - Exit chat')
            option = input('Option: ').strip()

            if not self.is_valid_input(option, range(1, 5)):
                print('Invalid option!')
            else:
                return option

    def show_messages(chat: Chat) -> None:
        pass

    def get_input() -> str:
        pass
