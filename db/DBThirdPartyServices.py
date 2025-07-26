from db.DBItems import DBItems
from Items.third_party_service import ThirdPartyServices


class DBThirdPartyServices(DBItems):
    TABLE_NAME = "ThirdPartyServices"

    def create_table(self):
        query = f"""
        CREATE TABLE IF NOT EXISTS {self.TABLE_NAME} (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            code VARCHAR(10) UNIQUE,
            created DATETIME,
            lastUpdated DATETIME,
            state VARCHAR(15),
            petitioner VARCHAR(50),
            service VARCHAR(100),
            provider VARCHAR(100),
            subscribers VARCHAR(50)
        );
        """
        self.db.execute(query, commit=True)

    def item_to_dict(self, item: ThirdPartyServices, subscribers=""):
        base = super().item_to_dict(item, subscribers)
        return {
            **base,
            "service": item.get_service(),
            "provider": item.get_provider(),
        }
