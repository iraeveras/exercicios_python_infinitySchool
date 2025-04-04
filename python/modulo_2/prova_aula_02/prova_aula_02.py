'''
Crie um dicionário que irá armazenar informações de um contato, incluindo o nome, o telefone e o email. Peça ao usuário para fornecer esses dados, solicitando que ele insira o nome do contato, 
o número de telefone e o endereço de email. 
Após coletar todas as informações necessárias, exiba o conteúdo do dicionário, mostrando todas as informações do contato inserido pelo usuário.
'''

contado = {
    "nome": "",
    "telefone": "",
    "email": ""
}

nome = input("Informe seu nome: ")
telefone = input("Informe seu telefone: ")
email = input("Informe seu email: ")

contado = {
    "nome": nome,
    "telefone": telefone,
    "email": email
}

print(contado)