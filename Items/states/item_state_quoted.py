from Items.states.item_state import ItemState
from Items.states.item_state_canceled import ItemStateCanceled
from Items.states.item_state_ordered import ItemStateOrdered


class ItemStateQuoted(ItemState):

    def quote(self, item):
        raise Exception("El item ya ha sido solicitado.")

    def order(self, item):
        item.set_state(ItemStateOrdered())
        print("Transición: Cotizando -> Ordenado")

    def transport(self, item):
        raise Exception("No se puede transportar en estado Cotizado.")

    def receive(self, item):
        raise Exception("No se puede recibir en estado Cotizado.")

    def refund(self, item):
        raise Exception("No se puede devolver en estado Cotizado.")

    def cancel(self, item):
        item.set_state(ItemStateCanceled())
        print("Transición: Cotizado -> Cancelado")

    def __str__(self) -> str:
        return "COTIZADO"
