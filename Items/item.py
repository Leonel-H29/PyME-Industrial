from datetime import datetime
from Items.states.item_state import ItemState
from Items.states.item_state_required import ItemStateRequired
from Items.enums.metric_unit_enum import MetricUnitEnum
from Observer.subject import Subject


class Item(Subject):
    __created: datetime
    __last_updated: datetime
    __item_state: ItemState
    __petitioner: str

    def __init__(self, petitioner: str):
        super().__init__()
        self.__created = datetime.now()
        self.__last_updated = self.__created
        self.__item_state = ItemStateRequired()
        self.__petitioner = petitioner

    def __str__(self) -> str:
        return (
            f"- Creado: {self.__created.strftime('%d/%m/%Y %H:%M:%S')}\n"
            f"- Última actualización: {self.__last_updated.strftime('%d/%m/%Y %H:%M:%S')}\n"
            f"- Solicitante: {self.__petitioner}\n"
            f"- Estado: {self.__item_state}"
        )

    @staticmethod
    def _validate_metric_unit(metric_unit) -> str:
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

    def __update_timestamp(self):
        self.__last_updated = datetime.now()

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
        self.__update_timestamp()
        self.notify(self, f"El estado del item cambió a {self.get_state()}")

    def get_state(self):
        return self.__item_state

    def get_petitioner(self):
        return self.__petitioner
