from Items.supply import Supply
from Factory_method.item_factory import ItemFactory
from Items.enums.item_types_enum import ItemTypesEnum
from db.DBSupply import DBSupply
from db.DBThirdPartyServices import DBThirdPartyServices
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

    def add_supply(self, product, quantity, metric_unit, petitioner):

        self.__supplies.append(
            self.__item_factory.create_item(ItemTypesEnum.SUPPLY, product, quantity, metric_unit, petitioner))

    def show_supply(self):

        for supply in self.__supplies:
            print(supply)

    def add_tps(self, service, provider, petitioner):
        """Adds third party service petition"""
        self.__third_party__services.append(
            self.__item_factory.create_item(ItemTypesEnum.THIRD_PARTY_SERVICES, service, provider, petitioner))

    def show_tps(self):

        for service in self.__third_party__services:
            print(service)

    def _load_supplies(self):
        #print(self.__dbSupplies.get())
        pass

    def _save_supplies(self):
        for supply in self.__supplies:
            self.__dbSupplies.create(supply, supply.get_petitioner())