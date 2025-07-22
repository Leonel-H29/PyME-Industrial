from Factory_method.item_factory import ItemFactory
from Items.third_party_service import ThirdPartyServices

class ThirdPartyServicesFactory(ItemFactory):
    def create_item(self, service: str, provider: str, petitioner: str)-> ThirdPartyServices:
        return ThirdPartyServices(service, provider, petitioner)