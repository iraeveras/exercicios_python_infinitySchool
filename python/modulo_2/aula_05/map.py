'''
Crie uma função que aceita uma lista de números e use
a função map para retornar uma nova lista contendo o
dobro de cada número na lista de entrada.
'''

def dobrar_numero():
    numeros = [5,10,20,30]
    dobro = list(map(lambda x: x * 2, numeros))
    return dobro

print(dobrar_numero())
