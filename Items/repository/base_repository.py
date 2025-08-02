from User.user import User
from Items.enums.item_status_enum import ItemStatusEnum
from Factory_method.item_factory import ItemFactory


class BaseRepository:

    def __init__(self) -> None:
        self._item_factory = ItemFactory()

    def create_user(self, email: str):
        return User(email)

    def _change_item_status(self, item, new_status: str):
        try:
            status_methods = {
                ItemStatusEnum.QUOTE: item.quote,
                ItemStatusEnum.ORDER: item.order,
                ItemStatusEnum.TRANSPORT: item.transport,
                ItemStatusEnum.RECEIVE: item.receive,
                ItemStatusEnum.REFUND: item.refund,
                ItemStatusEnum.CANCEL: item.cancel
            }
            status_enum = ItemStatusEnum(new_status)
            status_method = status_methods[status_enum]
            status_method()
        except KeyError:
            raise ValueError(f"Estado '{new_status}' no reconocido")
        except ValueError:
            raise ValueError(f"Estado '{new_status}' no es un estado válido")
