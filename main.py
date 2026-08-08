import auxiliares.monta_cardapio


cardapio_promocional = True

def carrega_cardapio():
    if cardapio_promocional:
        cardapio = auxiliares.monta_cardapio.monta_cardapio_promocional()
    else:
        cardapio = auxiliares.monta_cardapio.monta_cardapio_normal()

    return cardapio

print(carrega_cardapio())