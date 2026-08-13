import readchar
from collections import Counter
from tabulate import tabulate

from auxiliares import cadastro
from auxiliares import cardapio
from objetos.cliente import Cliente
from objetos.pedido import Pedido
from objetos.produto import Produto


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

def tela_pedido():
    print("\nInforme, um por vez, o código (apenas o número) dos produtos a serem adicionados no pedido.")
    print("\nPara finalizar, digite 0.")
    print("\n_________________________________________________________________________________")

def resumo_pedido(quantidades: dict, valor_total: float, pontos_acumulados: int):
    print("\033[H\033[2J", end="")
    print("*********************************************************************************\n")
    print("\033[1m\t\t\t\tResumo do pedido:\033[0m\n")
    print("_________________________________________________________________________________\n")

    cabecalho = ["Código", "Nome", "Quantidade", "Valor Unitário", "Valor Total"]
    dados_resumo = []

    for produto, quantidade in quantidades.items():
        if produto.promocao:
            dados_resumo.append([produto.codigo, produto.nome, quantidade, f"R${produto.preco_promocional:.2f}", f"R${(produto.preco_promocional * quantidade):.2f}"])
        else:
            dados_resumo.append([produto.codigo, produto.nome, quantidade, f"R${produto.preco:.2f}", f"R${(produto.preco * quantidade):.2f}"])

    print(tabulate(dados_resumo, cabecalho, tablefmt="grid", floatfmt=".2f", stralign="left", numalign="left"))

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

def registrar_pedido(pedido: Pedido):
    print("\nCódigo do produto:")

    try:
        codigo = int(input())
        produto = next((p for p in cardapio.produtos if p.codigo == codigo), None)

        if codigo != 0:
            if produto is None:
                raise ValueError("Digite um código válido.")
            else:
                if produto.estoque - 1 >= 0:
                    pedido.produtos.append(produto)
                    produto.estoque -= 1
                    registrar_pedido(pedido)
                else:
                    raise ValueError("Produto fora de estoque.")

    except ValueError as e:
        print(f"{e} Nenhum produto foi adicionado ao pedido.")
        registrar_pedido(pedido)
    except KeyboardInterrupt:
        print("\033[H\033[2J", end="")
        print("O usuário interrompeu o sistema.")
    except Exception:
        print("\033[H\033[2J", end="")
        print("Ocorreu um erro inesperado, tente novamente.")

def calcula_valor_total(pedido: Pedido):
    valor_total = 0
    pontos_acumulados = 0

    for produto in pedido.produtos:
        if produto.promocao:
            valor_total += produto.preco_promocional
        else:
            valor_total += produto.preco

    if pedido.cliente_fidelidade:
        valor_total *= 0.9
        pontos_acumulados = int(10 * len(pedido.produtos))

    return round(valor_total,2), pontos_acumulados

def calcula_quantidade_produtos(produtos: list):
    quantidades = Counter(produtos)
    return quantidades

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
            tela_topo()
            tela_pedido()
            pedido = iniciar_pedido(None)
            registrar_pedido(pedido)
            valor_pontos = calcula_valor_total(pedido)
            quantidades = calcula_quantidade_produtos(pedido.produtos)
            resumo_pedido(quantidades, valor_pontos[0], valor_pontos[1])

    except ValueError:
        opcoes_cliente_cadastrado()
    except KeyboardInterrupt:
        print("\033[H\033[2J", end="")
        print("O usuário interrompeu o sistema.")
    except Exception:
        print("\033[H\033[2J", end="")
        print(f"Ocorreu um erro inesperado, tente novamente.")

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
                tela_topo()
                tela_pedido()
                pedido = iniciar_pedido(cliente)
                registrar_pedido(pedido)
                valor_pontos = calcula_valor_total(pedido)
                quantidades = calcula_quantidade_produtos(pedido.produtos)
                resumo_pedido(quantidades, valor_pontos[0], valor_pontos[1])
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