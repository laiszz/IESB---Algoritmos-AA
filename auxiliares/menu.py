import readchar

import auxiliares.cardapio as cardapio
import auxiliares.cadastro as cadastro
import auxiliares.pedido as pedido


def tela_menu():
    # Arte em ASCII gerada no site: https://patorjk.com/software/taag/
    print("\033[H\033[2J", end="")
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
            cardapio.escolhe_cardapio()
        elif opcao == 2:
            pedido.tela_topo()
            pedido.definir_cliente_cadastrado()
            pedido.opcoes_cliente_cadastrado()
        elif opcao == 3:
            cadastro.tela_cadastro()
            informacoes_cliente = cadastro.informacoes_cliente()
            cadastro.cadastrar_cliente(informacoes_cliente[0], informacoes_cliente[1])

    except ValueError:
        tela_menu()
        opcoes_menu()
    except KeyboardInterrupt:
        print("\033[H\033[2J", end="")
        print("O usuário interrompeu o sistema.")
    except Exception:
        print("\033[H\033[2J", end="")
        print("Ocorreu um erro inesperado, tente novamente.")