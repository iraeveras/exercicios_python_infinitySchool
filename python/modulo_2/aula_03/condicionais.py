
# QUESTÃO 01
'''
# Peça a idade do usuário com base na idade fornecida, o programa deve
# classificar a pessoa em uma das seguintes categorias:
# Se a idade for menor que 12 anos, imprimir "Criança".
# Se a idade estiver entre 12 e 17 anos (inclusive), imprimir "Adolescente".
# Se a idade estiver entre 18 e 59 anos (inclusive), imprimir "Adulto".
# Se a idade for igual ou superior a 60 anos, imprimir "Idoso".

idade = input("Digite a idade sua idade: ")
if idade <= "12":
    print("Criança")    
elif idade <= "17":
    print("Adolecente")
else:
    print("Adulto")
'''


# QUESTÃO 02
'''
# Faça um programa que leia 3 números e informe o maior número e o menor.

numeros = []
limite = 0
while limite < 3:
    numero = int(input("Digite 3 numeros: "))
    numeros.append(numero)
    limite += 1
if numeros[0] > numeros[1] and numeros[0] > numeros[2]:
    print(f"O maior numero é: {numeros[0]}")
elif numeros[1] > numeros[0] and numeros[1] > numeros[2]:
    print(f"O maior numero é: {numeros[1]}")
else:
    print(f"O maior numero é: {numeros[2]}")
'''

# QUESTÃO 03
'''
Faça um programa que peça 10 números inteiros,
calcule e mostre a quantidade de números pares e aquantidade de números impares.
'''


numeros_pares = []
numeros_impares = []

for i in range(10):
    numero = int(input("Digite 10 numeros por vez: "))
    if numero % 2 == 0:
        numeros_pares.append(numero)
    else:
        numeros_impares.append(numero)
print(numeros_impares)
print(numeros_pares)

# for j in numeros:
#     print(j)


