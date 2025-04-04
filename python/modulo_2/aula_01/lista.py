# Faça a definição de uma lista contendo os números de 1
# até 5. Finalmente, utilize o print() para exibir os valores
# da lista. */
# lista_de_numeros = [1,2,3,4,5]
# print(lista_de_numeros)


# Defina uma lista com 5 itens que tenha, pelo menos, 3
# classes diferentes. Utilize o print() para exibir o
# terceiro elemento dessa lista.
lista_misturada = ('1','usuario', 'false', 'false', 'animal', 'True')
# print(lista_misturada[4])



for i in range(1, len(lista_misturada)):
    if lista_misturada[i] == 'false':
        qtd = lista_misturada.count('false')
        print(lista_misturada[i], qtd, i)
    