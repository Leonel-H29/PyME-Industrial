from Items.item_state import ItemState
from Items.item_state_canceled import ItemStateCanceled
from Items.item_state_transported import ItemStateTransported


class ItemStateOrdered(ItemState):
    def quote(self, item):
        raise Exception("El item ya ha sido solicitado.")

    def order(self, item):
        raise Exception("El item ya ha sido ordernado.")

    def transport(self, item):
        item.__item_state = ItemStateTransported()
        print("Transición: Ordenado -> Transportando")

    def receive(self, item):
        raise Exception("No se puede recibir en estado Ordenado.")

    def refund(self, item):
        raise Exception("No se puede devolver en estado Ordenado.")

    def cancel(self, item):
        item.__item_state = ItemStateCanceled()
        print("Transición: Solicitado -> Cancelado")

    def getStatus(self) -> str:
        return "ORDENADO"
