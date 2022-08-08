from datetime import date
from collections import Counter


class SimpleReport:
    @classmethod
    def generate(ctl, produtos):
        hoje = str(date.today())
        ultima_data_de_validade = "2100-31-12"
        ultima_data_de_fab = "2100-31-12"
        fabricas = []
        for produto in produtos:
            fabricas.append(produto["nome_da_empresa"])
            if hoje <= produto["data_de_validade"] <= ultima_data_de_validade:
                ultima_data_de_validade = produto["data_de_validade"]
            if ultima_data_de_fab > produto["data_de_fabricacao"]:
                ultima_data_de_fab = produto["data_de_fabricacao"]

        empresa_com_mais_produtos = Counter(fabricas).most_common()[0][0]

        return (
            f"Data de fabricação mais antiga: {ultima_data_de_fab}\n"
            f"Data de validade mais próxima: {ultima_data_de_validade}\n"
            f"Empresa com mais produtos: {empresa_com_mais_produtos}"
        )
