from Items.repository.base_repository import BaseRepository
from Items.repository.irepository import IRepository
from db.DBThirdPartyServices import DBThirdPartyServices
from Items.enums.item_types_enum import ItemTypesEnum
from Items.third_party_service import ThirdPartyServices


class ThirdPartyServiceRepository(BaseRepository, IRepository):

    def __init__(self) -> None:
        super().__init__()
        self.__dbTPS = DBThirdPartyServices()
        self.__third_party_services: list[ThirdPartyServices] = []

    def add(self, service, provider, petitioner, user_emails, code=None, status=None):
        return self._add_item(
            item_type_enum=ItemTypesEnum.THIRD_PARTY_SERVICES,
            db_instance=self.__dbTPS,
            item_list=self.__third_party_services,
            item_args=[service, provider, petitioner],
            user_emails=user_emails,
            code=code,
            status=status
        )

    def load(self):
        self._load_items(
            item_type_enum=ItemTypesEnum.THIRD_PARTY_SERVICES,
            item_list=self.__third_party_services,
            db_instance=self.__dbTPS,
            field_map=['service', 'provider', 'petitioner', 'code', 'state']
        )

    def show(self):
        for tps in self.__third_party_services:
            print(tps)
            self.show_observers(tps)

    def get_by_code(self, code: str):
        return self._get_item(
            item_type_enum=ItemTypesEnum.THIRD_PARTY_SERVICES,
            db_instance=self.__dbTPS,
            code=code,
            field_map=['service', 'provider', 'petitioner', 'code', 'state']
        )

    def update(self, code, new_status):
        self._update_item(
            code=code,
            new_status=new_status,
            db_instance=self.__dbTPS,
            get_by_code_func=self.get_by_code,
            load_func=self.load
        )

    def add_observer(self, code, email):
        item = self.get_by_code(code)
        if item:
            return self._add_observer(item, email, self.__dbTPS, self.load)
        return False

    def remove_observer(self, code, email):
        item = self.get_by_code(code)
        if item:
            return self._remove_observer(item, email, self.__dbTPS, self.load)
        return False
