'''
Crie um classe chamada cachorro com os atributos:

nome, raça, idade
'''

class Cachorro:
    def __init__(self, nome, raca, idade):
        self.nome = nome
        self.raca = raca
        self.idade = idade

    def identidade_canina(self):
        identidade = {
            "nome" : self.nome,
            "raca" : self.raca,
            "idade" : self.idade
        }

        return identidade
    
dados_do_cachorro = Cachorro("Pituca","Poodle", "12 anos")
print(dados_do_cachorro.identidade_canina())



