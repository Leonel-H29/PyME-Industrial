from User.user import User
from Items.enums.item_status_enum import ItemStatusEnum
from Factory_method.item_factory import ItemFactory


class BaseRepository:

    def __init__(self) -> None:
        self._item_factory = ItemFactory()

    def create_user(self, email: str) -> User:
        """
        Create a new user with the given email.
        """
        return User(email)

    def show_observers(self, item) -> None:
        """
        Print the list of observers for the given item.
        """
        print(f"** Observadores: ")
        for observer in item.get_observers():
            print(f"-- {observer}")
        print("\n")

    def _add_observer(self, item, email: str, db_instance, load_func) -> bool:
        """
        Add an observer to the item if they do not already exist.
        Update the database and reload data.
        """
        for observer in item.get_observers():
            if hasattr(observer, "get_email") and observer.get_email() == email:
                return False

        self.__add_user_as_observer(item, email)
        db_instance.update(item.get_code(), item, item.get_observers())
        load_func()
        return True

    def _remove_observer(self, item, email: str, db_instance, load_func) -> bool:
        """
        Remove an observer from the item if they exist.
        Update the database and reload data.
        """
        observers = item.get_observers()
        observer_to_remove = None
        for observer in observers:
            if hasattr(observer, "get_email") and observer.get_email() == email:
                observer_to_remove = observer
                break
        if observer_to_remove:
            item.remove(observer_to_remove)
            db_instance.update(item.get_code(), item, item.get_observers())
            load_func()
            return True
        return False

    def _add_item(self, item_type_enum, db_instance, item_list: list, item_args: list, user_emails: list[str], code=None, status=None) -> object:
        """
        Create a new item, add observers, and save it to the database.
        """
        item = self._item_factory.create_item(
            item_type_enum, *item_args, code, status)
        self.__add_users_as_observers(item, user_emails)
        item_list.append(item)
        db_instance.create(item, item.get_observers())
        return item

    def _load_items(self, item_type_enum, db_instance, item_list: list, field_map: list[str]) -> None:
        """
        Load items from the database and populate the item list.
        """
        item_list.clear()
        for item in db_instance.get():
            obj = self.__create_item_with_observers(
                item_type_enum, item, field_map)
            item_list.append(obj)

    def _get_item(self, item_type_enum, db_instance, code: str, field_map: list[str]) -> object:
        """
        Retrieve an item by its code from the database.
        """
        rows = db_instance.db.select(
            db_instance.TABLE_NAME, "code = ?", (code,))
        if not rows:
            return None
        data = dict(rows[0])
        return self.__create_item_with_observers(item_type_enum, data, field_map)

    def _update_item(self, code: str, new_status: str, get_by_code_func, load_func, db_instance) -> None:
        """
        Update the status of an item and refresh the data.
        """
        item = get_by_code_func(code)
        self.__change_item_status(item, new_status)
        db_instance.update(code, item, item.get_observers())
        load_func()

    def __change_item_status(self, item, new_status: str) -> None:
        """
        Change the status of an item using the appropriate method.
        """
        try:
            status_methods = {
                ItemStatusEnum.QUOTE: item.quote,
                ItemStatusEnum.ORDER: item.order,
                ItemStatusEnum.TRANSPORT: item.transport,
                ItemStatusEnum.RECEIVE: item.receive,
                ItemStatusEnum.REFUND: item.refund,
                ItemStatusEnum.CANCEL: item.cancel
            }
            status_enum = ItemStatusEnum(new_status)
            status_method = status_methods[status_enum]
            status_method()
        except KeyError:
            raise ValueError(f"Estado '{new_status}' no reconocido")
        except ValueError:
            raise ValueError(f"Estado '{new_status}' no es un estado válido")

    def __parse_subscribers(self, subscribers_str: str) -> list[str]:
        """
        Convert a comma-separated string of subscribers into a list.
        """
        return subscribers_str.split(",") if subscribers_str else []

    def __create_item_with_observers(self, item_type_enum, data: dict, field_map: list[str]) -> object:
        """
        Create an item with its observers from database data.
        """
        args = [data[field] for field in field_map]
        obj = self._item_factory.create_item(item_type_enum, *args)
        subscribers = self.__parse_subscribers(data.get('subscribers', ''))
        self.__add_users_as_observers(obj, subscribers)
        return obj

    def __add_user_as_observer(self, item, email: str) -> None:
        """
        Add a user as an observer to the item.
        """
        user = self.create_user(email)
        item.add(user)

    def __add_users_as_observers(self, item, emails: list[str]) -> None:
        """
        Add multiple users as observers to the item.
        """
        for email in emails:
            self.__add_user_as_observer(item, email)
