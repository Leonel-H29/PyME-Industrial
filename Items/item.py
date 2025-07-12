from Items.item_state import ItemState


class Item:
    __name: str
    __metric_unit: str
    __quantity: int
    __petitioner: str
    __production_area: str
    __item_state: ItemState

    def __init__(self, name: str, metric_unit: str, quantity: int, petitioner: str, production_area: str, item_state: ItemState):
        self.__name = name
        self.__metric_unit = metric_unit
        self.__quantity = quantity
        self.__petitioner = petitioner
        self.__production_area = production_area
        self.__item_state = item_state
