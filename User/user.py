from Observer.observer import Observer


class User(Observer):

    __email: str

    def __init__(self, email: str):
        self.__email: str = email

    def update(self, item, message):
        print(
            f"Notificando a {self.__email}: {message} (Item: {item}, Estado: {item.get_state()})")

    def get_email(self) -> str:
        return self.__email
