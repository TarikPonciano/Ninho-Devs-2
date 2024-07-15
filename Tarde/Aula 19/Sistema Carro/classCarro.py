#Crie uma classe que representa um carro. Os atributos dele serão Modelo, Ano, Placa, Fabricante, Velocidade.

# Crie um método acelerar que aumenta a velocidade do carro.

# Crie um método parar que zera a velocidade do carro

# Crie um método ver_informacoes que imprime as informações do carro e informa se ele está parado ou em movimento.

# No arquivo main.py crie 3 carros diferentes, acelere eles para velocidades diferentes e exiba suas informações na tela. Lembrar de dar import.

class Carro:
    def __init__(self, modelo, ano, fabricante, placa):
        self.modelo = modelo
        self.ano = ano
        self.fabricante = fabricante
        self.placa = placa
        self.velocidade = 0
        self.velocidadeMaxima = 200
        self._velocidade = 0
        self._velocidadeMaxima = 200
    def acelerar(self, aumento):
        if self.velocidade + aumento > self.velocidadeMaxima:
            print("Não é possível acelerar mais!")
        else:
            self.velocidade += aumento
            print("O carro está acelerando...")
        print(f"Velocidade atual do carro: {self.velocidade}km/h")
    def frear(self):
        self.velocidade = 0
        print("O carro está parando...")
        print(f"Velocidade atual do carro: {self.velocidade}km/h")
        print("O carro está parado!")
    def ver_informacoes(self):
        print(f'''
    Modelo: {self.modelo}
    Ano: {self.ano}
    Fabricante: {self.fabricante}
    Placa: {self.placa}
              
    Velocidade: {self.velocidade}km/h''')
        if self.velocidade > 0:
            print("Situação: Em movimento")
        else:
            print("Situação: Parado")
        # Situação: {"Em movimento" if self.velocidade>0 else "Parado"}        


carro1 = Carro("Ferrari GT", 1995, "Ferrari", "ZZZ-2B22")

print(carro1.velocidade)
print(carro1._velocidade)