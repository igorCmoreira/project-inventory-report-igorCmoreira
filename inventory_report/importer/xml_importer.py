from inventory_report.importer.importer import Importer
import xmltodict


class XmlImporter(Importer):
    @staticmethod
    def import_data(path):
        if ".xml" not in path:
            raise ValueError("Arquivo inválido")
        with open(path, "r") as file:
            parse = dict(xmltodict.parse(file.read()))
            retorno = parse["dataset"]["record"]

        return retorno
