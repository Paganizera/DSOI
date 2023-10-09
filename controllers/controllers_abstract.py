from abc import ABC, abstractmethod


class ControllersAbstract(ABC):
    @abstractmethod
    def open_screen():
        pass

    @abstractmethod
    def exit():
        pass

