from media_message import MediaMessage


class VideoMessage(MediaMessage):
    def __init__(self, path: str) -> None:
        super().__init__(path)
