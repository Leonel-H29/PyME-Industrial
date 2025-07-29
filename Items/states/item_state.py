from abc import abstractmethod


class ItemState:

    def quote(self, item) -> None:
        raise Exception("No se puede cotizar desde este estado.")

    def order(self, item) -> None:
        raise Exception("No se puede ordenar desde este estado.")

    def transport(self, item) -> None:
        raise Exception("No se puede cancelar desde este estado.")

    def receive(self, item) -> None:
        raise Exception("No se puede transportar desde este estado.")

    def refund(self, item) -> None:
        raise Exception("No se puede recibir desde este estado.")

    def cancel(self, item) -> None:
        raise Exception("No se puede devolver desde este estado.")

    @abstractmethod
    def __str__(self) -> str: pass
