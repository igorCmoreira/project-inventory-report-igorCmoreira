from inventory_report.inventory.product import Product


def test_cria_produto():
    product = Product(
        1, "mesa", "igcm ltda", "2000-03-14", "2100-03-14", 123456, "none"
    )
    assert product.id == 1
    assert product.nome_do_produto == 'mesa'
    assert product.data_de_fabricacao == '2000-03-14'
    assert product.nome_da_empresa == 'igcm ltda'
    assert product.data_de_validade == '2100-03-14'
    assert product.numero_de_serie == 123456
    assert product.instrucoes_de_armazenamento == 'none'
