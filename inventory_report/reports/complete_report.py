from inventory_report.reports.simple_report import SimpleReport
from collections import Counter


class CompleteReport(SimpleReport):
    @staticmethod
    def generate(produtos):
        relatorio_simples = SimpleReport.generate(produtos)
        lista_de_empresas = [
            produto["nome_da_empresa"] for produto in produtos
        ]
        retorno = ""

        nomes_das_empresas = Counter(lista_de_empresas).most_common()

        for nome, quantidade in nomes_das_empresas:
            retorno += f"- {nome} : {quantidade}/n"

        return (
            f"{relatorio_simples}/n"
            "Produtos estocados por empresas:/n"
            f"{retorno}"
        )
