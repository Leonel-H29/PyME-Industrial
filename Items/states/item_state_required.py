from Items.states.item_state import ItemState
from Items.states.item_state_quoted import ItemStateQuoted
from Items.states.item_state_canceled import ItemStateCanceled


class ItemStateRequired(ItemState):

    def quote(self, item):
        item.set_state(ItemStateQuoted())
        print("Transición: Solicitado -> Cotizando")

    def cancel(self, item):
        item.set_state(ItemStateCanceled())
        print("Transición: Solicitado -> Cancelado")

    def __str__(self) -> str:
        return "SOLICITADO"
