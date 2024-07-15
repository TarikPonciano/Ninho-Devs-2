from classPokemon import Pokemon
from pokedex import pokedex
import random

class Treinador:
    def __init__(self, nome:str, pokemons:list[Pokemon]):
        self._nome = nome
        self._pokemons = pokemons #[poke1, poke2]
    def ver_pokemons(self):
        
        for n,p in enumerate(self._pokemons):
            
            print(f"{n+1}. {p._especie}")
            
            

if __name__ == "__main__":
    
    jogador = Treinador("Tarik", [Pokemon("", "Pikachu", 10)])
    
    for i in range(5):
        aleatorio = random.choice(list(pokedex.keys()))
        pokemonAleatorio = Pokemon("", aleatorio, random.randint(1,99))   
        jogador._pokemons.append(pokemonAleatorio)
        
    jogador.ver_pokemons()
    