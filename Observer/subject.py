from Observer.observer import Observer
from abc import ABC


class Subject(ABC):

    __observers: list[Observer]

    def __init__(self):
        self.__observers = []

    def add(self, observer: Observer) -> None:
        if observer not in self.__observers:
            self.__observers.append(observer)

    def remove(self, observer: Observer) -> None:
        self.__observers.remove(observer)

    def notify(self, item, message):
        for observer in self.__observers:
            observer.update(item, message)

    def get_observers(self) -> str:
        return self.__observers
