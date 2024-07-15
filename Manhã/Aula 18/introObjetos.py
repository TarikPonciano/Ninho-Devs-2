#Criar uma classe Pessoa que contenha as informações Nome, Idade, Endereço e Telefone
#Crie 3 objetos do tipo Pessoa
#Exiba o nome dessas 3 pessoas na tela

class Pessoa():
    def __init__(self, nome:str, idade:int, endereco:str, telefone:str):
                        
        self.nome = nome
        self.idade = idade
        self.endereco = endereco
        self.telefone = telefone
        
p1 = Pessoa("Fulano", 24, "Rua A", "12345")
p2 = Pessoa("Ciclano", 30, "Rua B", "54321")
p3 = Pessoa("Beltrano", 28, "Rua C", "65478")

print(p1.nome)
print(p2.nome)
print(p3.nome)