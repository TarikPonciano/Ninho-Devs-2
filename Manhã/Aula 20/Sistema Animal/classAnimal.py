class Animal:
    def __init__(self,nome, cor, genero):
        self._nome = nome
        self._cor = cor
        self._genero = genero
    def comer(self):
        
        if self._genero == "Masculino":
            print(f"O {self._nome} está comendo!!!!")
        else:
            print(f"A {self._nome} está comendo!!!!")

class Coelho(Animal):
    def __init__(self, nome, cor, genero):
        super().__init__(nome, cor, genero)
        
class Gato(Animal):
    def __init__(self, nome, cor, genero):
        super().__init__(nome, cor, genero)

class Cachorro(Animal):
    def __init__(self, nome, cor, genero):
        super().__init__(nome, cor, genero)
            
a1 = Coelho("Fluffy", "Branco", "Feminino")
a2 = Gato("Luna", "Branco", "Feminino")
a3 = Cachorro("Bilu", "Caramelo", "Masculino")

print(a1._nome)
print(a1._cor)
print(a1._genero)
a1.comer()
a2.comer()
a3.comer()