from db.DBItems import DBItems
from Items.supply import Supply
from Observer.observer import Observer


class DBSupply(DBItems):
    TABLE_NAME = "Supplies"

    def create_table(self):
        query = f"""
        CREATE TABLE IF NOT EXISTS {self.TABLE_NAME} (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            code VARCHAR(10) UNIQUE,
            created DATETIME,
            lastUpdated DATETIME,
            state VARCHAR(15),
            petitioner VARCHAR(50),
            product VARCHAR(100),
            quantity INTEGER,
            metric_unit VARCHAR(10),
            subscribers TEXT
        );
        """
        self.db.execute(query, commit=True)

    def item_to_dict(self, item: Supply, subscribers: list[Observer] = []):
        base = super().item_to_dict(item, subscribers)
        return {
            **base,
            "product": item.get_product(),
            "quantity": item.get_quantity(),
            "metric_unit": item.get_metric_unit(),
        }
