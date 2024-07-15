#Criar o jogo do Pokemon
#1. Deve conter um menu para o jogador interagir
#2. Capturar Pokemon
#3. Ver Pokemons e Ver Pokemon específico
#4. Batalha Pokemon


#Crie um programa que importa os arquivos classTreinador, classPokemon e pokedex
#Esse programa deverá pedir o nome do jogador e oferecer uma escolha de 3 pokemons iniciais "Charmander", "Bulbasaur", "Squirtle". Você deverá usar essas informações para criar o objeto Treinador e imprimir seus pokemons na tela.
from classPokemon import Pokemon
from classTreinador import Treinador
from pokedex import pokedex
import random
import time
import os


def cria_nome():
    
    while (True):
    
        nomeTreinador = input("Digite seu nome: ")

        if nomeTreinador == '':
            print("Digite um nome válido!")
        else:
            break
    
    return nomeTreinador

print("Bem vindo ao mundo Pokemon. Eu sou o professor Carvalho e irei lhe guiar nessa jornada. Qual o seu nome?")

nomeTreinador = cria_nome()

# texto = f"É um prazer {nomeTreinador}. Para seguir nessa aventura você precisará de um parceiro. Fale com meu assistente para saber que pokemons temos disponíveis!"
# textoMontado = ""
# for letra in texto:
#     textoMontado+=letra
#     print(textoMontado)
#     time.sleep(1/60)
#     os.system('cls')
# print(textoMontado)
# time.sleep(1)
print(f"É um prazer {nomeTreinador}. Para seguir nessa aventura você precisará de um parceiro. Fale com meu assistente para saber que pokemons temos disponíveis!")
time.sleep(1)

print("Assistente: Olá, infelizmente você chegou tarde, restam apenas esses 3 pokemons. Qual deles deseja escolher para sua jornada?")
time.sleep(1)

pokemonsIniciais = {1: "Bulbasaur", 2:"Charmander", 3: "Squirtle"}
while True:
    print("Escolha seu pokemon inicial:")
    
    for chave,valor in pokemonsIniciais.items():
        print(f"{chave}. {valor}")
        
    escolha = int(input("Digite o número do pokemon desejado: "))
    
    pokemonEscolhido = pokemonsIniciais.get(escolha)
    if pokemonEscolhido == None:
        print("Esse pokemon não existe. Tente um novo número!")
        continue
    else:
        print("Seu pokemon escolhido foi", pokemonEscolhido)
        break

apelidoPokemon = input("Deseja mudar o nome do seu pokemon. Se sim, digite um novo nome: ")    

jogador = Treinador(nomeTreinador, [Pokemon(apelidoPokemon, pokemonEscolhido, 10)])

while True:
    
    print('''
    Menu:
    
    1. Ver meus Pokemons
    2. Capturar novo Pokemon
    3. Batalha Pokemon
    0. Sair      
          ''')
    
    op = input("Digite a opção desejada: ")
    
    if op == "1":
        jogador.ver_pokemons()
        
        escolhido = int(input("Digite o número do pokemon que deseja ver detalhes: "))
        
        jogador._pokemons[escolhido-1].mostrar_informacoes()
        
    elif op == "2":
        especieAleatoria = random.choice(list(pokedex.keys()))
        
        pokemonAleatorio = Pokemon("", especieAleatoria, random.randint(1, 20))
        
        pokemonAleatorio.mostrar_informacoes()
        
        capturar = input("Deseja capturar este pokemon?(Sim/Não)")
        
        if capturar == "Sim":
            print(f"Você capturou {pokemonAleatorio._especie}!")
            print("Pokemon adicionado ao time.")
            jogador._pokemons.append(pokemonAleatorio)
        else:
            print(f"{pokemonAleatorio._especie} fugiu!")
        
    elif op == "3":
        pass
    elif op == "0":
        print("Até a próxima...")
        break
    else:
        print("Opção inválida")
    
    input("Digite enter para continuar!")