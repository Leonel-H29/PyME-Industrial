import re
from Observer.observer import Observer


class User(Observer):

    __email: str

    def __init__(self, email: str):
        self.__email: str = self.__validate_email(email)

    def __validate_email(self, email: str) -> str:
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if re.match(pattern, email) is None:
            raise ValueError("El correo electrónico no es válido")
        return email

    def update(self, item, message):
        print(
            f"Notificando a {self.__email}: {message} (\nItem: {item}, \nEstado: {item.get_state()}\n)")

    def get_email(self) -> str:
        return self.__email
