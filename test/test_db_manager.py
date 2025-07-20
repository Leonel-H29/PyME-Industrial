import pytest
from db.DBManager import DBManager


def test_singleton_db_manager():
    db1 = DBManager("test_database_1.db")
    db2 = DBManager("test_database_2.db")
    assert db1 is db2, "DBManager no cumple el patrón Singleton"


def test_db_connection():
    db = DBManager("database.db")
    assert db.conn is not None, "La conexión a la base de datos no se inicializó correctamente"
