class ChatSelectionError(Exception):
    def __init__(self)-> None:
        super().__init__("There is no chat found with current input!")

class InvalidMessagePathError(Exception):
    def __init__(self) -> None:
        super().__init__("The file's path wasn't not found or the file doesn't exist")

class InvalidOptionError(Exception):
    def __init__(self) -> None:
        super().__init__("The selected option is not a valid one")
