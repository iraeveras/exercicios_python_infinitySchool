# ATIVIDADE 1
'''
Crie uma função que receba um nome e imprima uma
saudação personalizada.
'''
def saudacao(nome):
    print(f"olá, {nome}")

saudacao("Julia")


# ATIVIDADE 2
'''
Crie uma função que receba um horário e imprima
"Bom dia!", "Boa tarde!" ou "Boa noite!" conforme o horário.
'''
def comprimento(horario):
    if horario < 12:
        print(f"Bom dia")
    elif horario < 18:
        print(f"Boa tarde")
    else:
        print(f"Boa noite")

horario = 12
comprimento(horario)


# ATIVIDADE 3
'''
Crie uma função que receba dois números e retorne a
soma deles.
'''
def soma(num1, num2):
    return f"Soma: {num1 + num2}"

print(soma(12,5))


# ATIVIDADE 4
'''
Crie uma função que receba dois números e retorne a
subtração do primeiro pelo segundo.
'''
def subtracao(num1, num2):
    return f"Subtração: {num2 - num1}"

print(subtracao(7,2))


# ATIVIDADE 5
'''
Crie uma função que receba dois números e retorne a
multiplicação deles.
'''
def multiplicacao(num1, num2):
    return f"Multiplicação: {num1 * num2}"

print(multiplicacao(12,8))