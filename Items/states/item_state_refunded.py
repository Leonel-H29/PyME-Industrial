from Items.states.item_state import ItemState


class ItemStateRefunded(ItemState):

    def __str__(self) -> str:
        return "DEVUELTO"
