import os
import pytest
from Data.file import File


@pytest.fixture
def test_csv(tmp_path):
    # It creates a temporary CSV file for testing
    file_path = tmp_path / "items.csv"
    with open(file_path, "w", encoding="utf-8", newline="") as f:
        f.write("col1,col2\nvalor1,valor2\nvalor3,valor4\n")
    return str(file_path)


def test_items_from_file(test_csv):
    file = File(test_csv)
    items = file.itemsFromFile()
    assert len(items) == 2
    assert items[0]["col1"] == "valor1"
    assert items[1]["col2"] == "valor4"


def test_open_close(test_csv):
    file = File(test_csv)
    file.open()
    assert file._file_handle is not None
    file.close()
    assert file._file_handle is None


def test_get_set_path(test_csv, tmp_path):
    file = File(test_csv)
    assert file.get_path() == os.path.abspath(test_csv)
    nueva_ruta = str(tmp_path / "nuevo.csv")
    file.set_path(nueva_ruta)
    assert file.get_path() == nueva_ruta


def test_singleton_file(test_csv, tmp_path):
    file1 = File(test_csv)
    file2 = File(str(tmp_path / "otro.csv"))
    assert file1 is file2, "File no cumple el patrón Singleton"
    # The path should be the last one set
    file2.set_path("nuevo_path.csv")
    assert file1.get_path() == "nuevo_path.csv"
    assert file2.get_path() == "nuevo_path.csv"
