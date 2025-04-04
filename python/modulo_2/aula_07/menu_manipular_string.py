from manipulacao_strings import *

def menu():
    while True:
        print("===== Menu =====")
        print("1. Digitar texto")
        print("2. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            texto = input("Digite um texto: ")
            resultado = funcao_manipular_string(texto)
            print(resultado)
            break
        elif opcao == "2":
            print("Saindo...")
            break
        else:
            print("Opção inválida, tente novamente.")


menu()