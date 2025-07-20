from db.DBItems import DBItems
from Items.raw_material import RawMaterial


class DBRawMaterial(DBItems):
    TABLE_NAME = "RawMaterials"

    def create_table(self):
        query = f"""
        CREATE TABLE IF NOT EXISTS {self.TABLE_NAME} (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            created DATETIME,
            lastUpdated DATETIME,
            state VARCHAR(15),
            petitioner VARCHAR(50),
            product VARCHAR(100),
            quantity INTEGER,
            metric_unit VARCHAR(10),
            subscribers VARCHAR(50)
        );
        """
        self.db.execute(query, commit=True)

    def item_to_dict(self, item: RawMaterial, subscribers=""):
        return {
            "created": item._Item__created.strftime('%Y-%m-%d %H:%M:%S'),
            "lastUpdated": item._Item__last_updated.strftime('%Y-%m-%d %H:%M:%S'),
            "state": str(item.get_state()),
            "petitioner": item._Item__petitioner,
            "product": item._RawMaterial__product,
            "quantity": item._RawMaterial__quantity,
            "metric_unit": item._RawMaterial__metric_unit,
            "subscribers": subscribers
        }
