#Crie uma classe Funcionário que contém os atributos Nome, Cargo, Salário, CPF
class Funcionario():
    def __init__(self, nome, cargo, salario, cpf):
        self.nome = nome
        self.cargo = cargo
        self.salario = salario
        self.cpf = cpf
#Instanciar 3 objetos da classe funcionário
f1 = Funcionario("José", "Gerente", 7000, "1234")
f2 = Funcionario("Joana", "Dev Web", 12000, "2345")
f3 = Funcionario("Zeca", "Pagodeiro", 5300, "3456")
#Imprimir o nome dos 3 funcionários
print(f1.nome)
print(f2.nome)
print(f3.nome)
#Imprimir o funcionário com o maior salário
listaFuncionarios = [f1,f2,f3]

maiorFuncionario = listaFuncionarios[0]

for f in listaFuncionarios:
    if f.salario > maiorFuncionario.salario:
        maiorFuncionario = f
        
print(f'''
    Maior Salário:
    
    Nome - {maiorFuncionario.nome}
    Salário - R$ {maiorFuncionario.salario}
      ''')
        