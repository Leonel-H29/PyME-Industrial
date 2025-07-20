import sqlite3
from sqlite3 import Connection
from threading import Lock


class DBManager:
    _instance = None
    _lock = Lock()

    def __new__(cls, db_path="database.db"):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super(DBManager, cls).__new__(cls)
                cls._instance._init_db(db_path)
        return cls._instance

    def _init_db(self, db_path):
        try:
            self.conn: Connection = sqlite3.connect(
                db_path, check_same_thread=False)
            self.conn.row_factory = sqlite3.Row
        except sqlite3.Error as e:
            print(f"Error al conectar a la base de datos: {e}")
            self.conn = None

    def execute(self, query, params=(), commit=False):
        if not self.conn:
            print("No hay conexión a la base de datos.")
            return None
        try:
            cursor = self.conn.cursor()
            cursor.execute(query, params)
            if commit:
                self.conn.commit()
            return cursor
        except sqlite3.Error as e:
            print(f"Error al ejecutar la consulta: {e}")
            return None

    def insert(self, table, data: dict):
        keys = ', '.join(data.keys())
        question_marks = ', '.join(['?'] * len(data))
        values = tuple(data.values())
        query = f"INSERT INTO {table} ({keys}) VALUES ({question_marks})"
        self.execute(query, values, commit=True)

    def select(self, table, where=None, params=()):
        query = f"SELECT * FROM {table}"
        if where:
            query += f" WHERE {where}"
        cursor = self.execute(query, params)
        return cursor.fetchall()

    def update(self, table, data: dict, where, params=()):
        set_clause = ', '.join([f"{k}=?" for k in data.keys()])
        values = tuple(data.values()) + params
        query = f"UPDATE {table} SET {set_clause} WHERE {where}"
        self.execute(query, values, commit=True)

    def delete(self, table, where, params=()):
        query = f"DELETE FROM {table} WHERE {where}"
        self.execute(query, params, commit=True)
