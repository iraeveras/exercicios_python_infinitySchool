'''
[PYIA-A05] Crie uma função chamada maior_numero que receberá três números como argumentos. 
Esta função deve comparar os três números e identificar qual deles é o maior. Para isso, utilize uma estrutura de controle que 
verifique qual número é maior que os outros dois. A função deve então retornar o maior número encontrado.
'''
# from functools import reduce

def maior_numero(n1,n2,n3):
    return reduce(lambda x, y: x if x > y else y, [n1,n2,n3])

valor_01 = float(input("Digite o primeiro numero: "))
valor_02 = float(input("Digite o segundo numero: "))
valor_03 = float(input("Digite o terceiro numero: "))

maior = maior_numero(valor_01,valor_02,valor_03)

print(f"O maior numero é {maior}")