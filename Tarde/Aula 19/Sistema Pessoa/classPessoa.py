class Pessoa:
    def __init__(self, nome, genero, cpf, ativo):
        self.nome = nome
        self.genero = genero
        self.cpf = cpf
        self.ativo = ativo
    def desativar(self):
        self.ativo = False
        print(f"A pessoa {self.nome} foi desativada com sucesso!")
         

if __name__ == "__main__":
    p1 = Pessoa("Zeca", "M", "12345", True)

    p1.desativar()

    print(p1.ativo)