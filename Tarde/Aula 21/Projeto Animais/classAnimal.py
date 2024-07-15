class Animal:
    def __init__(self, nome, cor):
        self._nome = nome
        self._cor = cor
        
    def comer(self):
        print(f"O animal {self._nome} está comendo!")
    
    def correr(self):
        print(f"O animal {self._nome} está correndo!")
 
 
if __name__ == "__main__":
    a1 = Animal("Teste", "Branco") 
    a1.comer()
    a1.correr()          



    