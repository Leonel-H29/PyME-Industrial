import pytest
from Items.supply import Supply
from Items.states.item_state_required import ItemStateRequired
from Items.states.item_state_quoted import ItemStateQuoted
from Items.states.item_state_ordered import ItemStateOrdered
from Items.states.item_state_transported import ItemStateTransported
from Items.states.item_state_received import ItemStateReceived
from Items.states.item_state_canceled import ItemStateCanceled
from Items.states.item_state_refunded import ItemStateRefunded
from Items.enums.metric_unit_enum import MetricUnitEnum


@pytest.fixture
def supply():
    # return Supply(product="Acero", quantity=10, metric_unit="kg", petitioner="Juan")
    return Supply(product="Acero", quantity=10, metric_unit=MetricUnitEnum.SQUARE_METER, petitioner="Juan")


def test_creation_supply(supply):
    assert isinstance(supply.get_state(), ItemStateRequired)


def test_valid_transitions(supply):
    # Solicitado -> Cotizando
    supply.quote()
    assert isinstance(supply.get_state(), ItemStateQuoted)
    # Cotizando -> Ordenado
    supply.order()
    assert isinstance(supply.get_state(), ItemStateOrdered)
    # Ordenado -> Transportando
    supply.transport()
    assert isinstance(supply.get_state(), ItemStateTransported)
    # Transportando -> Recibido
    supply.receive()
    assert isinstance(supply.get_state(), ItemStateReceived)
    # Recibido -> Devuelto
    supply.refund()
    assert isinstance(supply.get_state(), ItemStateRefunded)


def test_cancel_in_requested(supply):
    supply.cancel()
    assert isinstance(supply.get_state(), ItemStateCanceled)


def test_cancel_in_quoted(supply):
    supply.quote()
    supply.cancel()
    assert isinstance(supply.get_state(), ItemStateCanceled)


def test_cancel_in_ordered(supply):
    supply.quote()
    supply.order()
    supply.cancel()
    assert isinstance(supply.get_state(), ItemStateCanceled)


@pytest.mark.parametrize("action", [
    lambda item: item.order(),
    lambda item: item.transport(),
    lambda item: item.receive(),
    lambda item: item.refund(),
])
def test_invalid_transitions_in_requested(supply, action):
    with pytest.raises(Exception):
        action(supply)


def test_invalid_transitions_in_quoted(supply):
    supply.quote()
    with pytest.raises(Exception):
        supply.quote()
    with pytest.raises(Exception):
        supply.transport()
    with pytest.raises(Exception):
        supply.receive()
    with pytest.raises(Exception):
        supply.refund()


def test_invalid_transitions_in_ordered(supply):
    supply.quote()
    supply.order()
    with pytest.raises(Exception):
        supply.quote()
    with pytest.raises(Exception):
        supply.order()
    with pytest.raises(Exception):
        supply.receive()
    with pytest.raises(Exception):
        supply.refund()


def test_invalid_transitions_in_transporting(supply):
    supply.quote()
    supply.order()
    supply.transport()
    with pytest.raises(Exception):
        supply.quote()
    with pytest.raises(Exception):
        supply.order()
    with pytest.raises(Exception):
        supply.transport()
    with pytest.raises(Exception):
        supply.refund()
    with pytest.raises(Exception):
        supply.cancel()


def test_invalid_transitions_in_received(supply):
    supply.quote()
    supply.order()
    supply.transport()
    supply.receive()
    with pytest.raises(Exception):
        supply.quote()
    with pytest.raises(Exception):
        supply.order()
    with pytest.raises(Exception):
        supply.transport()
    with pytest.raises(Exception):
        supply.receive()
    with pytest.raises(Exception):
        supply.cancel()


def test_no_transitions_in_canceled(supply):
    supply.cancel()
    for action in [supply.quote, supply.order, supply.transport, supply.receive, supply.refund, supply.cancel]:
        with pytest.raises(Exception):
            action()


def test_no_transitions_in_refunded(supply):
    supply.quote()
    supply.order()
    supply.transport()
    supply.receive()
    supply.refund()
    for action in [supply.quote, supply.order, supply.transport, supply.receive, supply.refund, supply.cancel]:
        with pytest.raises(Exception):
            action()
