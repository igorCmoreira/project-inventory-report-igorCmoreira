from inventory_report.importer.importer import Importer
import json


class jsonImporter(Importer):
    @staticmethod
    def import_data(path):
        if ".json" not in path:
            raise ValueError("Arquivo invalido")
        with open(path, "r") as file:
            retorno = json.load(file)

        return retorno
