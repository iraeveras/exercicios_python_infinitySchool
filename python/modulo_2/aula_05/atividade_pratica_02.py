'''
Crie um programa que define uma função

calcular_area_retangulo que recebe dois argumentos,
comprimento e largura de um retângulo, e retorna a
área desse retângulo. Em seguida, o programa deve
solicitar ao usuário que insira o comprimento e a

largura e imprimir a área calculada.
'''

def area_retangulo(largura, comprimento):
    area = largura * comprimento
    return area

largura = float(input("Digite o tamanho da largura: "))
comprimento = float(input("Digite o tamanho da comprimento: "))


print(area_retangulo(largura, comprimento))