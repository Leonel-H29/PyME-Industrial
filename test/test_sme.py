import pytest
from Items.repository.supply_repository import SupplyRepository
from Items.repository.third_party_service_repository import ThirdPartyServiceRepository
from Items.enums.metric_unit_enum import MetricUnitEnum
from Items.enums.item_types_enum import ItemTypesEnum
from Items.enums.item_status_enum import ItemStatusEnum

# Mock user emails for observer tests
USER_EMAILS = ["user1@example.com", "user2@example.com", "user3@example.com"]


@pytest.fixture
def supply_repo():
    repo = SupplyRepository()
    repo.load()
    return repo


@pytest.fixture
def tps_repo():
    repo = ThirdPartyServiceRepository()
    repo.load()
    return repo


def test_add_and_get_supply(supply_repo):
    item = supply_repo.add(
        "Steel", 100, MetricUnitEnum.MILLIMETER, "Alice", USER_EMAILS)
    fetched = supply_repo.get_by_code(item.get_code())
    assert fetched is not None
    assert fetched.get_product() == "Steel"
    assert set([u.get_email()
               for u in fetched.get_observers()]) == set(USER_EMAILS)


def test_add_duplicate_observer(supply_repo):
    item = supply_repo.add(
        "Copper", 50, MetricUnitEnum.MILLIMETER, "Bob", ["bob@example.com"])
    code = item.get_code()
    assert supply_repo.add_observer(
        code, "bob@example.com") is False  # Already observer


def test_remove_nonexistent_observer(supply_repo):
    item = supply_repo.add("Iron", 10, MetricUnitEnum.MILLIMETER, "Carol", [
                           "carol@example.com"])
    code = item.get_code()
    assert supply_repo.remove_observer(code, "notfound@example.com") is False


def test_invalid_status_update(supply_repo):
    item = supply_repo.add("Aluminum", 20, MetricUnitEnum.MILLIMETER, "Dave", [
                           "dave@example.com"])
    code = item.get_code()
    with pytest.raises(ValueError):
        supply_repo.update(code, "INVALID_STATUS")


def test_observer_notification_integrity(supply_repo):
    # Simulate observer that raises exception
    class FailingUser:
        def get_email(self): return "fail@example.com"
        def update(self, item, message): raise Exception("Observer failed")
    item = supply_repo.add(
        "Lead", 5, MetricUnitEnum.MILLIMETER, "Eve", ["eve@example.com"])
    item.add(FailingUser())
    # Should not break when updating status
    supply_repo.update(item.get_code(), ItemStatusEnum.QUOTE.value)


def test_bulk_add_and_remove_observers(supply_repo):
    item = supply_repo.add("Nickel", 30, MetricUnitEnum.MILLIMETER, "Frank", [
                           "frank@example.com"])
    code = item.get_code()
    # Add many observers
    for i in range(20):
        email = f"user{i}@example.com"
        assert supply_repo.add_observer(code, email) is True
    # Remove all observers
    for i in range(20):
        email = f"user{i}@example.com"
        assert supply_repo.remove_observer(code, email) is True


def test_concurrent_adds(supply_repo):
    import threading
    results = []

    def add_item():
        try:
            item = supply_repo.add("Zinc", 1, MetricUnitEnum.MILLIMETER, "Grace", [
                                   "grace@example.com"])
            results.append(item)
        except Exception as e:
            results.append(e)
    threads = [threading.Thread(target=add_item) for _ in range(10)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    assert all(isinstance(r, object) for r in results)


def test_data_integrity_after_multiple_operations(supply_repo):
    # Add, update, remove, and check data consistency
    item = supply_repo.add("Tin", 15, MetricUnitEnum.MILLIMETER, "Hank", [
                           "hank@example.com"])
    code = item.get_code()
    supply_repo.update(code, ItemStatusEnum.QUOTE.value)
    supply_repo.add_observer(code, "extra@example.com")
    supply_repo.remove_observer(code, "hank@example.com")
    fetched = supply_repo.get_by_code(code)
    assert fetched is not None
    assert "extra@example.com" in [u.get_email()
                                   for u in fetched.get_observers()]
    assert "hank@example.com" not in [u.get_email()
                                      for u in fetched.get_observers()]


def test_third_party_service_full_flow(tps_repo):
    item = tps_repo.add("Cleaning", "CleanCo", "Ivy", ["ivy@example.com"])
    code = item.get_code()
    tps_repo.update(code, ItemStatusEnum.QUOTE.value)
    tps_repo.update(code, ItemStatusEnum.ORDER.value)
    tps_repo.update(code, ItemStatusEnum.TRANSPORT.value)
    tps_repo.update(code, ItemStatusEnum.RECEIVE.value)
    tps_repo.update(code, ItemStatusEnum.REFUND.value)
    fetched = tps_repo.get_by_code(code)
    assert fetched.get_state().__class__.__name__ == "ItemStateRefunded"


def test_database_failure_handling(monkeypatch, supply_repo):
    # Simulate DB failure on update
    item = supply_repo.add("Gold", 1, MetricUnitEnum.MILLIMETER, "Jack", [
                           "jack@example.com"])
    code = item.get_code()
    def fail_update(*args, **kwargs): raise Exception("DB failure")
    monkeypatch.setattr(
        supply_repo._SupplyRepository__dbSupplies, "update", fail_update)
    with pytest.raises(Exception):
        supply_repo.update(code, ItemStatusEnum.QUOTE.value)
