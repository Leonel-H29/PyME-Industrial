from User.user import User
from Items.enums.item_status_enum import ItemStatusEnum
from Factory_method.item_factory import ItemFactory


class BaseRepository:

    def __init__(self) -> None:
        self._item_factory = ItemFactory()

    def create_user(self, email: str):
        return User(email)

    def show_observers(self, item):
        print(f"** Observadores: ")
        for observer in item.get_observers():
            print(f"-- {observer}")
        print("\n")

    def _add_observer(self, item, email, db_instance, load_func):
        # Check if that observer already exists
        for observer in item.get_observers():
            if hasattr(observer, "get_email") and observer.get_email() == email:
                return False

        user = self.create_user(email)
        item.add(user)
        db_instance.update(item.get_code(), item, item.get_observers())
        load_func()
        return True

    def _remove_observer(self, item, email, db_instance, load_func):
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

    def _add_item(self, item_type_enum, db_instance, item_list, item_args, user_emails, code=None, status=None):
        item = self._item_factory.create_item(
            item_type_enum, *item_args, code, status)
        for email in user_emails:
            user = self.create_user(email)
            item.add(user)
        item_list.append(item)
        db_instance.create(item, item.get_observers())
        return item

    def _load_items(self, item_type_enum, db_instance, item_list, field_map):
        item_list.clear()
        for item in db_instance.get():
            args = [item[field] for field in field_map]
            obj = self._item_factory.create_item(item_type_enum, *args)
            subscribers = item['subscribers'].split(
                ",") if item['subscribers'] else []
            for email in subscribers:
                obj.add(self.create_user(email))
            item_list.append(obj)

    def _get_item(self, item_type_enum, db_instance, code, field_map):
        rows = db_instance.db.select(
            db_instance.TABLE_NAME, "code = ?", (code,))
        if not rows:
            return None
        data = dict(rows[0])
        args = [data[field] for field in field_map]
        obj = self._item_factory.create_item(item_type_enum, *args)
        subscribers = data['subscribers'].split(
            ",") if data['subscribers'] else []
        for email in subscribers:
            obj.add(self.create_user(email))
        return obj

    def _update_item(self, code, new_status, get_by_code_func, load_func, db_instance):
        item = get_by_code_func(code)
        self.__change_item_status(item, new_status)
        db_instance.update(code, item, item.get_observers())
        load_func()

    def __change_item_status(self, item, new_status: str):
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
