from __future__ import annotations
import csv


class File:
    __file: File

    def __init__(self, path: str = ""):
        self.path = path

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
            self.__file = open(self.path, mode='r',
                               newline='', encoding='utf-8')
            print("Archivo abierto.")
        except FileNotFoundError:
            print("Archivo no encontrado.")

    def close(self):
        if self.__file:
            self.__file.close()
            print("Archivo cerrado.")
            self.__file = None

    def get_path(self):
        return self.path

    def set_path(self, path: str):
        self.path = path
