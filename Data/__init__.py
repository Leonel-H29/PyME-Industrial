import sys
import os

# Agregar la raíz del proyecto al path para importar File
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from Data.file import File

def test_itemsFromFile():
    print("Mostrando el contenido del archivo")
    file = File("csv/items.csv")
    items = file.itemsFromFile()
    print(f"Se leyeron {len(items)} filas")
    for i, item in enumerate(items):
        print(f"Fila {i+1}: {item}")

def test_open_close():
    print("\n")
    file = File("csv/items.csv")
    file.open()
    print(f"Archivo abierto, file_handle: {file._file_handle}")
    file.close()
    print(f"Archivo cerrado, file_handle: {file._file_handle}")

def test_get_set_path():
    print("\n")
    file = File("csv/items.csv")
    print(f"Ruta original: {file.get_path()}")
    nueva_ruta = os.path.abspath("csv/items.csv")
    file.set_path(nueva_ruta)
    print(f"Ruta actualizada: {file.get_path()}")

def run_all_tests():
    test_itemsFromFile()
    test_open_close()
    test_get_set_path()

if __name__ == "__main__":
    run_all_tests()
