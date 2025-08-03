from Items.states.item_state import ItemState


class ItemStateCanceled(ItemState):

    def __str__(self) -> str:
        return "CANCELADO"
