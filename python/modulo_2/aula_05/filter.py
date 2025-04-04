'''
Crie uma função que aceita uma lista de números e use
a função filter para retornar uma nova lista contendo
apenas os números pares da lista de entrada.
'''

def filtro_num_pares(lista_num):
    filtro = list(filter(lambda x: x % 2 == 0, lista_num))
    return filtro

num_listados = []

while True:
    numero = int(input("Digite o numero: "))
    num_listados.append(numero)
    opcao = input("deseja continuar? 1-sim | 2-não: ")
    if opcao == "1":
        continue
    elif opcao == "2":
        print(filtro_num_pares(num_listados))
        break

    