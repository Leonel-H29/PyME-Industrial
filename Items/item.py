from Items.states.item_state import ItemState
from Items.states.item_state_required import ItemStateRequired
from Items.enums.metric_unit_enum import MetricUnitEnum
from Observer.subject import Subject


class Item(Subject):
    __product: str
    __metric_unit: MetricUnitEnum
    __quantity: int
    __petitioner: str
    __production_area: str
    __item_state: ItemState

    def __init__(self, product: str, metric_unit: MetricUnitEnum, quantity: int, petitioner: str, production_area: str):
        super().__init__()
        self.__product = product
        self.__metric_unit = self.__validate_metric_unit(metric_unit)
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

    def __validate_metric_unit(self, metric_unit) -> str:
        if not isinstance(metric_unit, (MetricUnitEnum, str)):
            raise TypeError(
                f"Tipo inválido para unidad métrica: {type(metric_unit)}. Debe ser str o MetricUnitEnum.")

        if isinstance(metric_unit, MetricUnitEnum):
            return metric_unit.value

        try:
            enum_value = MetricUnitEnum(metric_unit)
            return enum_value.value
        except ValueError:
            valid_units = [e.value for e in MetricUnitEnum]
            raise ValueError(
                f"Unidad métrica inválida: {metric_unit}. Debe ser una de {valid_units}.")

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
        self.notify(self, f"El estado del item cambió a {self.get_state()}")

    def get_state(self):
        return self.__item_state
