import random
from pokedex import pokedex

class Pokemon:
    def __init__(self, apelido, especie, level):
        
        if apelido == "" or apelido == None:
            self._apelido = especie
        else:
            self._apelido = apelido
        
        self._especie = especie
        
        if level <= 0:
            self._level = 1
        elif level >99:
            self._level = 99
        else:
            self._level = level
            
        self._hp = pokedex[especie]["hp"]
        self._atk = pokedex[especie]["atk"]
        self._defesa = pokedex[especie]["defesa"]
        
        self._definir_atributos(self._level)
        
    def subir_nivel(self):
        
        hpAntigo = self._hp
        atkAntigo = self._atk
        defesaAntigo = self._defesa
        
        print("Parabéns seu pokemon subiu de nível.")
        self._level += 1
        print(f"Seu {self._especie} agora é nível {self._level}")
        self._definir_atributos(1)
        
        print(f'''
    HP: {hpAntigo} > {self._hp} (+{self._hp - hpAntigo})          
    Ataque: {atkAntigo} > {self._atk} (+{self._atk - atkAntigo})
    Defesa: {defesaAntigo} > {self._defesa} (+{self._defesa - defesaAntigo})          
              ''')
        
    def _definir_atributos(self, levels):
        
        
        self._hp += 10 * random.randint(0,levels)
        self._atk += 5 * random.randint(0,levels)
        self._defesa += 3 * random.randint(0,levels)
        
        
                
    def mostrar_informacoes(self):
        print(f'''
    ----------Atributo-----------
    Apelido: {self._apelido}
    Espécie: {self._especie}
    Level: {self._level}
    HP: {self._hp}
    Ataque: {self._atk}
    Defesa: {self._defesa}          
    ------------------------------
              ''')    
        
if __name__ == "__main__":
    
    p1 = Pokemon("", "Pikachu", 20)
    p2 = Pokemon("", "Moltres", 30)
    p3 = Pokemon("", "Squirtle", 20)
    p4 = Pokemon("", "Mew", 20)
    
    p1.mostrar_informacoes()
    p2.mostrar_informacoes()
    p3.mostrar_informacoes()
    p4.mostrar_informacoes()
   