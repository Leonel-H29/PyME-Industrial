from abc import ABC, abstractclassmethod


class ItemState(ABC):
    @abstractclassmethod
    def quote() -> None:
        pass

    @abstractclassmethod
    def order() -> None:
        pass

    @abstractclassmethod
    def transport() -> None:
        pass

    @abstractclassmethod
    def refund() -> None:
        pass

    @abstractclassmethod
    def cancel() -> None:
        pass
