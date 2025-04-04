import operacoes

def menu():
    while True:
        print("===== Menu =====")
        print("1 - Operação de soma")
        print("2 - Operação de multiplicação")
        print("3 - Operação de divisão")
        print("4 - Operação de subtração")
        print("5 - Sair")

        opcao = input("Digite uma opção: ")
        resultado = 0
        if opcao == "1":
            valor_01 = int(input("Informe o primeiro numero: "))
            valor_02 = int(input("Informe o segundo numero: "))
            resultado = operacoes.soma(valor_01, valor_02)
            print(resultado)
            print("1 - Sim")
            print("2 - Não")
            opcao_continuar = input("Deseja fazer mais alguma operação? ")
            if opcao_continuar == "1":
                continue
            else:
                print("Saindo do programa...")
                break
        elif opcao == "2":
            valor_01 = int(input("Informe o primeiro numero: "))
            valor_02 = int(input("Informe o segundo numero: "))
            resultado = operacoes.multiplicar(valor_01, valor_02)
            print(resultado)
            print("1 - Sim")
            print("2 - Não")
            opcao_continuar = input("Deseja fazer mais alguma operação? ")
            if opcao_continuar == "1":
                continue
            else:
                print("Saindo do programa...")
                break
        elif opcao == "3":
            valor_01 = int(input("Informe o primeiro numero: "))
            valor_02 = int(input("Informe o segundo numero: "))
            resultado = operacoes.divisao(valor_01, valor_02)
            print(resultado)
            print("1 - Sim")
            print("2 - Não")
            opcao_continuar = input("Deseja fazer mais alguma operação? ")
            if opcao_continuar == "1":
                continue
            else:
                print("Saindo do programa...")
                break
        elif opcao == "4":
            valor_01 = int(input("Informe o primeiro numero: "))
            valor_02 = int(input("Informe o segundo numero: "))
            resultado = operacoes.subtracao(valor_01, valor_02)
            print(resultado)
            print("1 - Sim")
            print("2 - Não")
            opcao_continuar = input("Deseja fazer mais alguma operação? ")
            if opcao_continuar == "1":
                continue
            else:
                print("Saindo do programa...")
                break
        elif opcao == "5":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. tente novamente.")

menu()