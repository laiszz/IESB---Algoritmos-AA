from objetos.produto import Produto


produtos = [
    Produto(1,"Café Expresso", "Café", 2.90, False, 2.50, 15),
    Produto(2, "Pingado", "Café e Leite", 3.30, False, 2.90, 15),
    Produto(3, "Cappuccino", "Café, Vapor de Leite e Canela", 6.90, True, 5.90, 15),
    Produto(4, "Pão na Chapa", "Pão e Manteiga", 6.90, True, 5.90, 15),
    Produto(5, "Pão com Queijo Quente", "Pão, Manteiga e Queijo Minas Frescal", 12.90, False, 9.90, 15),
    Produto(6, "Misto Quente", "Pão, Manteiga, Presunto e Queijo Mussarela", 9.90, False, 8.90, 15),
    Produto(7, "Tapioca de Frango com Requeijão", "Tapioca, Frango Desfiado, Tomate, Cebola e Requeijão", 15.90, True, 12.90, 15),
    Produto(8, "Fatia de Bolo de Chocolate", "Cacau 50%, Açúcar, Ovo, Farinha de Trigo, Óleo, Leite e Fermeto Químico",7.90, False, 12.90, 15)
]

def monta_cardapio_normal() -> list:
    return produtos

def monta_cardapio_promocional() -> list:
    lista_promocional = []

    for produto in monta_cardapio_normal():
        if produto.promocao:
            lista_promocional.append(produto)

    return lista_promocional