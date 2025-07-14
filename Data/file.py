from __future__ import annotations
import csv
import os


class File:
    _instance: File = None  

    def __new__(cls, path: str = ""):
        if cls._instance is None:
            cls._instance = super(File, cls).__new__(cls)
            cls._instance.path = os.path.abspath(path)
            cls._instance._file_handle = None
        return cls._instance

    def itemsFromFile(self):
        items = []
        try:
            with open(self.path, mode='r', newline='', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    items.append(row)
        except FileNotFoundError:
            print(f"Archivo no encontrado: {self.path}")
        return items

    def open(self):
        try:
            self._file_handle = open(self.path, mode='r', newline='', encoding='utf-8')
            print("Archivo abierto.")
        except FileNotFoundError:
            print("Archivo no encontrado.")

    def close(self):
        if self._file_handle:
            self._file_handle.close()
            print("Archivo cerrado.")
            self._file_handle = None

    def get_path(self):
        return self.path

    def set_path(self, path: str):
        self.path = path
