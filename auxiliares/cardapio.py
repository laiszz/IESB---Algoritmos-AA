import readchar

from objetos.produto import Produto


produtos = [
    Produto(1,"Café Expresso", "Café", "Bebidas", 2.90, False, 2.50, 15),
    Produto(2, "Pingado", "Café e Leite", "Bebidas", 3.30, False, 2.90, 15),
    Produto(3, "Cappuccino", "Café, Vapor de Leite e Canela", "Bebidas", 6.90, True, 5.90, 15),
    Produto(4, "Pão na Chapa", "Pão e Manteiga", "Comidas", 6.90, True, 5.90, 15),
    Produto(5, "Pão com Queijo Quente", "Pão, Manteiga e Queijo Minas Frescal", "Comidas", 12.90, False, 9.90, 15),
    Produto(6, "Misto Quente", "Pão, Manteiga, Presunto e Queijo Mussarela", "Comidas", 9.90, False, 8.90, 15),
    Produto(7, "Tapioca de Frango com Requeijão", "Tapioca, Frango Desfiado, Tomate, Cebola e Requeijão", "Comidas", 15.90, True, 12.90, 15),
    Produto(8, "Fatia de Bolo de Chocolate", "Cacau 50%, Açúcar, Ovo, Farinha de Trigo, Óleo, Leite e Fermeto Químico", "Comidas",7.90, False, 12.90, 15)
]

def monta_cardapio(cardapio_promocional: bool) -> list:
    if cardapio_promocional:
        lista_promocional = []

        for produto in produtos:
            if produto.promocao:
                lista_promocional.append(produto)

        return lista_promocional
    else:
        return produtos

def tela_cardapio(cardapio_promocional: bool, cardapio: list):
    print("\033[H\033[2J", end="")
    if cardapio_promocional:
        print("*********************************************************************************\n")
        print("\033[1m\t\t\t\tPromoções de Hoje:\033[0m\n")
        print("_________________________________________________________________________________\n")
    else:
        print("*********************************************************************************\n")
        print("\033[1m\t\t\t\tCardápio:\033[0m\n")
        print("_________________________________________________________________________________\n")

    if not cardapio_promocional:
        print("Obs: Produtos destacados com *** estão na promoção!\n")
        auxiliar_promocional = "***"
    else:
        auxiliar_promocional = ""

    print("\033[1mBebidas:\033[0m\n")

    for produto in cardapio:
        if produto.categoria == "Bebidas":
            if produto.promocao:
                print(f"\033[1m[{produto.codigo:03d}]\t{produto.nome:.<40}R${produto.preco_promocional:.2f}{auxiliar_promocional}\033[0m")
                print(f"     \t\x1B[3m{produto.ingredientes}\x1B[0m")
            else:
                print(f"\033[1m[{produto.codigo:03d}]\t{produto.nome:.<40}R${produto.preco:.2f}\033[0m")
                print(f"     \t\x1B[3m{produto.ingredientes}\x1B[0m")

    print("\n\033[1mComidas:\033[0m\n")

    for produto in cardapio:
        if produto.categoria == "Comidas":
            if produto.promocao:
                print(f"\033[1m[{produto.codigo:03d}]\t{produto.nome:.<40}R${produto.preco_promocional:.2f}{auxiliar_promocional}\033[0m")
                print(f"     \t\x1B[3m{produto.ingredientes}\x1B[0m")
            else:
                print(f"\033[1m[{produto.codigo:03d}]\t{produto.nome:.<40}R${produto.preco:.2f}\033[0m")
                print(f"     \t\x1B[3m{produto.ingredientes}\x1B[0m")

    print("\n*********************************************************************************")
    print("\nPressione 0 para sair.")

def escolhe_cardapio():
    print("\033[H\033[2J", end="")
    print("Deseja ver o cardápio completo ou apenas as promoções?")
    print("\nAperte um dos números abaixo para selecionar uma opção:")
    print("\033[1m1\033[0m - Ver o cardápio normal")
    print("\033[1m2\033[0m - Ver o cardápio das promoções")
    print("\033[1m0\033[0m - Sair")

    try:
        opcao = int(readchar.readkey())

        if opcao < 0 or opcao > 2:
            escolhe_cardapio()
        elif opcao == 1:
            tela_cardapio(False, monta_cardapio(False))
            opcoes_cardapio(False, monta_cardapio(False))
        elif opcao == 2:
            tela_cardapio(True, monta_cardapio(True))
            opcoes_cardapio(False, monta_cardapio(False))

    except ValueError:
        escolhe_cardapio()
    except KeyboardInterrupt:
        print("\033[H\033[2J", end="")
        print("O usuário interrompeu o sistema.")
    except Exception:
        print("\033[H\033[2J", end="")
        print("Ocorreu um erro inesperado, tente novamente.")

def opcoes_cardapio(cardapio_promocional: bool, cardapio: list):
    try:
        opcao = int(readchar.readkey())

        if opcao != 0:
            tela_cardapio(cardapio_promocional, cardapio)
            opcoes_cardapio(cardapio_promocional, cardapio)
        else:
            print(opcao)

    except ValueError:
        tela_cardapio(cardapio_promocional, cardapio)
        opcoes_cardapio(cardapio_promocional, cardapio)
    except KeyboardInterrupt:
        print("\033[H\033[2J", end="")
        print("O usuário interrompeu o sistema.")
    except Exception:
        print("\033[H\033[2J", end="")
        print("Ocorreu um erro inesperado, tente novamente.")