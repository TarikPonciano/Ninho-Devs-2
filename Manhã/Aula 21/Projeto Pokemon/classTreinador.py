from classPokemon import Pokemon
# from typing import List

class Treinador:
    def __init__(self, nome:str, pokemons:list[Pokemon]):
        self._nome = nome
        self._pokemons = pokemons
    
    def ver_pokemons(self):
        print("Meus Pokemons: ")
        contador = 1
        for pokemon in self._pokemons: 
            print(f"{contador}. {pokemon._apelido}")
            
            contador += 1 
                   
            
if __name__ == "__main__":
    treinador1 = Treinador("Ash", [Pokemon("Charmander", "Charmander", 10), Pokemon("Squirtle", "Invalido", 20)])
    
    treinador1._pokemons[1].mostrar_informacoes()
