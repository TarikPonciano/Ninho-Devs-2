#Criar um programa que recebe 4 notas válidas e imprime a média do aluno ao final.

#Criar um programa que pergunta quantas notas deverão ser inseridas e após esse número de notas válidas serem inseridas, imprime a média ao final.

#Criar um jogo de advinhação onde é definido um número secreto no início da execução do programa e o usuário deve dar um palpite. Dê dicas para o usuário a cada erro. O programa encerra ao acertar.

#Criar uma calculadora. Seu programa deverá pedir dois números (float) e exibir um menu com as opções disponíveis, exemplo:
# 1. Soma (+)
# 2. Subtração
# 3. Divisão
# 4. Multiplicação
# 0. Sair
#Ao escolher uma das opções o programa irá executar a operação desejada e exibir o resultado na tela. O programa deverá executar ATÉ QUE a pessoa escolha a opção 0. Sair. Impeça de acontecer divisão por 0

total = 0
#Apenas valores entre 0 e 100
# resposta = "Sim"

while (True):
    valor = input("Digite o valor do produto:")

    valor = float(valor)
    if(valor>=0 and valor <= 100):
        total += valor
    else:
        print("Valor inválido!")
            
    if(total > 500):
        print("Finalizando processo de compra.")
        break
    
    
    
print(f"R$ {total:.2f}")