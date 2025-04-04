# Passo 1:
'''
Você precisa criar uma função chamada processador_texto que recebe uma string (o texto a ser manipulado).
Essa função terá como objetivo realizar operações sobre esse texto, como contar palavras, contar letras, 
inverter o texto, ou substituir palavras específicas.
'''
# Passo 2:
'''
Aqui, o desafio é aceitar múltiplos parâmetros opcionais, conhecidos como argumentos de palavra-chave (**kwargs). 
Isso significa que, além do texto, a função também receberá várias operações que o usuário pode escolher.
A função deverá usar expressões lambda (funções anônimas) para realizar as operações. Por exemplo, 
contar palavras seria uma função lambda que separa o texto em uma lista de palavras e conta a quantidade.
Você deverá tratar diferentes operações, como "contar_palavras", "contar_letras", etc., e executar a correspondente função lambda para cada uma.
'''
# Passo 3:
'''
Uma das operações, "substituir_palavra", requer argumentos adicionais: a palavra a ser substituída e a nova palavra que deve tomar seu lugar. 
Você pode usar **kwargs também para aceitar esses parâmetros.
O objetivo final é que a função aplique todas as operações que foram passadas e retorne o texto modificado.
'''
textos = "processador"
def processador_texto(texto):
    qtd_palavras = len(texto.split())
    print(f"{qtd_palavras}")

    qtd_letras = sum(1 for char in textos if char.isalpha())
    print(qtd_letras)

    texto_invertido = texto[::-1]
    print(texto_invertido)

processador_texto(textos)