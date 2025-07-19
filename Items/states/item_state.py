from abc import ABC, abstractmethod


class ItemState(ABC):
    @abstractmethod
    def quote(self, item) -> None: pass

    @abstractmethod
    def order(self, item) -> None: pass

    @abstractmethod
    def transport(self, item) -> None: pass

    @abstractmethod
    def receive(self, item) -> None: pass

    @abstractmethod
    def refund(self, item) -> None: pass

    @abstractmethod
    def cancel(self, item) -> None: pass

    @abstractmethod
    def __str__(self) -> str: pass
