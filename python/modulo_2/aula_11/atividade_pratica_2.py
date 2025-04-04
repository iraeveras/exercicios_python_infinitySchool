'''
Crie um classe chamada pessoa com os atributos: nome,

idade, peso, gênero
'''

class Pessoa:
    def __init__(self, nome, idade, peso, genero):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.genero = genero

    def pessoa_infos(self):
        info = {
            "nome":self.nome,
            "idade":self.idade,
            "peso":self.peso,
            "genero":self.genero
        }

        return f"{info["nome"]} tem {info['idade']} anos e seu pêso é {info['peso']}kg e diz que seu gênero é {info['genero']}"
        
pessoa = Pessoa("Carlos", 25, 82.10, "masculino")
print(pessoa.pessoa_infos())