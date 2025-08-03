

from Items.repository.supply_repository import SupplyRepository
from Items.repository.third_party_service_repository import ThirdPartyServiceRepository


class MySME:
    def __init__(self) -> None:
        self.__supplyRepository = SupplyRepository()
        self.__thirdPartyServiceRepository = ThirdPartyServiceRepository()

        self.load_supplies()
        self.load_third_party_services()

    # ----------- SUPPLIES -----------
    def add_supply(self, product: str, quantity: int, metric_unit: str, petitioner: str, user_emails: list[str], code: str = None, status: str = None):
        return self.__supplyRepository.add(product, quantity, metric_unit, petitioner, user_emails, code, status)

    def load_supplies(self):
        self.__supplyRepository.load()

    def show_supplies(self):
        self.__supplyRepository.show()

    def get_supply_by_code(self, code: str):
        return self.__supplyRepository.get_by_code(code)

    def update_supply_status(self, code: str, new_status: str):
        self.__supplyRepository.update(code, new_status)

    def add_supply_observer(self, code: str, email: str):
        return self.__supplyRepository.add_observer(code, email)

    def remove_supply_observer(self, code: str, email: str):
        self.__supplyRepository.remove_observer(code, email)

    # ----------- THIRD PARTY SERVICES -----------
    def add_third_party_service(self, service: str, provider: str, petitioner: str, user_emails, code=None, status=None):
        return self.__thirdPartyServiceRepository.add(service, provider, petitioner, user_emails, code, status)

    def load_third_party_services(self):
        self.__thirdPartyServiceRepository.load()

    def show_third_party_services(self):
        self.__thirdPartyServiceRepository.show()

    def get_third_party_service_by_code(self, code: str):
        return self.__thirdPartyServiceRepository.get_by_code(code)

    def update_third_party_service_status(self, code: str, new_status: str):
        self.__thirdPartyServiceRepository.update(code, new_status)

    def add_third_party_service_observer(self, code: str, email: str):
        return self.__thirdPartyServiceRepository.add_observer(code, email)

    def remove_third_party_service_observer(self, code: str, email: str):
        self.__thirdPartyServiceRepository.remove_observer(code, email)
