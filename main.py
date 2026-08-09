import auxiliares.monta_cardapio

cardapio_promocional = False

def carrega_cardapio():
    if cardapio_promocional:
        cardapio = auxiliares.monta_cardapio.monta_cardapio_promocional()
    else:
        cardapio = auxiliares.monta_cardapio.monta_cardapio_normal()

    return cardapio

def monta_tela_cardapio():
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

    cardapio = carrega_cardapio()

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

monta_tela_cardapio()