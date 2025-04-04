numero_de_alunos = int(input("Digite o numero de alunos: "))

soma_media = 0

for i in range(numero_de_alunos):
    print(i)
    aluno = input("Informe o nome do aluno: ")
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    nota3 = float(input("Digite a terceira nota: "))

    media = (nota1 + nota2 + nota3) / 3
    soma_media += media

    if media >= 7.0:
        situacao = "Aprovado"
    else:
        situacao = "Reprovado"
    
    print(f"\nNome: {aluno}")
    print(f"Notas: {nota1, nota2, nota3}")
    print(f"Média: {media}")
    print(f"Situação: {situacao}")

media_geral = soma_media / numero_de_alunos
print(f"Média geral da turma: {media_geral}")


