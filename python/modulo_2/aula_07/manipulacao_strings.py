def funcao_manipular_string(texto):
    qtd_letras = sum(1 for char in texto if char.isalpha())
    texto_invertido = texto[::-1]
    eh_palindromo = "eh um palíndromo" if texto_invertido == texto else "não é um palíndromo"
    return f"qtd de letras: {qtd_letras} \neh um palídromo?: {eh_palindromo}"