from abc import abstractmethod


class ItemState:
    @abstractmethod
    def quote(self, item) -> None:
        raise Exception("No se puede cotizar desde este estado.")

    @abstractmethod
    def order(self, item) -> None:
        raise Exception("No se puede ordenar desde este estado.")

    @abstractmethod
    def transport(self, item) -> None:
        raise Exception("No se puede cancelar desde este estado.")

    @abstractmethod
    def receive(self, item) -> None:
        raise Exception("No se puede transportar desde este estado.")

    @abstractmethod
    def refund(self, item) -> None:
        raise Exception("No se puede recibir desde este estado.")

    @abstractmethod
    def cancel(self, item) -> None:
        raise Exception("No se puede devolver desde este estado.")

    @abstractmethod
    def __str__(self) -> str: pass
