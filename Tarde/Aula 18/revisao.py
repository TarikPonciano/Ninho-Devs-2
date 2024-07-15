def teste(parametro1, parametro2):
    pontuacao = "."
    frase = parametro1 + " " + parametro2 + pontuacao
    print("A frase é:",frase)
    return frase

def conexao(login, senha):
    for item in lista:
        if item % 2 == 0:
            novaLista.append(item)
        
    return novaLista
    
def teste2(palavra, pontuacao):
    frase = palavra + pontuacao
    return frase

def teste3(numeros):
    numeros.append(60)
    print("Numeros:",numeros)
    
pikachu = ["Pikachu", "Elétrico", 60, 10]

pokemonJogador = pikachu.copy()

pokemonInimigo = pikachu.copy()

pokemonInimigo[2] -= pokemonJogador[3]

print(pokemonJogador)
print(pokemonInimigo)