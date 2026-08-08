import auxiliares.monta_cardapio

cardapio_promocional = True

def carrega_cardapio():
    if cardapio_promocional:
        cardapio = auxiliares.monta_cardapio.monta_cardapio_promocional()
    else:
        cardapio = auxiliares.monta_cardapio.monta_cardapio_normal()

    return cardapio

def monta_tela_cardapio():
    if cardapio_promocional:
        print("********************************************************\n")
        print("\033[1m                 Promoções de Hoje:\033[0m")
        print("________________________________________________________\n")
    else:
        print("********************************************************\n")
        print("\033[1m                      Cardápio:\033[0m")
        print("________________________________________________________\n")

    cardapio = carrega_cardapio()

    for produto in cardapio:
        print(f"[{produto.codigo:03d}]\t{produto.nome:.<40}R${produto.preco:.2f}")

    print("\n********************************************************")

monta_tela_cardapio()