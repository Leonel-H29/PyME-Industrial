from Items.item_state import ItemState
from Items.item_state_received import ItemStateReceived


class ItemStateTransported(ItemState):
    def quote(self, item):
        raise Exception("El item ya ha sido solicitado.")

    def order(self, item):
        raise Exception("El item ya ha sido ordernado.")

    def transport(self, item):
        raise Exception("El item ya esta en camino.")

    def receive(self, item):
        item.__item_state = ItemStateReceived()
        print("Transición: Transportando -> Recibidoo")

    def refund(self, item):
        raise Exception("No se puede devolver en estado Transportando.")

    def cancel(self, item):
        raise Exception("No se puede cancelar en estado Transportando.")

    def getStatus(self) -> str:
        return "TRANSPORTADO"
