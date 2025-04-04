
# lista_misturada = ('1','usuario', 'false', 'usuario', 'false', 'animal', 'True')

# contador = 0
# for i in range(1, len(lista_misturada)):
#     if lista_misturada[i] == 'false':
#         contador += 1
#         print(lista_misturada[i], contador, i)

informacoes_palestra = (
    ("João", "Automação em Python", "Infinity School"),
    ("Antonio", "Frontend com HTML e CSS", "Infinity School"),
    ("José", "Logica de programação com Javascript", "Infinity School"),
)

# print(informacoes_palestra[0])

contador = 0

for i in range(0, len(informacoes_palestra)):
    contador += 1
    for j in informacoes_palestra[i]:
        print(j, contador)
    # print( i, informacoes_palestra[i], contador)
    
    

