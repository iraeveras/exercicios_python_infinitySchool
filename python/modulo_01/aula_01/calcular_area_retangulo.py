base = float(input("Digite a largura da base: "))
altura = float(input("Digite a altura: "))

area = 0

if base and altura:
    area = base * altura
    print(f"A área do retângulo é: {area}")
else:
    print("Você precisa informar o valor da largura e altura")
