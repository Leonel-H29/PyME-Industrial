from Items.item import Item
from Items.supply import Supply
from Items.third_party_service import ThirdPartyServices
from Items.enums.item_types_enum import ItemTypesEnum


class ItemFactory:

    @staticmethod
    def create_item(item_type: ItemTypesEnum, *args, **kwargs) -> Item:
        if item_type == ItemTypesEnum.SUPPLY:
            return Supply(*args, **kwargs)
        elif item_type == ItemTypesEnum.THIRD_PARTY_SERVICES:
            return ThirdPartyServices(*args, **kwargs)
        else:
            raise ValueError(f"Item type '{item_type}' no reconocido")
