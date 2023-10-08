from display_abstract import DisplayAbstract
from controllers_abstract import ControllersAbstract
from chat import Chat

class ChatMessagesDisplay(DisplayAbstract):
    def __init__(self, controller: ControllersAbstract) -> None:
        if not isinstance(controller, ControllersAbstract):
            raise TypeError(f"Expected ControllersAbstract, got {type(controller)}")
        
        super().__init__(controller)
        
    def show_options() -> int:
        pass

    def show_messages(chat: Chat) -> None:
        pass
    
    def show_chat_header(chat: Chat) -> None:
        pass

    def get_input() -> str:
        pass
