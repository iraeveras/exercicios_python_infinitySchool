# criando um objeto
class Carro:
    # Atributos
    def __init__(self, modelo, cor, placa, motor, ano):
        self.modelo = modelo
        self.cor = cor
        self.placa = placa
        self.motor = motor
        self.ano = ano
        self.velocidade = 0

    # Métodos
    def ligar(self):
        return "carro ligado"
    
    def buzinar(self):
        return "buzina acionada"
    
    def frear(self):
        return "break"


uno_com_escada = Carro("uno","preto","pcf-9521","1.8","2000")
print(uno_com_escada.buzinar())