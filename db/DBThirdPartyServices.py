from db.DBItems import DBItems
from Items.third_party_service import ThirdPartyServices


class DBThirdPartyServices(DBItems):
    TABLE_NAME = "ThirdPartyServices"

    def create_table(self):
        query = f"""
        CREATE TABLE IF NOT EXISTS {self.TABLE_NAME} (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
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
        return {
            "created": item._Item__created.strftime('%Y-%m-%d %H:%M:%S'),
            "lastUpdated": item._Item__last_updated.strftime('%Y-%m-%d %H:%M:%S'),
            "state": str(item.get_state()),
            "petitioner": item._Item__petitioner,
            "service": item._ThirdPartyServices__service,
            "provider": item._ThirdPartyServices__provider,
            "subscribers": subscribers
        }
