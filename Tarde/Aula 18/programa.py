class Pessoa:
    
    def __init__(self, nome, idade, endereco, telefone):
        self.nome = nome
        self.idade = idade
        self.endereco = endereco
        self.telefone = telefone
        if telefone[0] == "5":
            self.cidade = "Caucaia"
        else:
            self.cidade = "Fortaleza"
    def mostrar_informacoes(self):
        print(f'''
        Nome: {self.nome}
        Idade: {self.idade}
        Endereço: {self.endereco}
        Telefone: {self.telefone}      
        Cidade: {self.cidade}''')

p1 = Pessoa("Joana", 20, "Rua A", "12345")

p2 = Pessoa("Marquinhos", 25, "Rua B", "54321")

p1.mostrar_informacoes()
p2.mostrar_informacoes()