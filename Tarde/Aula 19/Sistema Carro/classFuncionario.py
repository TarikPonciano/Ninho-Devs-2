class Funcionario:
    def __init__ (self, nome, cargo, cpf, salario, departamento):
        self.nome = nome
        self.senha = "senha"
        self.cargo = cargo
        self.cpf = cpf
        self.salario = salario
        self.departamento = departamento
        self.ativo = True
        
    #getters and setters
    def getNome(self, senha):
        if senha == self.senha:
            return self.nome
        else:
            print("INFORMAÇÃO NEGADA!")
    def setNome(self, novoNome,senha):
        if senha == self.senha:
            self.nome = novoNome
        else:
            print("MUDANÇA NÃO AUTORIZADA")
            
    def setCpf(self, novoCpf):
        if len(novoCpf) == 11 and novoCpf.isdigit():
            self.cpf = novoCpf
        else:
            print("CPF INFORMADO É INVÁLIDO")
               
f1 = Funcionario("João", "Gerente", "12345678910", 5000, "TI")

print(f1.getNome("senha"))


funcionarios = [Funcionario("Arthur", "Analista", "54321", 4000, "TI")]
f2 = Funcionario("James", "Vendedor" , "12345", 10000, "RH")
f3 = Funcionario("Teste", "Teste", "Teste" , "Teste", "Teste")

funcionarios.append(f2)
funcionarios.append(f3)

for f in funcionarios:
    print(f.getNome("senha"))