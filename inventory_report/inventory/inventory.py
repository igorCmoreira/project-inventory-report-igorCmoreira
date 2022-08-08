import json
import csv
import xmltodict

from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    @staticmethod
    def import_data(path, tipo):
        with open(path) as inventario_de_produtos:
            if path.endswith("json"):
                retorno = json.load(inventario_de_produtos)
            if path.endswith("xml"):
                xmlR = inventario_de_produtos.read()
                retorno = xmltodict.parse(xmlR)["dataset"]["record"]
            if path.endswith("csv"):
                csvR = csv.DictReader(inventario_de_produtos)
                retorno = list(csvR)

            if tipo == "simples":
                return SimpleReport.generate(retorno)
            return CompleteReport.generate(retorno)
