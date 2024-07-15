from classAnimal import Animal

class Coelho(Animal):
    def __init__(self, nome, idade):
        super().__init__(nome, "Branco")
        self._idade = idade
    def correr(self):
        print(f"O animal {self._nome} está pulando!")
