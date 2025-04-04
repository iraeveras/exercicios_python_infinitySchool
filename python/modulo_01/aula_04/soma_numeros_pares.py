inicio_intervalo = int(input("Digite um numero para determinar o inicio do intervalo: "))
fim_intervalo = int(input("Digite um numero para determinar o fim do intervalo: "))
soma = 0
for i in range(inicio_intervalo, fim_intervalo + 1):
    if i % 2 == 0:
        soma += i
if soma == 0:
    print("Não há numeros pares no intervalo")
else:
    print(f"A soma dos numeros pares no intervalo é: {soma}")