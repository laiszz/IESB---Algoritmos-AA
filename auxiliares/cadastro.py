import readchar

import auxiliares.menu as menu
from objetos.cliente import Cliente

# ***********************
# LISTA DE CLIENTES PRÉ-CADASTRADOS
# ***********************

clientes = [
    Cliente("12345678910", "Admin", True, 1000, 0),
    Cliente("37923843880", "Laís Sales Xavier", True, 950, 2)
]

# ***********************
# TELAS E TEXTOS
# ***********************

def tela_cadastro():
    print("\033[H\033[2J", end="")
    print("*********************************************************************************\n")
    print("\033[1m\t\t\t\tCadastro de Cliente:\033[0m\n")
    print("_________________________________________________________________________________\n")
    print("\nPreencha com as informações do Cliente:")

# ***********************
# OPÇÕES E ESCOLHAS
# ***********************

def opcoes_cadastro():
    try:
        # Lê apenas um caracter na entrada, sem necessidade do usuário apertar Enter
        opcao = int(readchar.readkey())

        # Se opção inválida, aciona o ValueError
        if opcao != 0:
            raise ValueError
        # Carrega o Menu Principal
        else:
            menu.tela_menu()
            menu.opcoes_menu()

    # Trata o ValueError apenas recarregando a própria função recursivamente
    # para que o usuário tenha a sensação de que a tela continua estática
    # até ele pressionar uma opção válida
    except ValueError:
        opcoes_cadastro()
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

# ***********************
# PROCESSAMENTO
# ***********************

# Retorna o Nome e o CPF do Cliente
def informacoes_cliente():
    print("\nNome do Cliente:")
    nome = input()
    print("\nCPF do Cliente (apenas números, sem pontos ou traços):")
    cpf = input()

    return nome, cpf

# Instancia o Cliente com o Nome e o CPF informado
def cadastrar_cliente(nome: str, cpf: str):
    # Não contabiliza CPF repetido nem permite cadastrar
    # clientes com fidelidade, por complexidade
    novo_cliente = Cliente(cpf, nome, False, 0, 0)

    # Adiciona o novo Cliente à lista de clientes cadastrados
    clientes.append(novo_cliente)

    print(f"\nCliente \"{nome}\" cadastrado(a) com sucesso!")
    print("\n*********************************************************************************")
    print("\nPressione 0 para sair.")

    opcoes_cadastro()