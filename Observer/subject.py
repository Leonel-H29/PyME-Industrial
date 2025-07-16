from Observer.observer import Observer


class Subject:

    __observers: list[Observer]

    def __init__(self, observers: list[Observer]):
        self.__observers = observers

    def add(self, observer: Observer) -> None:

        self.__observers.append(observer)

    def remove(self, observer: Observer) -> None:
        self.__observers.remove(observer)

    def notify(self):
        for observer in self.__observers:
            observer.update()
