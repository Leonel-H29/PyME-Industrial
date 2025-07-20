from db.DBManager import DBManager
from Items.item import Item
from datetime import datetime
from abc import ABC, abstractmethod


class DBItems(ABC):
    TABLE_NAME = None

    def __init__(self):
        self.db = DBManager()
        self.create_table()

    @abstractmethod
    def create_table(self):
        pass

    @abstractmethod
    def item_to_dict(self, item: Item, subscribers=""):
        pass

    def create(self, item: Item, subscribers=""):
        data = self.item_to_dict(item, subscribers)
        self.db.insert(self.TABLE_NAME, data)

    def get(self, item_id=None):
        if item_id:
            rows = self.db.select(self.TABLE_NAME, "ID = ?", (item_id,))
        else:
            rows = self.db.select(self.TABLE_NAME)
        return [dict(row) for row in rows]

    def update(self, item_id, item: Item, subscribers=""):
        data = self.item_to_dict(item, subscribers)
        self.db.update(self.TABLE_NAME, data, "ID = ?", (item_id,))

    def delete(self, item_id):
        self.db.delete(self.TABLE_NAME, "ID = ?", (item_id,))
