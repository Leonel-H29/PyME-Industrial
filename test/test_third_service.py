import pytest
from Items.third_party_service import ThirdPartyServices
from Items.states.item_state_required import ItemStateRequired
from Items.states.item_state_quoted import ItemStateQuoted
from Items.states.item_state_ordered import ItemStateOrdered
from Items.states.item_state_transported import ItemStateTransported
from Items.states.item_state_received import ItemStateReceived
from Items.states.item_state_canceled import ItemStateCanceled
from Items.states.item_state_refunded import ItemStateRefunded
from Items.enums.metric_unit_enum import MetricUnitEnum


@pytest.fixture
def third_party_service():
    return ThirdPartyServices(service="Servicio de Mantenimiento", provider='Kousal S.A.', petitioner="Juan")


def test_creation_third_party_service(third_party_service):
    assert isinstance(third_party_service.get_state(), ItemStateRequired)


def test_valid_transitions(third_party_service):
    # Solicitado -> Cotizando
    third_party_service.quote()
    assert isinstance(third_party_service.get_state(), ItemStateQuoted)
    # Cotizando -> Ordenado
    third_party_service.order()
    assert isinstance(third_party_service.get_state(), ItemStateOrdered)
    # Ordenado -> Transportando
    third_party_service.transport()
    assert isinstance(third_party_service.get_state(), ItemStateTransported)
    # Transportando -> Recibido
    third_party_service.receive()
    assert isinstance(third_party_service.get_state(), ItemStateReceived)
    # Recibido -> Devuelto
    third_party_service.refund()
    assert isinstance(third_party_service.get_state(), ItemStateRefunded)


def test_cancel_in_requested(third_party_service):
    third_party_service.cancel()
    assert isinstance(third_party_service.get_state(), ItemStateCanceled)


def test_cancel_in_quoted(third_party_service):
    third_party_service.quote()
    third_party_service.cancel()
    assert isinstance(third_party_service.get_state(), ItemStateCanceled)


def test_cancel_in_ordered(third_party_service):
    third_party_service.quote()
    third_party_service.order()
    third_party_service.cancel()
    assert isinstance(third_party_service.get_state(), ItemStateCanceled)


@pytest.mark.parametrize("action", [
    lambda item: item.order(),
    lambda item: item.transport(),
    lambda item: item.receive(),
    lambda item: item.refund(),
])
def test_invalid_transitions_in_requested(third_party_service, action):
    with pytest.raises(Exception):
        action(third_party_service)


def test_invalid_transitions_in_quoted(third_party_service):
    third_party_service.quote()
    with pytest.raises(Exception):
        third_party_service.quote()
    with pytest.raises(Exception):
        third_party_service.transport()
    with pytest.raises(Exception):
        third_party_service.receive()
    with pytest.raises(Exception):
        third_party_service.refund()


def test_invalid_transitions_in_ordered(third_party_service):
    third_party_service.quote()
    third_party_service.order()
    with pytest.raises(Exception):
        third_party_service.quote()
    with pytest.raises(Exception):
        third_party_service.order()
    with pytest.raises(Exception):
        third_party_service.receive()
    with pytest.raises(Exception):
        third_party_service.refund()


def test_invalid_transitions_in_transporting(third_party_service):
    third_party_service.quote()
    third_party_service.order()
    third_party_service.transport()
    with pytest.raises(Exception):
        third_party_service.quote()
    with pytest.raises(Exception):
        third_party_service.order()
    with pytest.raises(Exception):
        third_party_service.transport()
    with pytest.raises(Exception):
        third_party_service.refund()
    with pytest.raises(Exception):
        third_party_service.cancel()


def test_invalid_transitions_in_received(third_party_service):
    third_party_service.quote()
    third_party_service.order()
    third_party_service.transport()
    third_party_service.receive()
    with pytest.raises(Exception):
        third_party_service.quote()
    with pytest.raises(Exception):
        third_party_service.order()
    with pytest.raises(Exception):
        third_party_service.transport()
    with pytest.raises(Exception):
        third_party_service.receive()
    with pytest.raises(Exception):
        third_party_service.cancel()


def test_no_transitions_in_canceled(third_party_service):
    third_party_service.cancel()
    for action in [third_party_service.quote, third_party_service.order, third_party_service.transport, third_party_service.receive, third_party_service.refund, third_party_service.cancel]:
        with pytest.raises(Exception):
            action()


def test_no_transitions_in_refunded(third_party_service):
    third_party_service.quote()
    third_party_service.order()
    third_party_service.transport()
    third_party_service.receive()
    third_party_service.refund()
    for action in [third_party_service.quote, third_party_service.order, third_party_service.transport, third_party_service.receive, third_party_service.refund, third_party_service.cancel]:
        with pytest.raises(Exception):
            action()
