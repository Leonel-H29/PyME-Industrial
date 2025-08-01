from uuid import uuid4
from datetime import datetime
from Items.states.item_state import ItemState
from Items.states.item_state_required import ItemStateRequired
from Items.enums.metric_unit_enum import MetricUnitEnum
from Observer.subject import Subject
from Items.states.item_state_required import ItemStateRequired
from Items.states.item_state_quoted import ItemStateQuoted
from Items.states.item_state_ordered import ItemStateOrdered
from Items.states.item_state_transported import ItemStateTransported
from Items.states.item_state_received import ItemStateReceived
from Items.states.item_state_refunded import ItemStateRefunded
from Items.states.item_state_canceled import ItemStateCanceled


class Item(Subject):
    __created: datetime
    __last_updated: datetime
    __item_state: ItemState
    __petitioner: str
    __code: str

    def __init__(self, petitioner: str, code: str | None = None, state: str = None):
        super().__init__()
        self.__code = self.__validate_code(code)
        self.__created = datetime.now()
        self.__last_updated = self.__created
        self.__item_state = self._get_state_instance(state_name=state)
        self.__petitioner = petitioner

    def __str__(self) -> str:
        return (
            f"- Código: {self.__code}\n"
            f"- Creado: {self.__created.strftime('%d/%m/%Y %H:%M:%S')}\n"
            f"- Última actualización: {self.__last_updated.strftime('%d/%m/%Y %H:%M:%S')}\n"
            f"- Solicitante: {self.__petitioner}\n"
            f"- Estado: {self.__item_state}\n"
        )

    @staticmethod
    def _get_state_instance(state_name: str):

        try:
            if state_name is None:
                return ItemStateRequired()
            mapping = {
                "SOLICITADO": ItemStateRequired,
                "COTIZADO": ItemStateQuoted,
                "ORDENADO": ItemStateOrdered,
                "TRANSPORTADO": ItemStateTransported,
                "RECIBIDO": ItemStateReceived,
                "REEMBOLSADO": ItemStateRefunded,
                "CANCELADO": ItemStateCanceled,
            }
            return mapping[state_name.upper()]()
        except KeyError:
            raise ValueError(f"Estado '{state_name}' no reconocido")

    def __update_timestamp(self):
        self.__last_updated = datetime.now()

    def __validate_code(self, code):
        return code if code else uuid4().hex[:10]

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

    def get_code(self):
        return self.__code
