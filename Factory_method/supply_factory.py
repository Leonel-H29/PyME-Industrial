from Factory_method.item_factory import ItemFactory
from Items.supply import Supply

class SupplyFactory(ItemFactory):
    def create_item(self, product: str, quantity: int, metric_unit, petitioner: str)-> Supply:
        return Supply(product, quantity, metric_unit, petitioner)