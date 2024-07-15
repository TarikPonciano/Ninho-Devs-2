#Criar um jogo de advinhação onde é definido um número secreto no início da execução do programa e o usuário deve dar um palpite. Dê dicas para o usuário a cada erro. O programa encerra ao acertar.
import random

numeroSecreto = random.randint(0,100)

while(True):
    palpite = int(input("Digite um número de 0 a 100:"))
    
    if (palpite == numeroSecreto):
        print("Parabéns, você acertou!")
        break
    else:
        print("Você errou!")
        
        if(palpite > numeroSecreto):
            print("O número secreto é menor do que seu palpite.")
        else:
            print("O número secreto é maior do que seu palpite.")