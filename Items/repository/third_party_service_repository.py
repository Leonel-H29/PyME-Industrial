from Items.repository.base_repository import BaseRepository
from db.DBThirdPartyServices import DBThirdPartyServices
from Items.enums.item_types_enum import ItemTypesEnum
from Items.third_party_service import ThirdPartyServices


class ThirdPartyServiceRepository(BaseRepository):

    def __init__(self) -> None:
        super().__init__()
        self.__dbTPS = DBThirdPartyServices()
        self.__third_party_services: list[ThirdPartyServices] = []

    def add(self, service, provider, petitioner, user_emails, code=None, status=None):
        tps = self._item_factory.create_item(
            ItemTypesEnum.THIRD_PARTY_SERVICES, service, provider, petitioner, code, status)

        for email in user_emails:
            user = self.user(email)
            tps.add(user)

        self.__third_party_services.append(tps)
        self.__dbTPS.create(tps, tps.get_observers())
        return tps

    def load(self):
        self.__third_party_services.clear()
        for item in self.__dbTPS.get():
            tps = self._item_factory.create_item(
                ItemTypesEnum.THIRD_PARTY_SERVICES,
                item['service'],
                item['provider'],
                item['petitioner'],
                item['code'],
                item['state']
            )
            subscribers = item['subscribers'].split(
                ",") if item['subscribers'] else []
            for email in subscribers:
                tps.add(self.user(email))
            self.__third_party_services.append(tps)

    def show(self):
        for tps in self.__third_party_services:
            print(tps)

    def get_by_code(self, code: str):
        """Searches for a Third Party Service in the database by its code and returns it as an object."""
        rows = self.__dbTPS.db.select(
            self.__dbTPS.TABLE_NAME, "code = ?", (code,))
        if not rows:
            return None
        data = dict(rows[0])
        tps = self._item_factory.create_item(
            ItemTypesEnum.THIRD_PARTY_SERVICES,
            data['service'],
            data['provider'],
            data['petitioner'],
            data['code'],
            data['state']
        )
        subscribers = data['subscribers'].split(
            ",") if data['subscribers'] else []
        for email in subscribers:
            tps.add(self.user(email))
        return tps

    def update(self, code, new_status):
        tps = self.get_by_code(code)
        self._change_item_status(tps, new_status)
        self.__dbTPS.update(code, tps, tps.get_observers())
        self.load()
