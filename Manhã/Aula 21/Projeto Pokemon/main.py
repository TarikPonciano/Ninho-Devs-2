#Fazer um jogo do Pokemon com as funcionalidades:

#1. Menu para escolha do que será feito
#2. Batalha pokemon
#3. Capturar pokemon
#4. Ver pokemons e ver pokemon individual

#Crie um programa que importa os arquivos classTreinador, classPokemon e pokedex
#Esse programa deverá pedir o nome do jogador e oferecer uma escolha de 3 pokemons iniciais "Charmander", "Bulbasaur", "Squirtle". Você deverá usar essas informações para criar o objeto Treinador e imprimir seus pokemons na tela.
from classPokemon import Pokemon
from classTreinador import Treinador
from pokedex import pokedex
import random

def criar_nome():
    while True:
    
        nome = input("Digite seu nome: ")
        
        if nome == "":
            print("Não entendi. Poderia repetir?")
            
        else:
            return nome

print("Bem vindo ao mundo Pokemon. Eu sou o professor Carvalho e irei lhe guiar na sua nova aventura.")

nome = criar_nome()
    
while True:
    
    pokemonsIniciais = {1: "Bulbasaur", 2: "Charmander", 3: "Squirtle"}

    print("Escolha seu pokemon inicial:")

    for chave,valor in pokemonsIniciais.items():
        print(f"{chave}. {valor}")

    escolha = int(input("Escolha o número do pokemon desejado: "))
    
    nomePokemon = pokemonsIniciais.get(escolha)
    
    if nomePokemon == None:
        print("Número inválido. Selecione um pokemon válido!")
    else:
        break
    
pokemonInicial = Pokemon(nomePokemon, nomePokemon, 1)

treinador = Treinador(nome, [pokemonInicial])

while True:
    
    print('''
    Bem vindo Treinador!
    Escolha uma opção:
    
    1. Ver meus Pokemons
    2. Capturar Pokemon
    3. Batalha Pokemon
    0. Sair do Jogo      
          
          ''')
    
    op = input("Digite a opção desejada: ")
    
    if op == "1":
        while True:
            treinador.ver_pokemons()
            escolha = int(input("Digite o número do pokemon que deseja ver mais detalhes:"))
            
            if escolha == 0:
                break
            elif escolha > len(treinador._pokemons) or escolha < 0:
                print("Escolha um número válido!")
            else:
                treinador._pokemons[escolha-1].mostrar_informacoes()
                break
        
    elif op == "2":
        especieAleatoria = random.choice(list(pokedex.keys()))
        pokemonAleatorio = Pokemon(especieAleatoria, especieAleatoria, random.randint(1, 20))
        pokemonAleatorio.mostrar_informacoes()
        
        capturar = input(f"Deseja capturar este {pokemonAleatorio._especie}?")
        
        if (capturar == "Sim"):
            print("Pokemon adicionado ao seu time!")
            treinador._pokemons.append(pokemonAleatorio)
        else:
            print(f"{pokemonAleatorio._especie} fugiu!")
        
    elif op == "3":
        pass
    elif op == "0":
        print("Até a próxima aventura!")
        break
    else:
        print("Escolha uma opção válida!")
        
    input("Enter para continuar!")