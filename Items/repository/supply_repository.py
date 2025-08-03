from Items.repository.base_repository import BaseRepository
from Items.repository.irepository import IRepository
from db.DBSupply import DBSupply
from Items.enums.item_types_enum import ItemTypesEnum
from Items.supply import Supply


class SupplyRepository(BaseRepository, IRepository):

    def __init__(self) -> None:
        super().__init__()
        self.__dbSupplies = DBSupply()
        self.__supplies: list[Supply] = []

    def add(self, product: str, quantity: int, metric_unit: str, petitioner: str, user_emails: list[str], code=None, status=None) -> Supply:
        return self._add_item(
            item_type_enum=ItemTypesEnum.SUPPLY,
            db_instance=self.__dbSupplies,
            item_list=self.__supplies,
            item_args=[product, quantity, metric_unit, petitioner],
            user_emails=user_emails,
            code=code,
            status=status
        )

    def load(self) -> None:
        self._load_items(
            item_type_enum=ItemTypesEnum.SUPPLY,
            item_list=self.__supplies,
            db_instance=self.__dbSupplies,
            field_map=['product', 'quantity', 'metric_unit',
                       'petitioner', 'code', 'state']
        )

    def show(self) -> None:
        for supply in self.__supplies:
            print(supply)
            self.show_observers(supply)

    def get_by_code(self, code: str) -> Supply:
        return self._get_item(
            item_type_enum=ItemTypesEnum.SUPPLY,
            db_instance=self.__dbSupplies,
            code=code,
            field_map=['product', 'quantity', 'metric_unit',
                       'petitioner', 'code', 'state']
        )

    def update(self, code: str, new_status: str) -> None:
        self._update_item(
            code=code,
            new_status=new_status,
            db_instance=self.__dbSupplies,
            get_by_code_func=self.get_by_code,
            load_func=self.load
        )

    def add_observer(self, code: str, email: str) -> bool:
        item = self.get_by_code(code)
        if item:
            return self._add_observer(item, email, self.__dbSupplies, self.load)
        return False

    def remove_observer(self, code: str, email: str) -> bool:
        item = self.get_by_code(code)
        if item:
            return self._remove_observer(item, email, self.__dbSupplies, self.load)
        return False
