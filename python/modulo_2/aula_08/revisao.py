# FUNÇÕES
# args
'''
def media(*args):
    if not args:
        return 0
    return sum(args) / len(args)

resultado = media(2,4,6,8,10)
print(resultado)
'''

# kwargs
# def saudacao(nome, *args, mensagem="olá", **kwargs):
#     saudacao_completa = f" {mensagem}, {nome}"
#     if args:
#         saudacao_completa += f" {', '.join(args)}"
#     if kwargs:
#         saudacao_completa += f"({', '.join(f'{k}={v}' for k, v in kwargs.items())})"
#     return saudacao_completa

# resultado = saudacao("Alice", "Bob", "Carol", mensagem="Oi", idade=30, cidade="Nova York")
# print(resultado)

import random

# Função para gerar dados de vendas trimestrais
def gerar_dados_vendas(produtos, trimestres):
    dados_vendas = {}
    for produto in produtos:
        dados_vendas[produto] = { trimestre: random.randint(1000, 10000) for trimestre in trimestres }
    return dados_vendas



# Lista de produtos
produtos = ["Produto A", "Produto B", "Produto C", "Produto D"]
# Lista de trimestres
trimestres = ["Q1", "Q2", "Q3", "Q4"]

# Gerar dados de vendas
dados_vendas = gerar_dados_vendas(produtos, trimestres)

# Exibir os dados gerados
for produto, vendas in dados_vendas.items():
    print(f"{produto}: {vendas}")
    print(vendas["Q1"] + vendas["Q2"] + vendas["Q3"] + vendas["Q4"])