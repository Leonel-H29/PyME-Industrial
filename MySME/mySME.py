from Items.supply import Supply
from Factory_method.item_factory import ItemFactory
from Items.enums.item_types_enum import ItemTypesEnum
"""
This module orchestrates the interaction between the different modules on this software.
It receives commands from the CLI module, executes them either by delegating the responsibility
to other modules or by itself.
"""


class MySME:

    __supplies: list = []
    __third_party__services: list = []
    __item_factory: ItemFactory

    def __init__(self) -> None:
        self.__item_factory = ItemFactory()

    def add_supply(self, product, quantity, metric_unit, petitioner):

        self.__supplies.append(
            self.__item_factory.create_item(ItemTypesEnum.SUPPLY, product, quantity, metric_unit, petitioner))

    def show_supply(self):

        for supply in self.__supplies:
            print(supply)

    def add_third_services(self, service, provider, petitioner):

        self.__third_party__services.append(
            self.__item_factory.create_item(ItemTypesEnum.THIRD_PARTY_SERVICES, service, provider, petitioner))

    def show_third_services(self):

        for service in self.__third_party__services:
            print(service)
