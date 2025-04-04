'''
Crie uma função que aceita uma lista de strings e use a
função reduce (importada de functools) para encontrar
a maior string na lista.
'''

from functools import reduce

def lista_de_palavras(list_palavras):
    lista = reduce(lambda x, y: x if len(x) > len(y) else y, list_palavras)
    return lista

palavra_01 = input("Digite a primeira palavra: ")
palavra_02 = input("Digite a segunda palavra: ")

palavra = []

palavra.append(palavra_01)
palavra.append(palavra_02)

print(lista_de_palavras(palavra))
