#Crie uma classe que representa um carro. Os atributos dele serão Modelo, Ano, Placa, Fabricante, Velocidade.
# Crie um método acelerar que aumentar a velocidade do carro.
# Crie um método parar que zera a velocidade do carro
# Crie um método ver_informacoes que imprime as informações do carro e informa se ele está parado ou em movimento.
# Na pasta main crie 3 carros diferentes, acelere eles para velocidades diferentes e exiba suas informações na tela. Lembrar de dar import.
class Carro:
    def __init__(self, modelo, ano, placa, fabricante):
        self.modelo = modelo
        self.ano = ano
        self.placa = placa
        self.fabricante = fabricante
        self.velocidade = 0
        
    def acelerar(self, aumento):
        self.velocidade += aumento
        print("O carro está acelerando...")
        print(f"A velocidade atual é: {self.velocidade}km/h")
    def frear(self):
        self.velocidade = 0
        print("O carro está freando!")
        print(f"A velocidade atual é: {self.velocidade}km/h")
        print("O carro está parado!")
    def ver_informacoes(self):
        
        print(f'''
    Modelo: {self.modelo}
    Fabricante: {self.fabricante}          
    Ano: {self.ano}
    Placa: {self.placa}
    Velocidade Atual: {self.velocidade}km/h          
              ''')
        if self.velocidade >0:
            print("Status: Em movimento")
        else:
            print("Status: Parado")
    
    def nome_carro(self):
        print(f"{self.modelo} - {self.ano} - {self.fabricante}")
        
    #getters and setters
    def getModelo(self):
        
        return self.modelo
    
    def setModelo(self, novoModelo):
        self.modelo = novoModelo
    
    def getPlaca(self):
        return self.placa
    def setPlaca(self, novaPlaca):
        if len(novaPlaca) == 8 and novaPlaca[5].isalpha() :
            self.placa = novaPlaca
        else:
            print("PLACA NO FORMATO ERRADO!")        
    
          
    
car1 = Carro("HB-20", 2023, "HYB-20I3", "Hyundai")



car1.setModelo("Onyx")
print(car1.getModelo())

car1.setPlaca("XYZ-1C34")
print(car1.getPlaca())
