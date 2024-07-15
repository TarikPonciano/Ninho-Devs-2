class Funcionario:
    def __init__(self, nome, cpf, salario):
        self._nome = nome
        self._cpf = cpf
        self._salario = salario
    def mostrar_informacoes(self):
        print(f'''
        Nome: {self._nome}
        CPF: {self._cpf}
        Salário: R$ {self._salario}      
              ''')        
class Gerente(Funcionario):
    def __init__(self, nome, cpf, salario, setor):
        super().__init__(nome, cpf, salario)
        self._setor = setor
    def ver_setor(self):
        print(f"Setor: {self._setor}")
        
f1 = Funcionario("Zeca", "12345", 3000)
f1.mostrar_informacoes()


f2 = Gerente("Joaquina", "54321", 5000, "T.I")
f2.mostrar_informacoes()
f2.ver_setor()



#Crie uma classe veículo que possui atributos à sua escolha e possui o método mover. Crie as subsclasses Carro, Barco, Avião e instancie um objeto de cada subclasse e execute o método mover.
# Ex: barco.mover() > "O barco está se movendo!"

class Veiculo:
    def __init__(self, velocidade, rodas, tipo, cor):
        self._velocidade = velocidade
        self._rodas = rodas
        self._tipo = tipo
        self._cor = cor
    def mover(self):
        print(f"O veículo {self._cor} {self._tipo} com {self._rodas} rodas está se movimentando com {self._velocidade}km/h")

class Carro(Veiculo):
    def __init__(self, velocidade, cor):
        super().__init__(velocidade, 4, "Terrestre", cor)
    def mover(self):
        print(f"O veículo {self._cor} {self._tipo} com {self._rodas} rodas está se deslocando por terra com {self._velocidade}km/h")
        
class Barco(Veiculo):
    def __init__(self, velocidade, cor):
        super().__init__(velocidade, 0, "Marítimo", cor)
    def mover(self):
        print(f"O veículo {self._cor} {self._tipo} com {self._rodas} rodas está se movimentando por água com {self._velocidade}km/h")
        
class Aviao(Veiculo):
    def __init__(self, velocidade, cor):
        super().__init__(velocidade, 3, "Aéreo", cor)
    def mover(self):
        print(f"O veículo {self._cor} {self._tipo} com {self._rodas} rodas está voando com {self._velocidade}km/h")
        
v1 = Carro(100, "Preto")
v2 = Barco(80, "Branco")
v3 = Aviao(400, "Azul")

v1.mover()
v2.mover()
v3.mover()
# class Pokemon:
#     def __init__(self, especie, regiao, numero):
#         self._especie = especie
#         self._regiao = regiao
#         self._numero = numero
#     def pokedex(self):
#         print(f'''
#     Pokemon #{self._numero}
#     Espécie: {self._especie}
#     Região: {self._regiao}          
#               ''')
# class Agua(Pokemon):
#     def __init__(self, especie, regiao, numero):
#         super().__init__(especie, regiao, numero)
# class Fogo(Pokemon):
#     def __init__(self, especie, regiao, numero):
#         super().__init__(especie, regiao, numero)
# class Eletrico(Pokemon):
#     def __init__(self, especie, regiao, numero):
#         super().__init__(especie, regiao, numero)

# squirtle = Agua("Squirtle", "Kanto", "4")
# charmander = Fogo("Charmander", "Kanto", "7")
# pikachu = Eletrico("Pikachu", "Kanto", "10")

# squirtle.pokedex()

# charmander.pokedex()

# pikachu.pokedex()
