import random
from pokedex import pokedex

class Pokemon:
    def __init__(self,apelido, especie, level):
        
        if pokedex.get(especie)== None:
            especie = "Pikachu"
            
        self._apelido = apelido
        self._especie = especie
        
        if level == None or level == 0:
            self._level = 1
        else:
            if level > 99:
                self._level = 99
            else:
                self._level = level
        
        self._hp = pokedex[especie]["hp"]
        
        self._defesa = pokedex[especie]["defesa"]
        
        self._atk = pokedex[especie]["atk"]
        
        self._definir_atributos()
        
        
    
    def _definir_atributos(self):
        self._hp += (10 * random.randint(0,self._level)) 
        
        self._defesa += (3 * random.randint(0,self._level))
        
        self._atk += (5 * random.randint(0,self._level))
    
    def mostrar_informacoes(self):
        
        print(f'''
---------------Atributos---------------
    Apelido: {self._apelido}
    Espécie: {self._especie}
    Level: {self._level}
    HP: {self._hp}
    Ataque: {self._atk}
    Defesa: {self._defesa}
----------------------------------------
    ''')
        
            
if __name__ == "__main__":
    nomesPokemons = list(pokedex.keys())
    nomeAleatorio = random.choice(nomesPokemons)
    pokemon1 = Pokemon("Jotinha", "Dragonite", 10)
    pokemonAleatorio = Pokemon(nomeAleatorio, nomeAleatorio, random.randint(1,99))
    
    
    pokemonAleatorio.mostrar_informacoes()