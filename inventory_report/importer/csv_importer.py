from inventory_report.importer.importer import Importer
import csv


class CsvImporter(Importer):
    @staticmethod
    def import_data(path):
        if'.csv' not in path:
            raise ValueError('Tipo de arquivo invalido')
        with open(path, encoding="utf-8") as file:
            retorno = list(
                csv.DictReader(file, delimiter=",", quotechar='"')
            )

            return retorno
