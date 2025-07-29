from Items.states.item_state import ItemState
from Items.states.item_state_canceled import ItemStateCanceled
from Items.states.item_state_transported import ItemStateTransported


class ItemStateOrdered(ItemState):

    def transport(self, item):
        item.set_state(ItemStateTransported())
        print("Transición: Ordenado -> Transportando")

    def cancel(self, item):
        item.set_state(ItemStateCanceled())
        print("Transición: Ordenado -> Cancelado")

    def __str__(self) -> str:
        return "ORDENADO"
