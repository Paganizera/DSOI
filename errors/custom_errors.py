class ChatSelectionError(Exception):
    def __init__(self) -> None:
        super().__init__("There is no chat with current input!")


class InvalidMessagePathError(Exception):
    def __init__(self) -> None:
        super().__init__("The file's path wasn't not found or the file doesn't exist")


class InvalidOptionError(Exception):
    def __init__(self) -> None:
        super().__init__("The selected option is not a valid one")


class ClosedProgramWindowError(Exception):
    def __init__(self) -> None:
        super().__init__("The window was closed")


class UserNotFoundError(Exception):
    def __init__(self) -> None:
        super().__init__("The user wasn't found")

class InvalidPassword(Exception):
    def __init__(self) -> None:
        super().__init__("The password is incorrect")

class CloseChatError(Exception):
    def __init__(self) -> None:
        super().__init__("Chat closed")

class CloseChatListError(Exception):
    def __init__(self) -> None:
        super().__init__("ChatList closed")
