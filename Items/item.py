from Items.item_state import ItemState
from Items.item_state_required import ItemStateRequired
from Items.enums.metric_unit_enum import MetricUnitEnum


class Item:
    __product: str
    __metric_unit: MetricUnitEnum
    __quantity: int
    __petitioner: str
    __production_area: str
    __item_state: ItemState

    def __init__(self, product: str, metric_unit: MetricUnitEnum, quantity: int, petitioner: str, production_area: str):
        self.__product = product
        self.__metric_unit = metric_unit.value
        self.__quantity = quantity
        self.__petitioner = petitioner
        self.__production_area = production_area
        self.__item_state = ItemStateRequired()

    def __str__(self) -> str:
        return f"""
            - Item: {self.__product}
            - Cantidad: {self.__quantity}
            - UM: {self.__metric_unit}
            - Área de producción: {self.__production_area}
            - Solicitante: {self.__petitioner}
            - Estado: {self.__item_state}
        """

    def quote(self) -> None:
        self.__item_state.quote(self)

    def order(self) -> None:
        self.__item_state.order(self)

    def transport(self) -> None:
        self.__item_state.transport(self)

    def receive(self) -> None:
        self.__item_state.receive(self)

    def refund(self) -> None:
        self.__item_state.refund(self)

    def cancel(self) -> None:
        self.__item_state.cancel(self)

    def set_state(self, new_state: ItemState):
        self.__item_state = new_state

    def get_state(self):
        return self.__item_state
