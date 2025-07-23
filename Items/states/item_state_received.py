from Items.states.item_state import ItemState
from Items.states.item_state_canceled import ItemStateCanceled
from Items.states.item_state_refund import ItemStateRefund


class ItemStateReceived(ItemState):

    def refund(self, item):
        item.set_state(ItemStateRefund())
        print("Transición: Recibido -> Devuelto")

    def __str__(self) -> str:
        return "RECIBIDO"
