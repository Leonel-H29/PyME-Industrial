from Items.supply import Supply
"""
This module orchestrates the interaction between the different modules on this software.
It receives commands from the CLI module, executes them either by delegating the responsibility
to other modules or by itself.
"""


class MySME:

    __supplies: list = []

    def add_supply(self, product, quantity, metric_unit, petitioner):

        self.__supplies.append(
            Supply(product, quantity, metric_unit, petitioner))

    def show_supply(self):

        for supply in self.__supplies:
            print(supply)
