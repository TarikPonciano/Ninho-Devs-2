#Adivinhação Versão 1

#Crie um programa que possui um número secreto de 0 a 10 e peça para que o usuário tente adivinhar. Informe se o usuário acertou ou errou!
import random
# from random import randint

numeroSecreto = random.randint(0,10)

palpite1 = int(input("Digite um número de 0 a 10. Você terá 3 chances para acertar:"))

if (palpite1 == numeroSecreto):
    print("Parabéns, você acertou!")
else:
    print("Você errou!")
    palpite2 = int(input("Digite outro número de 0 a 10. Você ainda tem 2 chances:"))
    
    if (palpite2 == numeroSecreto):
        print("Parabéns, você acertou na segunda tentativa.")
    else:
        print("Você errou de novo!")
        palpite3 = int(input("Digite outro número de 0 a 10. Esta é a última chance:"))
        
        if (palpite3 == numeroSecreto):
            print("Parabéns, você acertou na ultima tentativa.")
        else:
            print("Acabaram as tentativas!")
    


#Adivinhação Versão 2

#Crie um programa que possui um número secreto de 0 a 100 e peça para que o usuário tente adivinhar. Informe se o usuário acertou, se ele errou, informe se o palpite foi acima ou abaixo do número secreto.

numeroSecreto = 42

palpite = int(input("Dê um palpite entre 0 e 100:"))
if (palpite >= 0 and palpite <= 100):
    if (palpite == numeroSecreto):
        print("Parabéns, você acertou!")
    else:
        print("Você errou!")
        
        if (palpite > numeroSecreto):
            print("Você chutou um número MAIOR que o número secreto.")
        else:
            print("Você chutou um número MENOR que o número secreto.")
else:
    print("Digite um palpite válido!")
            
        
# if (palpite == numeroSecreto):
#     print("Parabéns, você acertou!")
# elif(palpite > numeroSecreto):
#     print("O número que você procura é menor")
# elif (palpite < numeroSecreto):
#     print("O número que você procura é maior")

