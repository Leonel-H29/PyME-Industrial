from Items.states.item_state import ItemState
from Items.states.item_state_received import ItemStateReceived


class ItemStateTransported(ItemState):

    def receive(self, item):
        item.set_state(ItemStateReceived())
        print("Transición: Transportando -> Recibidoo")

    def __str__(self) -> str:
        return "TRANSPORTADO"
