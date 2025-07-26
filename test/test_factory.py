import pytest
from Factory_method.item_factory import ItemFactory
from Items.supply import Supply
from Items.third_party_service import ThirdPartyServices
from Items.enums.metric_unit_enum import MetricUnitEnum
from Items.enums.item_types_enum import ItemTypesEnum


def test_supply_factory_creates_supply():
    factory = ItemFactory()
    product = "Chapa lisa"
    quantity = 10
    metric_unit = MetricUnitEnum.SQUARE_METER
    petitioner = "Juan"

    item = factory.create_item(item_type=ItemTypesEnum.SUPPLY, product=product,
                               quantity=quantity, metric_unit=metric_unit, petitioner=petitioner)

    assert isinstance(item, Supply)
    assert item.get_product() == product
    assert item.get_quantity() == quantity
    assert item.get_metric_unit() == metric_unit.value
    assert item.get_petitioner() == petitioner


def test_third_party_services_factory_creates_service():
    factory = ItemFactory()
    service = "Recolección de residuos"
    provider = "EcoService S.A."
    petitioner = "Juan"

    item = factory.create_item(item_type=ItemTypesEnum.THIRD_PARTY_SERVICES,
                               service=service, provider=provider, petitioner=petitioner)

    assert isinstance(item, ThirdPartyServices)
    assert item.get_service() == service
    assert item.get_provider() == provider
    assert item.get_petitioner() == petitioner
