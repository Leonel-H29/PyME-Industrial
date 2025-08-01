from Items.item import Item


class ThirdPartyServices(Item):
    def __init__(self, service: str, provider: str, petitioner: str, code: str = None, state: str = None):
        super().__init__(petitioner, code, state)
        self.__service = service
        self.__provider = provider

    def get_service(self):
        return self.__service

    def get_provider(self):
        return self.__provider

    def __str__(self) -> str:
        base = super().__str__()
        return (
            f"- Servicio: {self.__service}\n"
            f"- Proveedor: {self.__provider}\n"
            f"{base}\n"
        )
