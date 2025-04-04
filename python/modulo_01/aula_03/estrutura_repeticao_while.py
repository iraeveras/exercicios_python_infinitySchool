
numero_aleatorio = 4
tentativas = 0
chance = 3
print(f"você tem {chance} tentativa(s)")

while tentativas < 3:
    palpite = int(input("Adivinhe o numero [entre 1 e 10]: "))
    tentativas += 1
    chance -= 1
    print(f"você tem mais {chance} tentativa(s)")
    if palpite == numero_aleatorio:
        print("parabéns! você acertou.")
        break
else:
    print(f"Infelizmente você não conseguiu, mas não desanime continue tentando. o numero era {numero_aleatorio}")