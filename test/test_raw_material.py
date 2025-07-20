import pytest
from Items.raw_material import RawMaterial
from Items.states.item_state_required import ItemStateRequired
from Items.states.item_state_quoted import ItemStateQuoted
from Items.states.item_state_ordered import ItemStateOrdered
from Items.states.item_state_transported import ItemStateTransported
from Items.states.item_state_received import ItemStateReceived
from Items.states.item_state_canceled import ItemStateCanceled
from Items.states.item_state_refund import ItemStateRefund
from Items.enums.metric_unit_enum import MetricUnitEnum


@pytest.fixture
def raw_material():
    # return RawMaterial(product="Acero", quantity=10, metric_unit="kg", petitioner="Juan")
    return RawMaterial(product="Acero", quantity=10, metric_unit=MetricUnitEnum.SQUARE_METER, petitioner="Juan")


def test_creation_raw_material(raw_material):
    assert isinstance(raw_material.get_state(), ItemStateRequired)


def test_valid_transitions(raw_material):
    # Solicitado -> Cotizando
    raw_material.quote()
    assert isinstance(raw_material.get_state(), ItemStateQuoted)
    # Cotizando -> Ordenado
    raw_material.order()
    assert isinstance(raw_material.get_state(), ItemStateOrdered)
    # Ordenado -> Transportando
    raw_material.transport()
    assert isinstance(raw_material.get_state(), ItemStateTransported)
    # Transportando -> Recibido
    raw_material.receive()
    assert isinstance(raw_material.get_state(), ItemStateReceived)
    # Recibido -> Devuelto
    raw_material.refund()
    assert isinstance(raw_material.get_state(), ItemStateRefund)


def test_cancel_in_requested(raw_material):
    raw_material.cancel()
    assert isinstance(raw_material.get_state(), ItemStateCanceled)


def test_cancel_in_quoted(raw_material):
    raw_material.quote()
    raw_material.cancel()
    assert isinstance(raw_material.get_state(), ItemStateCanceled)


def test_cancel_in_ordered(raw_material):
    raw_material.quote()
    raw_material.order()
    raw_material.cancel()
    assert isinstance(raw_material.get_state(), ItemStateCanceled)


@pytest.mark.parametrize("action", [
    lambda item: item.order(),
    lambda item: item.transport(),
    lambda item: item.receive(),
    lambda item: item.refund(),
])
def test_invalid_transitions_in_requested(raw_material, action):
    with pytest.raises(Exception):
        action(raw_material)


def test_invalid_transitions_in_quoted(raw_material):
    raw_material.quote()
    with pytest.raises(Exception):
        raw_material.quote()
    with pytest.raises(Exception):
        raw_material.transport()
    with pytest.raises(Exception):
        raw_material.receive()
    with pytest.raises(Exception):
        raw_material.refund()


def test_invalid_transitions_in_ordered(raw_material):
    raw_material.quote()
    raw_material.order()
    with pytest.raises(Exception):
        raw_material.quote()
    with pytest.raises(Exception):
        raw_material.order()
    with pytest.raises(Exception):
        raw_material.receive()
    with pytest.raises(Exception):
        raw_material.refund()


def test_invalid_transitions_in_transporting(raw_material):
    raw_material.quote()
    raw_material.order()
    raw_material.transport()
    with pytest.raises(Exception):
        raw_material.quote()
    with pytest.raises(Exception):
        raw_material.order()
    with pytest.raises(Exception):
        raw_material.transport()
    with pytest.raises(Exception):
        raw_material.refund()
    with pytest.raises(Exception):
        raw_material.cancel()


def test_invalid_transitions_in_received(raw_material):
    raw_material.quote()
    raw_material.order()
    raw_material.transport()
    raw_material.receive()
    with pytest.raises(Exception):
        raw_material.quote()
    with pytest.raises(Exception):
        raw_material.order()
    with pytest.raises(Exception):
        raw_material.transport()
    with pytest.raises(Exception):
        raw_material.receive()
    with pytest.raises(Exception):
        raw_material.cancel()


def test_no_transitions_in_canceled(raw_material):
    raw_material.cancel()
    for action in [raw_material.quote, raw_material.order, raw_material.transport, raw_material.receive, raw_material.refund, raw_material.cancel]:
        with pytest.raises(Exception):
            action()


def test_no_transitions_in_refunded(raw_material):
    raw_material.quote()
    raw_material.order()
    raw_material.transport()
    raw_material.receive()
    raw_material.refund()
    for action in [raw_material.quote, raw_material.order, raw_material.transport, raw_material.receive, raw_material.refund, raw_material.cancel]:
        with pytest.raises(Exception):
            action()
