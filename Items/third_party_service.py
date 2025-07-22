from Items.item import Item


class ThirdPartyServices(Item):
    def __init__(self, service: str, provider: str, petitioner: str):
        super().__init__(petitioner)
        self.__service = service
        self.__provider = provider

    @property
    def service(self):
        return self.__service

    @property
    def provider(self):
        return self.__provider

    @property
    def petitioner(self):
        return super().petitioner


    def __str__(self) -> str:
        base = super().__str__()
        return (
            f"- Servicio: {self.__service}\n"
            f"- Proveedor: {self.__provider}\n"
            f"{base}\n"
        )