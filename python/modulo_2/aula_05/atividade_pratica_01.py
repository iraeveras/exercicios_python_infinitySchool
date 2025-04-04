'''
Crie um programa que solicita ao usuário que insira três
notas e, em seguida, calcule a média dessas notas
usando uma função. A função deve receber as três
notas como argumentos e retornar a média. Por fim, o

programa deve imprimir a média calculada.
'''

def media (n1, n2, n3):
    soma = n1 + n2 + n3
    media = soma / 3
    print(media)


valor_01 = float(input("Digite a primeira nota: "))
valor_02 = float(input("Digite a segunda nota: "))
valor_03 = float(input("Digite a terceira nota: "))

media(valor_01,valor_02,valor_03)