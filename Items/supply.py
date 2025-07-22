from Items.item import Item


class Supply(Item):
    def __init__(self, product: str, quantity: int, metric_unit, petitioner: str):
        super().__init__(petitioner)
        self.__product = product
        self.__quantity = quantity
        self.__metric_unit = self._validate_metric_unit(metric_unit)

    @property
    def product(self):
        return self.__product

    @property
    def quantity(self):
        return self.__quantity

    @property
    def metric_unit(self):
        return self.__metric_unit
    @property
    def petitioner(self):
        return super().petitioner
    
    def __str__(self) -> str:
        base = super().__str__()
        return (
            f"- Producto: {self.__product}\n"
            f"- Cantidad: {self.__quantity}\n"
            f"- UM: {self.__metric_unit}\n"
            f"{base}\n"
        )