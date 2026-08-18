import readchar

import auxiliares.cardapio as cardapio
import auxiliares.cadastro as cadastro
import auxiliares.pedido as pedido

# ***********************
# TELAS E TEXTOS
# ***********************

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

# ***********************
# OPÇÕES E ESCOLHAS
# ***********************

def opcoes_menu():
    try:
        # Lê apenas um caracter na entrada, sem necessidade do usuário apertar Enter
        opcao = int(readchar.readkey())

        # Se opção inválida, aciona o ValueError
        if opcao < 0 or opcao > 3:
            raise ValueError
        # Início do Cardápio
        elif opcao == 1:
            cardapio.tela_escolhe_cardapio()
            cardapio.escolhe_cardapio()
        # Início do Pedido
        elif opcao == 2:
            pedido.tela_topo()
            pedido.definir_cliente_cadastrado()
            pedido.opcoes_cliente_cadastrado()
        # Início do Cadastro
        elif opcao == 3:
            cadastro.tela_cadastro()
            informacoes_cliente = cadastro.informacoes_cliente()
            cadastro.cadastrar_cliente(informacoes_cliente[0], informacoes_cliente[1])

    # Trata o ValueError apenas recarregando a própria função recursivamente
    # para que o usuário tenha a sensação de que a tela continua estática
    # até ele pressionar uma opção válida
    except ValueError:
        tela_menu()
        opcoes_menu()
    # Caso o usuário interrompa o sistema (CTRL + C), limpa a tela e
    # imprime uma mensagem informativa
    except KeyboardInterrupt:
        print("\033[H\033[2J", end="")
        print("O usuário interrompeu o sistema.")
    # Caso aconteça um erro genérico não tratado anteriormente, limpa a tela
    # e imprime uma mensagem informativa
    except Exception as e:
        print("\033[H\033[2J", end="")
        print(f"Ocorreu um erro inesperado, tente novamente. {e}")