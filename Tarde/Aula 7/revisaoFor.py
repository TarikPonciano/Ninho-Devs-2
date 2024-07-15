
# Crie um programa que calcula o somatório dos números de 200 a 1000.
# soma = 0
# for i in range(200,10001):
#     soma += i

# print(soma)

# Crie um programa que pede dois números ao usuário, calcule o somatório de todos os números entre esses dois números.

# Crie um programa que pede 10 nomes e imprime a frase "Olá, fulano!"
rep = int(input("Quantos nomes deseja escrever?"))

for i in range (rep):
    nome = input("Digite o seu nome:")
    if (nome[0] == "A" or nome[0] == "a"):
        print("Olá,", nome)
# Crie um programa que pede 10 nomes porém só imprime a frase, se o nome começar com a letra "A"

#Crie um programa que recebe o valor de 5 produtos, no final calcula o total da compra e determinar se o cliente terá desconto ou não. Se o valor total for maior que 200, 10% de desconto, senão, não há desconto. Imprima na tela, os valores inseridos, o total da compra, o valor descontado e o valor final da compra.