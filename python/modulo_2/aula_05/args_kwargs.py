'''
Crie uma função chamada concatenar_strings que
aceita um número variável de strings como argumentos
posicionais (usando *args). A função deve concatenar
todas as strings em uma única string e retorná-la.
'''

def concatenar_string(*args):
    return args

valores = []

while True:    
    palavras = input("Digite a palvra desejada: ")
    valores.append(palavras)
    opcao = input("Deseja acrescentar mais? 1-sim | 2-não")    
    if opcao == "1":
        continue
    elif opcao == "2":
        print(concatenar_string(valores))
        break
    

    

