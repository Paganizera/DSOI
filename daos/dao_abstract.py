import pickle
from uuid import UUID
from typing import Any
from pathlib import Path
from abc import ABC, abstractmethod


class DAO(ABC):
    @abstractmethod
    def __init__(self, datasource: Path):
        datasource.parent.mkdir(parents=True, exist_ok=True)
        self.__datasource = datasource.absolute()
        if self.__datasource.is_file():
            self.__load()
        else:
            self.__cache: dict[UUID, Any] = {}

    def __dump(self):
        with self.__datasource.open("wb") as fd:
            pickle.dump(self.__cache, fd)

    def __load(self):
        with self.__datasource.open("rb") as fd:
            self.__cache = pickle.load(fd)

    # esse método precisa chamar o self.__dump()
    def add(self, key: UUID, obj):
        self.__cache[key] = obj
        self.__dump()  # atualiza o arquivo depois de add novo amigo
        return True

    # cuidado: esse update só funciona se o objeto com essa chave já existe
    def update(self, key: UUID, obj) -> bool:
        # try:
        if self.__cache.get(key, None) is not None:
            self.__cache[key] = obj  # atualiza a entrada
            self.__dump()  # atualiza o arquivo
            return True
        else:
            return False
        # except KeyError:
        #     pass  # implementar aqui o tratamento da exceção

    def get(self, key: UUID):
        return self.__cache.get(key, None)
        # try:
        #     return self.__cache[key]
        # except KeyError:
        #     pass #implementar aqui o tratamento da exceção

    # esse método precisa chamar o self.__dump()
    def remove(self, key: UUID) -> bool:
        value = self.__cache.pop(key, None)
        if value is not None:
            self.__dump()
            return True
        return False
        # try:
        #     self.__cache.pop(key)
        #     self.__dump() #atualiza o arquivo depois de remover um objeto
        # except KeyError:
        #     pass #implementar aqui o tratamento da exceção

    def get_all(self):
        # Python 3.7+: dicts must preserve insertion order
        return list(self.__cache.values())
