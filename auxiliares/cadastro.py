import readchar

import auxiliares.menu as menu
from objetos.cliente import Cliente

clientes = [
    Cliente("123.456.789-10", "Admin", True, 1000, 0)
]

def tela_cadastro():
    print("\033[H\033[2J", end="")
    print("*********************************************************************************\n")
    print("\033[1m\t\t\t\tCadastro de Cliente:\033[0m\n")
    print("_________________________________________________________________________________\n")
    print("\nPreencha com as informações do Cliente:")

def informacoes_cliente():
    print("\nNome do Cliente:")
    nome = str(input())
    print("\nCPF do Cliente:")
    cpf = str(input())

    return nome, cpf

def cadastrar_cliente(nome: str, cpf: str):
    novo_cliente = Cliente(cpf, nome, False, 0, 0)
    clientes.append(novo_cliente)

    print(f"\nCliente \"{nome}\" cadastrado(a) com sucesso!")
    print("\n*********************************************************************************")
    print("\nPressione 0 para sair.")

    opcoes_cadastro()

def opcoes_cadastro():
    try:
        opcao = int(readchar.readkey())

        if opcao != 0:
            opcoes_cadastro()
        else:
            menu.tela_menu()
            menu.opcoes_menu()

    except ValueError:
        opcoes_cadastro()
    except KeyboardInterrupt:
        print("\033[H\033[2J", end="")
        print("O usuário interrompeu o sistema.")
    except Exception:
        print("\033[H\033[2J", end="")
        print("Ocorreu um erro inesperado, tente novamente.")