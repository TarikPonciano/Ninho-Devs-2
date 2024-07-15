from classAnimal import Animal

class Coelho (Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)
    def correr(self):
        print(f"O animal {self._nome} está saltando!")
    def cava_buraco(self):
        print(f"O animal {self._nome} está cavando um buraco!")