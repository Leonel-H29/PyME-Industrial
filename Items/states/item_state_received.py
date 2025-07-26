from Items.states.item_state import ItemState
from Items.states.item_state_refunded import ItemStateRefunded


class ItemStateReceived(ItemState):

    def refund(self, item):
        item.set_state(ItemStateRefunded())
        print("Transición: Recibido -> Devuelto")

    def __str__(self) -> str:
        return "RECIBIDO"
