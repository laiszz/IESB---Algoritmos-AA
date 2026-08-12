import readchar

import auxiliares.cardapio


def tela_menu():
    # Arte em ASCII gerada no site: https://patorjk.com/software/taag/
    print("*********************************************************************************\n")
    print("  _______ _         _____                 ")
    print(" |__   __(_)       |  __ \                ")
    print("    | |   _  __ _  | |__) |___  ___  __ _ ")
    print("    | |  | |/ _` | |  _  // _ \/ __|/ _` |")
    print("    | |  | | (_| | | | \ \ (_) \__ \ (_| |")
    print("    |_|  |_|\__,_| |_|  \_\___/|___/\__,_|")
    print("                               Coffee Shop")
    print("\n*********************************************************************************")
    print("\nAperte um dos números abaixo para selecionar uma opção:")
    print("\033[1m1\033[0m - Ver o cardápio")
    print("\033[1m2\033[0m - Fazer um pedido")
    print("\033[1m3\033[0m - Cadastrar cliente")
    print("\033[1m0\033[0m - Sair")

def opcoes_menu():
    try:
        opcao = int(readchar.readkey())

        if opcao < 0 or opcao > 3:
            tela_menu()
            opcoes_menu()
        elif opcao == 1:
            auxiliares.cardapio.escolhe_cardapio()

    except ValueError:
        tela_menu()
        opcoes_menu()
    except KeyboardInterrupt:
        print("\033[H\033[2J", end="")
        print("O usuário interrompeu o sistema.")
    except Exception:
        print("\033[H\033[2J", end="")
        print("Ocorreu um erro inesperado, tente novamente.")