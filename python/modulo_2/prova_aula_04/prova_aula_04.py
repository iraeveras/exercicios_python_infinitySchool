'''
Crie uma função chamada media que receberá três números como argumentos. 
Esta função deve calcular a média aritmética desses três números. Para fazer isso, some os três números e, 
em seguida, divida o resultado por três. Por fim, a função deve retornar o valor da média aritmética calculada.
'''

def media (n1, n2, n3):
    soma = n1 + n2 + n3
    media = soma / 3
    print(media)


valor_01 = float(input("Digite a primeira nota: "))
valor_02 = float(input("Digite a segunda nota: "))
valor_03 = float(input("Digite a terceira nota: "))

media(valor_01,valor_02,valor_03)