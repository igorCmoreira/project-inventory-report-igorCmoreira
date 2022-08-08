import sys

from inventory_report.inventory.inventory_refactor import InventoryRefactor

from inventory_report.importer.xml_importer import XmlImporter
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter


def main():
    if len(sys.argv) < 3:
        return sys.stderr.write("Verifique os argumentos\n")
    path, tipo = sys.argv[1], sys.argv[2]
    if path.endswith(".csv"):
        print(InventoryRefactor(CsvImporter).import_data(path, tipo), end="")
    if path.endswith(".json"):
        print(InventoryRefactor(JsonImporter).import_data(path, tipo), end="")
    if path.endswith(".xml"):
        print(InventoryRefactor(XmlImporter).import_data(path, tipo), end="")
