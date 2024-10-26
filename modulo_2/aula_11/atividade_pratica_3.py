'''
Crie uma classe Empresa que permita gerenciar
funcionários. Os funcionários devem ter informações
como nome, cargo e salário. A empresa deve ser capaz

de adicionar, remover e listar funcionários.
'''
funcionarios = {}

class Empresa:
    def __init__(self):
        self.funcionarios = []



    def adicionar_funcionario(self):
        funcionario = {
            "nome":input("Digite o nome do funcionário: "),
            "cargo":input("Digite o cargo do funcionário: "),
            "salario":float(input("Digite o salário do funcionário: "))
        }

        self.funcionarios.append(funcionario)
        print("Funcionario adicionado com sucesso!")
        self.listar_funcionario()

    def listar_funcionario(self):
        for func in self.funcionarios:
            print(f"Funcionário: {func["nome"]}, Cargo: {func["cargo"]}, Salário: {func["salario"]}")
            
    
    def remover_fucnionario(self):
        nome_funcionario = input("Digite o nome do funcionario: ")
        for func in self.funcionarios:
            if func["nome"] == nome_funcionario:
                self.funcionarios.remove(func)

empresa = Empresa()
print(empresa.adicionar_funcionario())


        
    
