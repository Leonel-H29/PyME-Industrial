from Items.item import Item
from Items.enums.metric_unit_enum import MetricUnitEnum


class Supply(Item):
    def __init__(self, product: str, quantity: int, metric_unit, petitioner: str, code: str = None):
        super().__init__(petitioner, code)
        self.__product = product
        self.__quantity = quantity
        self.__metric_unit = self.__validate_metric_unit(metric_unit)

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

    def get_product(self):
        return self.__product

    def get_quantity(self):
        return self.__quantity

    def get_metric_unit(self):
        return self.__metric_unit

    def __str__(self) -> str:
        base = super().__str__()
        return (
            f"- Producto: {self.__product}\n"
            f"- Cantidad: {self.__quantity}\n"
            f"- UM: {self.__metric_unit}\n"
            f"{base}\n"
        )
