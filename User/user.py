from Observer.observer import Observer

class User(Observer):

    __email: str

    def __init__(self, email: str):
        self.__email: str = email

    def notify(self):
        print(f'Se notifica a {self.__email}')
