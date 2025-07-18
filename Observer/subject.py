from Observer.observer import Observer
from abc import ABC


class Subject(ABC):

    __observers: list

    def __init__(self):
        self.__observers = []

    def add(self, observer: Observer) -> None:
        self.__observers.append(observer)

    def remove(self, observer: Observer) -> None:
        self.__observers.remove(observer)

    def notify(self, item, message):
        for observer in self.__observers:
            observer.update(item, message)
