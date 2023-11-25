from uuid import UUID
from pathlib import Path
from .dao_abstract import DAO
from entities.user import User


class UserDAO(DAO):
    def __init__(self):
        path = Path().parent / "source" / "users.pkl"
        super().__init__(path)

    def add(self, user: User) -> bool:
        if isinstance(user, User) and isinstance(user.id, UUID):
            return super().add(user.id, user)
        return False

    def update(self, user: User) -> bool:
        if isinstance(user, User) and isinstance(user.id, UUID):
            return super().update(user.id, user)
        return False

    def get(self, key: UUID) -> User | None:
        if isinstance(key, UUID):
            return super().get(key)
        return False

    def remove(selfself, key: UUID) -> bool:
        if isinstance(key, UUID):
            return super().remove(key)
        return False
