import readchar
from collections import Counter
from tabulate import tabulate

from auxiliares import cadastro
from auxiliares import cardapio
from objetos.cliente import Cliente
from objetos.pedido import Pedido
from auxiliares import menu

# ***********************
# TELAS E TEXTOS
# ***********************

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

# Mostra o resumo do Pedido formatado na tela, com valores padrões ou promocionais,
# usando o pacote externo Tabulate
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

    print(f"\nValor Total: R${valor_total:.2f}\nPontos acumulados: {pontos_acumulados}")

    print("\nDeseja finalizar ou cancelar o pedido?")
    print("\nAperte um dos números abaixo para selecionar uma opção:")
    print("\033[1m1\033[0m - Finalizar")
    print("\033[1m2\033[0m - Cancelar")

# ***********************
# OPÇÕES E ESCOLHAS
# ***********************

def opcoes_cadastrar_cliente():
    try:
        # Lê apenas um caracter na entrada, sem necessidade do usuário apertar Enter
        opcao = int(readchar.readkey())

        # Se opção inválida, aciona o ValueError
        if opcao < 0 or opcao > 2:
            raise ValueError
        # Cadastro do Cliente
        if opcao == 1:
            cadastro.tela_cadastro()
            informacoes_cliente = cadastro.informacoes_cliente()
            cadastro.cadastrar_cliente(informacoes_cliente[0], informacoes_cliente[1])
        # Prossegue para o processamento do Pedido
        if opcao == 2:
            tela_topo()
            tela_pedido()
            pedido = iniciar_pedido(None)
            registrar_pedido(pedido)
            valor_pontos = calcula_valor_total(pedido)
            quantidades = calcula_quantidade_produtos(pedido.produtos)
            resumo_pedido(quantidades, valor_pontos[0], valor_pontos[1])
            opcoes_resumo(pedido, None)

    # Trata o ValueError apenas recarregando a própria função recursivamente
    # para que o usuário tenha a sensação de que a tela continua estática
    # até ele pressionar uma opção válida
    except ValueError:
        opcoes_cliente_cadastrado()
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

def opcoes_cliente_cadastrado():
    try:
        # Lê apenas um caracter na entrada, sem necessidade do usuário apertar Enter
        opcao = int(readchar.readkey())

        # Se opção inválida, aciona o ValueError
        if opcao < 1 or opcao > 2:
            raise ValueError
        # Coleta os dados do Cliente
        elif opcao == 1:
            tela_topo()
            cpf = informar_cliente()
            # Procura o cliente pelo cpf digitado, se não encontrar == None
            cliente = next((c for c in cadastro.clientes if c.cpf == cpf), None)

            # Se não encontrar, carrega a tela Cliente Não Encontrado
            if cliente is None:
                tela_topo()
                cliente_nao_encontrado()
                opcoes_voltar()
            # Prossegue para o processamento do Pedido
            else:
                tela_topo()
                tela_pedido()
                pedido = iniciar_pedido(cliente)
                registrar_pedido(pedido)
                valor_pontos = calcula_valor_total(pedido)
                quantidades = calcula_quantidade_produtos(pedido.produtos)
                resumo_pedido(quantidades, valor_pontos[0], valor_pontos[1])
                opcoes_resumo(pedido, cliente)
        # Da a opção de cadastrar o Cliente
        else:
            tela_topo()
            escolher_cadastrar_cliente()
            opcoes_cadastrar_cliente()

    # Trata o ValueError apenas recarregando a própria função recursivamente
    # para que o usuário tenha a sensação de que a tela continua estática
    # até ele pressionar uma opção válida
    except ValueError:
        opcoes_cliente_cadastrado()
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

def opcoes_voltar():
    try:
        # Lê apenas um caracter na entrada, sem necessidade do usuário apertar Enter
        opcao = int(readchar.readkey())

        # Se opção inválida, aciona o ValueError
        if opcao != 0:
            raise ValueError
        # Volta para a tela de "O Cliente já possui cadastro?"
        else:
            tela_topo()
            definir_cliente_cadastrado()
            opcoes_cliente_cadastrado()

    # Trata o ValueError apenas recarregando a própria função recursivamente
    # para que o usuário tenha a sensação de que a tela continua estática
    # até ele pressionar uma opção válida
    except ValueError:
        opcoes_voltar()
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

def opcoes_resumo(pedido: Pedido, cliente: Cliente | None):
    try:
        # Lê apenas um caracter na entrada, sem necessidade do usuário apertar Enter
        opcao = int(readchar.readkey())

        # Se opção inválida, aciona o ValueError
        if opcao < 1 or opcao > 2:
            raise ValueError
        # Finaliza o Pedido, aumentando o nº de pedidos do Cliente
        # e acumulando pontos, e volta para o Menu Principal
        if opcao == 1:
            if cliente is not None:
                cliente.total_pedidos += 1

                if cliente.fidelidade:
                    cliente.pontos += pedido.pontos_acumulados

            menu.tela_menu()
            menu.opcoes_menu()
        # Cancela o Pedido e volta para o Menu Principal
        else:
            del pedido
            menu.tela_menu()
            menu.opcoes_menu()

    # Trata o ValueError apenas recarregando a própria função recursivamente
    # para que o usuário tenha a sensação de que a tela continua estática
    # até ele pressionar uma opção válida
    except ValueError:
        opcoes_resumo(pedido, cliente)
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

# Retorna o CPF do Cliente
def informar_cliente():
    print("\nInforme o CPF do cliente (apenas números, sem pontos ou traços):")
    cpf = input()

    return cpf

# Retorna a instância do Pedido a ser usada no processo
def iniciar_pedido(cliente: Cliente | None):
    if cliente is None:
        pedido = Pedido([], 0, None, None, None, None)
    else:
        pedido = Pedido([], 0, cliente.cpf, cliente.fidelidade, 0, 0)

    return pedido

# Adiciona produtos à lista do Pedido, de forma recursiva
# e contínua até ser interrompido
def registrar_pedido(pedido: Pedido):
    print("\nCódigo do produto:")

    try:
        codigo = int(input())
        # Procura o produto pelo código digitado, se não encontrar == None
        produto = next((p for p in cardapio.produtos if p.codigo == codigo), None)

        # Se não deseja voltar
        if codigo != 0:
            # Se não encontrou o produto (None), aciona o ValueError
            # com uma mesagem informativa
            if produto is None:
                raise ValueError("Digite um código válido.")
            else:
                # Se o produto tem estoque, adiciona ao Pedido,
                # remove 1 do estoque e continua a execução do
                # registro de pedido
                if produto.estoque - 1 >= 0:
                    pedido.produtos.append(produto)
                    produto.estoque -= 1
                    registrar_pedido(pedido)
                # Se o produto não tem estoque, aciona o ValueError
                # com uma mesagem informativa
                else:
                    raise ValueError("Produto fora de estoque.")

    # Trata o ValueError recarregando a própria função recursivamente
    # para que o usuário possa continuar adicionando produtos no
    # pedido, com uma mensagem sobre o motivo do erro
    except ValueError as e:
        print(f"{e} Nenhum produto foi adicionado ao pedido.")
        registrar_pedido(pedido)
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

# Retorna o valor total e os pontos acumulados de um Pedido
def calcula_valor_total(pedido: Pedido):
    valor_total = 0
    pontos_acumulados = 0

    for produto in pedido.produtos:
        # Se o produto está em promoção, soma o valor promocional
        if produto.promocao:
            valor_total += produto.preco_promocional
        # Soma o valor padrão
        else:
            valor_total += produto.preco

    # Se o cliente tiver fidelidade, concede 10% de desconto
    # e 10 pontos por produto no pedido
    if pedido.cliente_fidelidade:
        valor_total *= 0.9
        pontos_acumulados = int(10 * len(pedido.produtos))
        pedido.pontos_acumulados = pontos_acumulados

    return round(valor_total,2), pontos_acumulados

# Retorna a quantidade de cada produto no Pedido
# Ex: [{Café: 2}, {Pão na Chapa: 3}]
def calcula_quantidade_produtos(produtos: list):
    quantidades = Counter(produtos)
    return quantidades