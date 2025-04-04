'''
Crie uma função chamada criar_lista_de_compras que
aceita um número variável de itens de compras como
argumentos posicionais (usando *args). A função deve
criar e retornar uma lista de compras que contenha

todos os itens fornecidos.
'''
compras = []

def cria_lista_de_compras(*args):
    return args

opcao_inicial = input("Deseja iniciar sua lista agora? 1-SIM 2-NÃO: ")
if opcao_inicial == "1":
    while True:
        entrada = input("Digite sua lista: ")
        compras.append(entrada)
        opcao = input("Deseja adicionar mais? 1-SIM 2-NÃO: ")
        if opcao == "1":
            continue
        elif opcao == "2":
            print(cria_lista_de_compras(compras))
            break
        else:
            print("Opção inválida.")
            continue
else:
    print("Saindo do sistema.")