from Items.item_state import ItemState


class ItemStateRefund(ItemState):
    def quote(self, item):
        raise Exception("El item ya ha sido devuelto")

    def order(self, item):
        raise Exception("El item ya ha sido devuelto")

    def transport(self, item):
        raise Exception("El item ya ha sido devuelto")

    def receive(self, item):
        raise Exception("El item ya ha sido devuelto")

    def refund(self, item):
        raise Exception("El item ya ha sido devuelto")

    def cancel(self, item):
        raise Exception("El item ya ha sido devuelto")

    def getStatus(self) -> str:
        return "DEVUELTO"
