from abc import ABC, abstractmethod


class IRepository(ABC):
    @abstractmethod
    def add(self, *args, **kwargs):
        pass

    @abstractmethod
    def load(self):
        pass

    @abstractmethod
    def show(self):
        pass

    @abstractmethod
    def get_by_code(self, code: str):
        pass

    @abstractmethod
    def update(self, code: str, new_status: str):
        pass

    @abstractmethod
    def add_observer(self, code: str, email: str):
        pass

    @abstractmethod
    def remove_observer(self, code: str, email: str):
        pass
