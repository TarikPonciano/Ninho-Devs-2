class Animal:
    def __init__(self, nome, cor,genero):
        self._nome = nome
        self._cor = cor
        self._genero = genero
    
    def comer(self):
        if self._genero == "Macho":
            print(f"O {self._nome} está comendo!!!!")
        else:
            print(f"A {self._nome} está comendo!!!!")
            
    def fazer_som(self):
        if self._genero == "Macho":
            print(f"O {self._nome} está fazendo barulho!!!!")
        else:
            print(f"A {self._nome} está fazendo barulho!!!!")
            

class Cachorro(Animal):
    def __init__(self, nome, cor, genero):
        super().__init__(nome, cor, genero)
    def fazer_som(self):
        super().fazer_som()
        print("AU AU")

class Gato(Animal):
    def __init__(self, nome, cor,genero):
        super().__init__(nome, cor, genero)
    
    def fazer_som(self):
        super().fazer_som()
        print("Miau Miau")
        
class Coelho(Animal):
    def __init__(self, nome, cor, genero):
        super().__init__(nome, cor, genero)
    def fazer_som(self):
        super().fazer_som()
        print("SQUEAK SQUEAK")        
        
a2 = Cachorro("Bilu", "Caramelo", "Macho")
a3 = Coelho("Hannah", "Branco", "Fêmea")
a4 = Gato("Lunna", "Tigrado", "Fêmea")

a2.comer()
a3.comer()
a4.comer()

a2.fazer_som()
a3.fazer_som()
a4.fazer_som()
