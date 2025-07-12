from Items.item_state import ItemState
from Items.item_state_canceled import ItemStateCanceled
from Items.item_state_refund import ItemStateRefund


class ItemStateReceived(ItemState):

    def quote(self, item):
        raise Exception("El item ya ha sido solicitado.")

    def order(self, item):
        raise Exception("El item ya ha sido ordernado.")

    def transport(self, item):
        raise Exception("El item ya ha llegado a su destino.")

    def receive(self, item):
        raise Exception("El item ya ha sido entregado.")

    def refund(self, item):
        item.set_state(ItemStateRefund())
        print("Transición: Recibido -> Devuelto")

    def cancel(self, item):
        raise Exception("No se puede cancelar en estado Recibido.")

    def __str__(self) -> str:
        return "RECIBIDO"
