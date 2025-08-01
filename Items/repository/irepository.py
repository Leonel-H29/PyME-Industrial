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
    def update(self, code, new_status):
        pass
