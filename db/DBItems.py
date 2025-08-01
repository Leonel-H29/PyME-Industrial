from db.DBManager import DBManager
from Items.item import Item
from datetime import datetime
from abc import ABC, abstractmethod


class DBItems(ABC):
    TABLE_NAME: str | None = None

    def __init__(self):
        self.db = DBManager()
        self.create_table()

    @abstractmethod
    def create_table(self):
        pass

    def item_to_dict(self, item: Item, subscribers=None):
        if isinstance(subscribers, list):
            # If the list contains User objects, extract the email
            subscribers = [u.get_email() if hasattr(
                u, "get_email") else str(u) for u in subscribers]
            subscribers = ",".join(subscribers)

        elif subscribers is None:
            subscribers = ""

        return {
            "code": item.get_code(),
            "created": item._Item__created.strftime('%Y-%m-%d %H:%M:%S'),
            "lastUpdated": item._Item__last_updated.strftime('%Y-%m-%d %H:%M:%S'),
            "state": str(item.get_state()),
            "petitioner": item.get_petitioner(),
            "subscribers": subscribers,
        }

    def create(self, item: Item, subscribers=None):
        data = self.item_to_dict(item, subscribers)
        self.db.insert(self.TABLE_NAME, data)

    def get(self, item_id=None):
        if item_id:
            rows = self.db.select(self.TABLE_NAME, "ID = ?", (item_id,))
        else:
            rows = self.db.select(self.TABLE_NAME)
        return [dict(row) for row in rows]

    def update(self, item_id, item: Item, subscribers=None):
        data = self.item_to_dict(item, subscribers)
        self.db.update(self.TABLE_NAME, data, "code = ?", (item_id,))

    def delete(self, item_id):
        self.db.delete(self.TABLE_NAME, "ID = ?", (item_id,))
