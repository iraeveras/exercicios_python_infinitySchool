# criando um conjuto vazio
frutas = set()
# adcionando uma lista de frutas
frutas.add('Maçã')
frutas.add('Banana')
frutas.add('Uva')
frutas.add('Laranja')
frutas.add('Morango')
print(f"Imprimindo o conjuto frutas: {frutas}")

banana = 'Banana' in frutas
print(f"Verificando se a fruta Banana consta no conjunto: {banana}")

frutas_vermelhas = {'morango','cereja','franboesa'}
print(f"Imprimindo o conjuto frutas vermelhas: {frutas_vermelhas}")

frutas_vermelhas.remove('cereja')
print(f"Imprimindo o conjuto frutas vermelhas atualizado: {frutas_vermelhas}")

a = {'a','b'}
b = {'b','c'}

uniao_a_b = a.union(b)
print(f"Fazendo a união dos conjuntos 'a' e 'b': {uniao_a_b}")

intercection = a.intersection(b)
print(f"intercection: {intercection}")

lista1 = ['cereja', 'franboesa', 'morango']
lista2 = ['Maçã', 'Banana', 'Laranja']

set1 = set(lista1)
set2 = set(lista2)

print(set1.union(set2))

