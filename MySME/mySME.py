from Items.supply import Supply
from Items.third_party_service import ThirdPartyServices
from Factory_method.item_factory import ItemFactory
from Items.enums.item_types_enum import ItemTypesEnum
from db.DBSupply import DBSupply
from db.DBThirdPartyServices import DBThirdPartyServices
from User.user import User
from Items.enums.item_status_enum import ItemStatusEnum


class MySME:
    def __init__(self):
        self.__item_factory = ItemFactory()
        self.__dbSupplies = DBSupply()
        self.__dbTPS = DBThirdPartyServices()
        self.__supplies: list[Supply] = []
        self.__third_party_services: list[ThirdPartyServices] = []
        self.load_supplies()
        self.load_third_party_services()

    def user(self, email: str):
        return User(email)

    # ----------- SUPPLIES -----------
    def add_supply(self, product, quantity, metric_unit, petitioner, user_email, code=None):
        item = self.__item_factory.create_item(
            ItemTypesEnum.SUPPLY, product, quantity, metric_unit, petitioner, code)
        item.add(self.user(user_email))
        self.__supplies.append(item)
        self.__dbSupplies.create(item, item.get_observers())
        return item

    def load_supplies(self):
        self.__supplies.clear()
        for item in self.__dbSupplies.get():
            supply = self.__item_factory.create_item(
                ItemTypesEnum.SUPPLY,
                item['product'],
                item['quantity'],
                item['metric_unit'],
                item['petitioner'],
                item['code']
            )
            supply.add(self.user(supply['subscribers']))
            self.__supplies.append(supply)

    def show_supplies(self):
        for supply in self.__supplies:
            print(supply)

    def update_supply_status(self, code, new_status):
        # Search the database, convert to object, change state, save and reload list
        data = next((d for d in self.__dbSupplies.get()
                    if d['code'] == code), None)
        if not data:
            print(f"No se encontró supply con code {code}")
            return
        supply = self.__item_factory.create_item(
            ItemTypesEnum.SUPPLY,
            data['product'],
            data['quantity'],
            data['metric_unit'],
            data['petitioner'],
            data['code']
        )
        supply.add(self.user(data['subscribers']))
        # Change status
        self.__change_item_status(supply, new_status)
        self.__dbSupplies.update(code, supply, supply.get_observers())
        self.load_supplies()

    # ----------- THIRD PARTY SERVICES -----------
    def add_third_party_service(self, service, provider, petitioner, user_email, code=None):
        tps = self.__item_factory.create_item(
            ItemTypesEnum.THIRD_PARTY_SERVICES, service, provider, petitioner, code)
        tps.add(self.user(user_email))
        self.__third_party_services.append(tps)
        self.__dbTPS.create(tps, tps.get_observers())
        return tps

    def load_third_party_services(self):
        self.__third_party_services.clear()
        for item in self.__dbTPS.get():
            tps = self.__item_factory.create_item(
                ItemTypesEnum.THIRD_PARTY_SERVICES,
                item['service'],
                item['provider'],
                item['petitioner'],
                item['code']
            )
            tps.add(self.user(item['subscribers']))
            self.__third_party_services.append(tps)

    def show_third_party_services(self):
        for tps in self.__third_party_services:
            print(tps)

    def update_third_party_service_status(self, code, new_status):
        data = next((d for d in self.__dbTPS.get() if d['code'] == code), None)
        if not data:
            print(f"No se encontró servicio con code {code}")
            return
        tps = self.__item_factory.create_item(
            ItemTypesEnum.THIRD_PARTY_SERVICES,
            data['service'],
            data['provider'],
            data['petitioner'],
            data['code']
        )
        tps.add(self.user(data['subscribers']))
        self.__change_item_status(tps, new_status)
        self.__dbTPS.update(code, tps, tps.get_observers())
        self.load_third_party_services()

    # ----------- CHANGE OF STATUS (GENERIC) -----------
    def __change_item_status(self, item, new_status: str):
        try:
            status_methods = {
                ItemStatusEnum.QUOTE: item.quote,
                ItemStatusEnum.ORDER: item.order,
                ItemStatusEnum.TRANSPORT: item.transport,
                ItemStatusEnum.RECEIVE: item.receive,
                ItemStatusEnum.REFUND: item.refund,
                ItemStatusEnum.CANCEL: item.cancel
            }
            status_enum = ItemStatusEnum(new_status)
            status_method = status_methods[status_enum]
            status_method()
        except KeyError:
            raise ValueError(f"Estado '{new_status}' no reconocido")
        except ValueError:
            raise ValueError(f"Estado '{new_status}' no es un estado válido")
