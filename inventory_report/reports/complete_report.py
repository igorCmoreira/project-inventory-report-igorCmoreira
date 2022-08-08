from inventory_report.reports.simple_report import SimpleReport
from collections import Counter


class CompleteReport(SimpleReport):
    @staticmethod
    def generate(produtos):
        relatorio_simples = SimpleReport.generate(produtos)
        lista_de_empresas = [
            empresa["nome_da_empresa"] for empresa in produtos
        ]
        retorno = ""
        for empresa, quantidade in Counter(lista_de_empresas).most_common():
            retorno += f"- {empresa}: {quantidade}\n"
        return (
            f"{relatorio_simples}\n"
            "Produtos estocados por empresa:\n"
            f"{retorno}"
        )
