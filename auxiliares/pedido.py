import readchar

import auxiliares.cadastro as cadastro
from objetos.cliente import Cliente
from objetos.pedido import Pedido


def tela_topo():
    print("\033[H\033[2J", end="")
    print("*********************************************************************************\n")
    print("\033[1m\t\t\t\tRegistrar pedido:\033[0m\n")
    print("_________________________________________________________________________________\n")

def definir_cliente_cadastrado():
    print("\nO Cliente já possui cadastro?")
    print("\nAperte um dos números abaixo para selecionar uma opção:")
    print("\033[1m1\033[0m - Sim")
    print("\033[1m2\033[0m - Não")

def escolher_cadastrar_cliente():
    print("\nDeseja cadastrar o Cliente?")
    print("\nAperte um dos números abaixo para selecionar uma opção:")
    print("\033[1m1\033[0m - Sim")
    print("\033[1m2\033[0m - Não")

def cliente_nao_encontrado():
    print("\nCliente não encontrado")
    print("\nPressione 0 para voltar.")

def informar_cliente():
    print("\nInforme o CPF do cliente (apenas números, sem pontos ou traços):")
    cpf = input()

    return cpf

def iniciar_pedido(cliente: Cliente | None):
    if cliente is None:
        pedido = Pedido([], 0, None, None, None, None)
    else:
        pedido = Pedido([], 0, cliente.cpf, cliente.fidelidade, None, None)

    return pedido

def opcoes_cadastrar_cliente():
    try:
        opcao = int(readchar.readkey())

        if opcao < 0 or opcao > 2:
            raise ValueError
        if opcao == 1:
            cadastro.tela_cadastro()
            informacoes_cliente = cadastro.informacoes_cliente()
            cadastro.cadastrar_cliente(informacoes_cliente[0], informacoes_cliente[1])
        if opcao == 2:
            pedido = iniciar_pedido(None)
            print(pedido.cliente_cpf)

    except ValueError:
        opcoes_cliente_cadastrado()
    except KeyboardInterrupt:
        print("\033[H\033[2J", end="")
        print("O usuário interrompeu o sistema.")
    except Exception:
        print("\033[H\033[2J", end="")
        print("Ocorreu um erro inesperado, tente novamente.")

def opcoes_cliente_cadastrado():
    try:
        opcao = int(readchar.readkey())

        if opcao < 1 or opcao > 2:
            raise ValueError
        elif opcao == 1:
            tela_topo()
            cpf = informar_cliente()
            cliente = next((c for c in cadastro.clientes if c.cpf == cpf), None)

            if cliente is None:
                tela_topo()
                cliente_nao_encontrado()
                opcoes_voltar()
            else:
                pedido = iniciar_pedido(cliente)
                print(pedido.cliente_cpf)
        else:
            tela_topo()
            escolher_cadastrar_cliente()
            opcoes_cadastrar_cliente()

    except ValueError:
        opcoes_cliente_cadastrado()
    except KeyboardInterrupt:
        print("\033[H\033[2J", end="")
        print("O usuário interrompeu o sistema.")
    except Exception as e:
        print("\033[H\033[2J", end="")
        print(f"Ocorreu um erro inesperado, tente novamente. {e}")

def opcoes_voltar():
    try:
        opcao = int(readchar.readkey())

        if opcao != 0:
            raise ValueError
        else:
            tela_topo()
            definir_cliente_cadastrado()
            opcoes_cliente_cadastrado()

    except ValueError:
        opcoes_voltar()
    except KeyboardInterrupt:
        print("\033[H\033[2J", end="")
        print("O usuário interrompeu o sistema.")
    except Exception:
        print("\033[H\033[2J", end="")
        print("Ocorreu um erro inesperado, tente novamente.")