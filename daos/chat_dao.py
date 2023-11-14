from .dao_abstract import DAO
from uuid import UUID
from entities.chat import Chat

#cada entidade terá uma classe dessa, implementação bem simples.
class UserDAO(DAO):
    def __init__(self):
        path = Path().parent / "source" / "chats.pkl"
        super().__init__(path)

    def add(self, chat: Chat):
        if((chat is not None) and isinstance(chat, Chat) and isinstance(chat.id, UUID)): 
            super().add(chat.id, chat)

    def update(self, chat: Chat):
        if((chat is not None) and isinstance(chat, Chat) and isinstance(chat.id, UUID)):
            super().update(chat.id, chat)

    def get(self, key:int):
        if isinstance(key, int):
            return super().get(key)

    def remove(selfself, key:int):
        if(isinstance(key, int)):
            return super().remove(key)