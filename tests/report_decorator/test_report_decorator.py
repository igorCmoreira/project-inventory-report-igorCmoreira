from inventory_report.reports.colored_report import ColoredReport
from inventory_report.reports.simple_report import SimpleReport


mock = [
    {
        "nome_da_empresa": "farinha",
        "data_de_fabricacao": "2022-09-03",
        "data_de_validade": "2025-12-12",
    }
]


def test_decorar_relatorio():
    relatorio = ColoredReport(SimpleReport).generate(mock)

    assert "\033[36m2022-09-03\033[0m" in relatorio
    assert "\033[36m2025-12-12\033[0m" in relatorio
    assert "\033[31mfarinha\033[0m" in relatorio
