class Animal:
    def __init__(self, nome, cor):
        self._nome = nome
        self._cor = cor
    # def get_nome(self):
    #     return self._nome
    # def set_nome(self,novoNome):
    #     self._nome = novoNome
    def comer(self):
        print(f"O animal {self._nome} está comendo!")
        
    def correr(self):
        print(f"O animal {self._nome} está correndo!")
        