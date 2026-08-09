import readchar
import auxiliares.cardapio as cardapio
import auxiliares.menu as menu

cardapio_promocional = True

while True:
    menu.monta_tela_menu()

    try:
        opcao = int(readchar.readkey())

        if opcao < 0 or opcao > 3:
            raise ValueError("\033[H\033[2J")

        if opcao == 1:
            print("\033[H\033[2J", end="")

            while True:
                cardapio.monta_tela_cardapio(cardapio_promocional, cardapio.monta_cardapio(cardapio_promocional))

                try:
                    opcao_cardapio = int(readchar.readkey())

                    if opcao_cardapio != 0:
                        raise ValueError("\033[H\033[2J")

                    if opcao_cardapio == 0:
                        break

                except Exception:
                    print("\033[H\033[2J", end="")

        if opcao == 0:
            break

    except ValueError:
        print("\033[H\033[2J", end="")
    except KeyboardInterrupt:
        print("\033[H\033[2J", end="")
        print("O usuário interrompeu o sistema.")
        break
    except Exception:
        print("\033[H\033[2J", end="")
        print("Ocorreu um erro inesperado, tente novamente.")
        break