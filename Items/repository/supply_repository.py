from Items.repository.base_repository import BaseRepository
from db.DBSupply import DBSupply
from Items.enums.item_types_enum import ItemTypesEnum
from Items.supply import Supply


class SupplyRepository(BaseRepository):

    def __init__(self) -> None:
        super().__init__()
        self.__dbSupplies = DBSupply()
        self.__supplies: list[Supply] = []

    def add(self, product, quantity, metric_unit, petitioner, user_emails, code=None, status=None):
        item = self._item_factory.create_item(
            ItemTypesEnum.SUPPLY, product, quantity, metric_unit, petitioner, code, status)

        for email in user_emails:
            user = self.user(email)
            item.add(user)
        self.__supplies.append(item)

        self.__dbSupplies.create(item, item.get_observers())
        return item

    def load(self):
        self.__supplies.clear()
        for item in self.__dbSupplies.get():
            supply = self._item_factory.create_item(
                ItemTypesEnum.SUPPLY,
                item['product'],
                item['quantity'],
                item['metric_unit'],
                item['petitioner'],
                item['code'],
                item['state']
            )
            subscribers = item['subscribers'].split(
                ",") if item['subscribers'] else []
            for email in subscribers:
                supply.add(self.user(email))
            self.__supplies.append(supply)

    def show(self):
        for supply in self.__supplies:
            print(supply)

    def get_by_code(self, code: str):
        """Searches for a Supply in the database by its code and returns it as a Supply object."""
        rows = self.__dbSupplies.db.select(
            self.__dbSupplies.TABLE_NAME, "code = ?", (code,))
        if not rows:
            return None
        data = dict(rows[0])
        supply = self._item_factory.create_item(
            ItemTypesEnum.SUPPLY,
            data['product'],
            data['quantity'],
            data['metric_unit'],
            data['petitioner'],
            data['code'],
            data['state']
        )
        subscribers = data['subscribers'].split(
            ",") if data['subscribers'] else []
        for email in subscribers:
            supply.add(self.user(email))
        return supply

    def update(self, code, new_status):
        supply = self.get_by_code(code)
        self._change_item_status(supply, new_status)
        self.__dbSupplies.update(code, supply, supply.get_observers())
        self.load()
