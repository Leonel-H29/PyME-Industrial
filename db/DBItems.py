from db.DBManager import DBManager
from Items.item import Item
from datetime import datetime


class DBItems:
    TABLE_NAME = "Items"

    def __init__(self):
        self.db = DBManager()
        self.create_table()

    def create_table(self):
        query = f"""
        CREATE TABLE IF NOT EXISTS {self.TABLE_NAME} (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            created DATE,
            lastUpdated DATE,
            state VARCHAR(15),
            petitioner VARCHAR(50),
            product VARCHAR(50),
            quantity REAL,
            metricUnit CHAR(2),
            subscriptors VARCHAR(50)
        );
        """
        self.db.execute(query, commit=True)

    def item_to_dict(self, item: Item, subscriptors=""):
        return {
            "created": datetime.now().date(),
            "lastUpdated": datetime.now().date(),
            "state": str(item.get_state()),
            "petitioner": item._Item__petitioner,
            "product": item._Item__product,
            "quantity": item._Item__quantity,
            "metricUnit": item._Item__metric_unit,
            "subscriptors": subscriptors
        }

    def create(self, item: Item, subscriptors=""):
        data = self.item_to_dict(item, subscriptors)
        self.db.insert(self.TABLE_NAME, data)

    def get(self, item_id=None):
        if item_id:
            rows = self.db.select(self.TABLE_NAME, "ID = ?", (item_id,))
        else:
            rows = self.db.select(self.TABLE_NAME)
        return [dict(row) for row in rows]

    def update(self, item_id, item: Item, subscriptors=""):
        data = self.item_to_dict(item, subscriptors)
        data["lastUpdated"] = datetime.now().date()
        self.db.update(self.TABLE_NAME, data, "ID = ?", (item_id,))

    def delete(self, item_id):
        self.db.delete(self.TABLE_NAME, "ID = ?", (item_id,))
