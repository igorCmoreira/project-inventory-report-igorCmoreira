from inventory_report.inventory.product import Product


def test_relatorio_produto():
    product = Product(
        2,
        "farinha",
        "farini",
        "01-05-2021",
        "02-06-2023",
        123457,
        "Ao abrigo de luz",
    )
    assert product.__repr__() == (
        "O produto farinha"
        " fabricado em 01-05-2021"
        " por farini com validade"
        " até 02-06-2023"
        " precisa ser armazenado Ao abrigo de luz."
    )
