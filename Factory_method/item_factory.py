from Items.item import Item
from Items.supply import Supply
from Items.third_party_service import ThirdPartyServices
from Items.enums.item_types_enum import ItemTypesEnum
from Items.enums.item_status_enum import ItemStatusEnum


class ItemFactory:

    @staticmethod
    def create_item(item_type: str, *args, **kwargs) -> Item:
        if item_type == ItemTypesEnum.SUPPLY:
            return Supply(*args, **kwargs)
        elif item_type == ItemTypesEnum.THIRD_PARTY_SERVICES:
            return ThirdPartyServices(*args, **kwargs)
        else:
            raise ValueError(f"Item type '{item_type}' no reconocido")

    @staticmethod
    def change_item_status(item, new_status: str):
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
