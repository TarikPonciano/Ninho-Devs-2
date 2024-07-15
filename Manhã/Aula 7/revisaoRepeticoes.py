#Sintaxe do for:
"""
for i in range(x):
    print(i)


i - Número de repetições até o momento
range(x) - Repita até o número x
print(i) - Imprima o número da repetição atual
"""

#Crie um programa que itera de 0 a 100

#Imprima todos os números pares

#Imprima a soma dos números pares

#Imprima a quantidade dos números pares

#Imprima a média dos números pares

# if (numero % 2) == 0:

soma = 0
qtdPares = 0

for i in range(101):
    
    if (i%2) == 0:
        print(i)
        
        soma += i
        qtdPares += 1


media = soma/qtdPares
        
print("Soma:",soma)
print("Quantidade de números pares:",qtdPares)
print("A média dos números pares de 0 a 100 é:",media)
        
# for i in range (1001):
#     if (i >= 200):
        
# for i in range (200, 1001):
        
# Crie um programa que calcula o somatório dos números de 200 a 1000.

# Crie um programa que pede dois números ao usuário, calcule o somatório de todos os números entre esses dois números.

# Crie um programa que pede 10 nomes e imprime a frase "Olá, fulano!"

# Crie um programa que pede 10 nomes porém só imprime a frase, se o nome começar com a letra "A"

#Crie um programa que recebe o valor de 5 produtos, no final calcula o total da compra e determinar se o cliente terá desconto ou não. Se o valor total for maior que 200, 10% de desconto, senão, não há desconto. Imprima na tela, os valores inseridos, o total da compra, o valor descontado e o valor final da compra.