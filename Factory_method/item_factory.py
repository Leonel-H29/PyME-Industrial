from abc import ABC, abstractmethod
from Items.item import Item

class ItemFactory(ABC):
    @abstractmethod
    def create_item(self, *arg, **kwargs)-> Item:
        pass