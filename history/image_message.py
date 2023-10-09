from .media_message import MediaMessage


class ImageMessage(MediaMessage):
    def __init__(self, path: str):
        super().__init__(path)
