from Items.supply import Supply
from Factory_method.item_factory import ItemFactory
from Items.enums.item_types_enum import ItemTypesEnum
from db.DBSupply import DBSupply
from db.DBThirdPartyServices import DBThirdPartyServices
from User.user import User
from Items.enums.item_status_enum import ItemStatusEnum
"""
This module orchestrates the interaction between the different modules on this software.
It receives commands from the CLI module, executes them either by delegating the responsibility
to other modules or by itself.
"""


class MySME:

    __supplies: list[Supply] = []
    __dbSupplies: DBSupply
    __third_party_services: list = []
    __dbTPS: DBThirdPartyServices
    __item_factory: ItemFactory

    def __init__(self) -> None:
        self.__item_factory = ItemFactory()
        self.__dbSupplies = DBSupply()
        self.__dbTPS = DBThirdPartyServices()

        self.load_supplies()

    def user(self, email: str):
        return User(email)

    def add_supply(self, product, quantity, metric_unit, petitioner, user_email, code=None):
        item = self.__item_factory.create_item(ItemTypesEnum.SUPPLY, product, quantity, metric_unit, petitioner, code)
        item.add(self.user(user_email))
        self.__supplies.append(item)
        return item


    def show_supply(self):

        for supply in self.__supplies:
            print(supply)

    def show_supply_from_db(self):

        for supply in self.__dbSupplies.get():
            print(supply)

    def add_tps(self, service, provider, petitioner):
        """Adds third party service petition"""
        self.__third_party_services.append(
            self.__item_factory.create_item(ItemTypesEnum.THIRD_PARTY_SERVICES, service, provider, petitioner))

    def show_tps(self):

        for service in self.__third_party_services:
            print(service)

    def load_supplies(self):
        list_supply = self.__dbSupplies.get()
        
        for dict in list_supply:
            supply = self.__item_factory.create_item(ItemTypesEnum.SUPPLY,
                                                    dict['code'],
                                                    dict['product'],
                                                    dict['quantity'],
                                                    dict['metric_unit'],
                                                    dict['petitioner'])
            supply.add(self.user(dict['subscribers']))
            self.__supplies.append(supply)

    def save_supplies(self):
        for supply in self.__supplies:
            self.__dbSupplies.create(supply, supply.get_observers())

    def change_item_status(self, item, new_status: str):
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
        
    def update_supply(self, supply: Supply):
        self.__dbSupplies.update(supply.get_code(), supply, supply.get_observers())
    
