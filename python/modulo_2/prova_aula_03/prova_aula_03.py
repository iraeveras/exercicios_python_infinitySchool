'''
Crie um dicionário para armazenar o nome e o preço de cinco produtos. Peça ao usuário para inserir o nome de cada produto e o respectivo preço. À medida que o usuário fornece os dados, 
armazene cada produto como uma chave no dicionário e o preço como o valor associado a essa chave. 
Após a inserção de todos os produtos e preços, calcule o valor total da compra somando todos os preços armazenados no dicionário. Por fim, exiba o valor total da compra.
'''

produtos = dict()
soma_valor_produtos = 0

for i in range(5):
    nome_produto = input("Informe o nome do produto: ")
    preco_produto = float(input("Informe o valor do produto: "))
    produtos[nome_produto] = preco_produto
    soma_valor_produtos += preco_produto

for chave, valor in produtos.items():
    print(f"{chave}: {valor}")

print(f"Valor total dos produtos: R$ {soma_valor_produtos}")
    