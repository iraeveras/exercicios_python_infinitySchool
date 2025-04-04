# dados_pessoa1 = {
#     'nome': 'João',
#     'idade': '32',
# }

# print(dados_pessoa1)

dados_pessoa2 = dict([
    ('nome', 'Antonio'),
    ('idade', '56'),
    ('endereco','rua de baixo')
])

for i in dados_pessoa2.items():
    print(i)


dados_pessoa3 = {
    'nome': 'Ambrosio',
    'cargo': 'Analista de suport',
    'setor': 'TI',
    'sub_setor': 'service desk',
}

for chave, valor in dados_pessoa3.items():
    print(f"{chave}: {valor}")