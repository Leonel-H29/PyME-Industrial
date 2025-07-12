from Items.item_state import ItemState
from Items.item_state_quoted import ItemStateQuoted
from Items.item_state_canceled import ItemStateCanceled


class ItemStateRequired(ItemState):

    def quote(self, item):
        item.set_state(ItemStateQuoted())
        print("Transición: Solicitado -> Cotizando")

    def order(self, item):
        raise Exception("No se puede ordenar sin cotizar primero.")

    def transport(self, item):
        raise Exception("No se puede transportar en estado Solicitado.")

    def receive(self, item):
        raise Exception("No se puede recibir en estado Solicitado.")

    def refund(self, item):
        raise Exception("No se puede devolver en estado Solicitado.")

    def cancel(self, item):
        item.set_state(ItemStateCanceled())
        print("Transición: Solicitado -> Cancelado")

    def __str__(self) -> str:
        return "SOLICITADO"
