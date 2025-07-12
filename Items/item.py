from Items.item_state import ItemState
from Items.item_state_required import ItemStateRequired


class Item:
    __name: str
    __metric_unit: str
    __quantity: int
    __petitioner: str
    __production_area: str
    __item_state: ItemState

    def __init__(self, name: str, metric_unit: str, quantity: int, petitioner: str, production_area: str):
        self.__name = name
        self.__metric_unit = metric_unit
        self.__quantity = quantity
        self.__petitioner = petitioner
        self.__production_area = production_area
        self.__item_state = ItemStateRequired()

    def __str__(self) -> str:
        return f"""
            - Item: {self.__name}
            - Cantidad: {self.__quantity}
            - UM: {self.__metric_unit}
            - Área de producción: {self.__production_area}
            - Solicitante: {self.__petitioner}
            - Estado: {self.getStatus()}
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

    def getStatus(self) -> str:
        return self.__item_state.getStatus()
