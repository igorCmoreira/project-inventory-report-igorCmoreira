from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport

from collections.abc import Iterable
from inventory_report.inventory.inventory_iterator import InventoryIterator


class InventoryRefactor(Iterable):
    def __init__(self, importe):
        self.importer = importe
        self.data = []

    def __iter__(self):
        return InventoryIterator(self.data)

    def import_from_data_file(self, path):
        self.data.extend(self.importer.import_data(path))

    def import_data(self, path, tipo):
        self.import_from_data_file(path)
        if tipo == "simples":
            return SimpleReport.generate(self.data)
        return CompleteReport.generate(self.data)
