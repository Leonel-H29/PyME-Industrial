import pytest
from Items.item import Item
from Observer.observer import Observer
from User.user import User


class MockUser(User):
    def __init__(self, email):
        super().__init__(email)
        self.notifications = []

    def update(self, item, message):
        self.notifications.append((item, message))


@pytest.fixture
def item():
    return Item(petitioner="Juan")


@pytest.fixture
def user():
    return MockUser(email="test@example.com")


@pytest.fixture
def user2():
    return MockUser(email="test2@example.com")


def test_single_observer_notified_on_state_change(item, user):
    item.add(user)
    item.quote()
    assert len(user.notifications) == 1
    assert "El estado del item cambió" in user.notifications[0][1]


def test_multiple_observers_notified(item, user, user2):
    item.add(user)
    item.add(user2)
    item.quote()
    assert len(user.notifications) == 1
    assert len(user2.notifications) == 1


def test_remove_observer_no_notification(item, user):
    item.add(user)
    item.remove(user)
    item.quote()
    assert len(user.notifications) == 0


def test_observer_notified_on_all_state_changes(item, user):
    item.add(user)
    item.quote()
    item.order()
    item.transport()
    item.receive()
    item.refund()
    assert len(user.notifications) == 5  # One message for each state change


def test_no_observers_no_error(item):
    # Should not throw exception even if there are no observers
    item.quote()
    item.order()


def test_add_same_observer_twice(item, user):
    item.add(user)
    item.add(user)
    item.quote()
    # Depending on the implementation, this can be either 1 or 2. If duplicates are not allowed, it must be 1.
    assert len(user.notifications) == 1


def test_remove_nonexistent_observer(item, user):
    # Should not throw exception
    item.remove(user)
    item.quote()  # No observers, must not fail


def test_observer_raises_exception(item):
    class FailingObserver(Observer):
        def update(self, item, message):
            raise Exception("Error en observer")
    user = MockUser(email="ok@example.com")
    failing = FailingObserver()
    item.add(user)
    item.add(failing)
    # The observer that fails should not affect the others
    item.quote()
    assert len(user.notifications) == 1
