'''
Crie uma função que aceite dois números e uma
operação (por exemplo, adição, subtração,

multiplicação, divisão) como argumentos e use funções
lambda para realizar a operação especificada. A função

deve retornar o resultado da operação.
'''
from functools import reduce

tipo_operacao = input("Informe o tipo de operação 1-SOMA 2-SUBTRAÇÃO 3-MULTIPLICAÇAO 4-DIVISÃO: ")
operador_01 = float(input("Digite o primeiro operador: "))
operador_02 = float(input("Digite o segundo operador: "))


def calculo(operacao, n1, n2):
    if operacao == "1":
        soma = reduce(lambda x, y: x + y, [n1, n2])
        return f"Resultado da soma: {soma}"

    if operacao == "2":
        subtracao = reduce(lambda x, y: x - y, [n1, n2])
        return f"Resultado da subtração: {subtracao}"

    if operacao == "3":
        multiplicacao = reduce(lambda x, y: x * y, [n1, n2])
        return f"Resultado da multiplicação: {multiplicacao}"
    
    if operacao == "4":
        divisao = reduce(lambda x, y: x / y, [n1, n2])
        return f"Resultado da divisão: {divisao}"

print(calculo(tipo_operacao, operador_01, operador_02))
