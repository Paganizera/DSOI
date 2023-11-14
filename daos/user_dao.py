from .dao_abstract import DAO
from uuid import UUID
from entities.user import User
from pathlib import Path

#cada entidade terá uma classe dessa, implementação bem simples.
class UserDAO(DAO):
    def __init__(self):
        path = Path().parent / "source"/ "users.pkl"
        super().__init__(str(path))

    def add(self, user: User):
        if((user is not None) and isinstance(user, User) and isinstance(user.id, UUID)): 
            super().add(user.id, user)

    def update(self, user: User):
        if((user is not None) and isinstance(user, User) and isinstance(user.id, UUID)):
            super().update(user.id, user)

    def get(self, key:int):
        if isinstance(key, int):
            return super().get(key)

    def remove(selfself, key:int):
        if(isinstance(key, int)):
            return super().remove(key)