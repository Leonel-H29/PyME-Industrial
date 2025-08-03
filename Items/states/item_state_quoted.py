from Items.states.item_state import ItemState
from Items.states.item_state_canceled import ItemStateCanceled
from Items.states.item_state_ordered import ItemStateOrdered


class ItemStateQuoted(ItemState):

    def order(self, item):
        item.set_state(ItemStateOrdered())
        print("Transición: Cotizando -> Ordenado")

    def cancel(self, item):
        item.set_state(ItemStateCanceled())
        print("Transición: Cotizado -> Cancelado")

    def __str__(self) -> str:
        return "COTIZADO"
