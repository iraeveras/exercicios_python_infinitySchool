# DESAFIO PRÁTICO
'''
Calculadora

Crie uma calculadora com opções de soma, multiplicação,
subtração, divisão e sair.

(Ela deverá funcionar infinitamente, até que o usuário decida sair da calculadora.)

Utilize funções de rotina para cada operação e funções de unidade lógica para
realizar os cálculos.

Dica:
Utilize de condicionais e Laços de Repetição para realizar esse
exercício.
'''
def calculadora(lista):
    return f"{lista}"

lista = list()
resultado = 0

while True:
    entrada = input("O que voce deseja fazer, operação de 1-SOMA, 2-MULT, 3-DIVISAO, 4-SUBTRAÇÃO OU 5-SAIR? ")
    if entrada == "1" or entrada == "2" or entrada == "3" or entrada == "4" or entrada == "5":       
        if entrada == "5":
            break
        
        if entrada == "1":
            print("Voçê escolheu calculo de soma")
            while True:
                for i in range(2):
                    num = float(input("Digite um numero: "))
                    resultado += num
                    lista.append(resultado)
                opcao =  input("Deseja 1-continuar ou 2-parar? ")
                while opcao == "1":
                    num = float(input("Digite um numero: "))
                    opcao =  input("Deseja 1-continuar ou 2-parar? ")
                    resultado += num
                    lista.append(resultado)
                else:
                    break
            print(f"{calculadora(resultado)}")            
        
        if entrada == "2":
            print("Voçê escolheu calculo de multiplicação")
            multiplicador = float(input("Digite o multiplicador: "))
            multiplicando = float(input("Digite o multiplicando: "))
            resultado = (multiplicador * multiplicando)
            lista.append(resultado)
            print(f"{calculadora(resultado)}")
            resultado = 0

        if entrada == "3":
            print("Voçê escolheu calculo de divisão")
            divisor = float(input("Digite o divisor: "))
            dividendo = float(input("Digite o dividendo: "))
            resultado = (divisor / dividendo)
            lista.append(resultado)
            print(f"{calculadora(resultado)}")
            resultado = 0
        
        if entrada == "4":
            print("Voçê escolheu calculo de subtração")
            minuendo = float(input("Digite o minuendo: "))
            subtraendo = float(input("Digite o subtraendo: "))
            resultado = (minuendo - subtraendo)
            lista.append(resultado)
            print(f"{calculadora(resultado)}")
            resultado = 0
    else:
        print("Opções inválidas.")
        continue





