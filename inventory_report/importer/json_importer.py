from inventory_report.importer.importer import Importer
import json


class JsonImporter(Importer):
    @staticmethod
    def import_data(path):
        if ".json" not in path:
            raise ValueError("Arquivo inválido")
        with open(path, "r") as file:
            retorno = json.load(file)

        return retorno
