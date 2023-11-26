from uuid import UUID
from pathlib import Path
from .dao_abstract import DAO
from entities.chat import Chat


class ChatDAO(DAO):
    def __init__(self):
        path = Path().parent / "source" / "chats.pkl"
        super().__init__(path)

    def add(self, chat: Chat) -> bool:
        if isinstance(chat, Chat) and isinstance(chat.id, UUID):
            return super().add(chat.id, chat)
        return False

    def update(self, chat: Chat) -> bool:
        if isinstance(chat, Chat) and isinstance(chat.id, UUID):
            return super().update(chat.id, chat)
        return False

    def get(self, key: UUID) -> Chat | None:
        if isinstance(key, UUID):
            return super().get(key)
        return None

    def remove(self, key: UUID) -> bool:
        if isinstance(key, UUID):
            return super().remove(key)
        return False
