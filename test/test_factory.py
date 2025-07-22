import pytest
from Factory_method.supply_factory import SupplyFactory
from Factory_method.third_party_services_factory import ThirdPartyServicesFactory
from Items.supply import Supply
from Items.third_party_service import ThirdPartyServices
from Items.enums.metric_unit_enum import MetricUnitEnum

def test_supply_factory_creates_supply():
    factory = SupplyFactory()
    product = "Chapa lisa"
    quantity = 10
    metric_unit = MetricUnitEnum.SQUARE_METER
    petitioner = "Juan"

    item = factory.create_item(product, quantity, metric_unit, petitioner)

    assert isinstance(item, Supply)
    assert item.product == product
    assert item.quantity == quantity
    assert item.metric_unit == metric_unit.value
    assert item.petitioner == petitioner

def test_third_party_services_factory_creates_service():
    factory = ThirdPartyServicesFactory()
    service = "Recolección de residuos"
    provider = "EcoService S.A."
    petitioner = "Juan"

    item = factory.create_item(service, provider, petitioner)

    assert isinstance(item, ThirdPartyServices)
    assert item.service == service
    assert item.provider == provider
    assert item.petitioner == petitioner
