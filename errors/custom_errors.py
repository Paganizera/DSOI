

class chat_selection_error(Exception):
    def __init__(self)-> None:
        super().__init__("There is no chat found with current input!")

class invalid_message_path(Exception):
    def __init__(self) -> None:
        super().__init__("The file's path wasn't not found or doesn't exists")

class invalid_option_error(Exception):
    def __init__(self) -> None:
        super().__init__("The selected option is not a valid one")

