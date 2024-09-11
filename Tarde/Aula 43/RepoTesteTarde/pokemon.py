class Pokemon():
    def __init__(self, especie, tipo, forca):
        self.especie = especie
        self.tipo = tipo
        self.forca = forca
        
    def pokedex(self):
        print(f'''
    Espécie: {self.especie}          
    Tipo: {self.tipo}
    Força: {self.forca}         
              ''')
        
def batalha(pokemon1, pokemon2):
    
    if (pokemon1.forca > pokemon2.forca):
        print(f"{pokemon1.especie} venceu a batalha!")
    elif (pokemon2.forca > pokemon1.forca):
        print(f"{pokemon2.especie} venceu a batalha!")
    else:
        print("Empate!")        

poke1 = Pokemon("Charmander", "Fogo", 500)
poke2 = Pokemon("Squirtle", "Água", 400)
poke3 = Pokemon("Bulbasaur", "Grama", 600)

poke1.pokedex()
poke2.pokedex()

batalha(poke1, poke3)
batalha(poke2,poke1)