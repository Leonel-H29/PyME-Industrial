from Items.states.item_state import ItemState


class ItemStateCanceled(ItemState):

    def quote(self, item):
        raise Exception("El item ya ha sido cancelado")

    def order(self, item):
        raise Exception("El item ya ha sido cancelado")

    def transport(self, item):
        raise Exception("El item ya ha sido cancelado")

    def receive(self, item):
        raise Exception("El item ya ha sido cancelado")

    def refund(self, item):
        raise Exception("El item ya ha sido cancelado")

    def cancel(self, item):
        raise Exception("El item ya ha sido cancelado")

    def __str__(self) -> str:
        return "CANCELADO"
