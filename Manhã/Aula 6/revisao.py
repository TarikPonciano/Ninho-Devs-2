# numero = int(input("Digite um número inteiro positivo:"))

# # (numero % 2) == 0
# print("If verificando negativo!")
# if (numero < 0):
#     print("Número negativo detectado! Insira um valor positivo!")
# else:
#     if (numero % 2) == 0:
#         print("O número é par!")
#     else:
#         print("O número é impar!")
        
# print("If verificando positivo primeiro")
# if (numero >= 0):
#     if (numero % 2) == 0:
#         print("O número é par!")
#     else:
#         print("O número é impar!")
# else:
#     print("O numero é negativo!")

# print("Elif correto!")
# if (numero < 0):
#     print("Número inválido!")
# elif(numero %2 == 0):
#     print("O número é par!")
# else:
#     print("O número é impar!")
    
# print("Elif Errado:")
# if (numero %2 == 0):
#     print("O número é par!")
# elif(numero < 0):
#     print("Número inválido!")
# else:
#     print("O número é impar!")


# #App 1: Termômetro

# #Crie um aplicativo termômetro. Peça a temperatura em graus Celsius da pessoa e imprima na tela se essa pessoa está ou não com febre. Febre é 37.5 ou mais

# #Melhore o aplicativo termômetro, indique se a pessoa está com febre baixa, febre ou febre elevada. Febre baixa deverá começar a partir de 37.5 e os critérios restantes serão a critério da dupla.

# #App 2: Sistema de Desconto

# #Receba o valor das compras de um usuário. Determine qual será o desconto que esse usuário irá receber nas compras e exiba o valor original, o valor do desconto e valor final.
# #Se o valor for superior a R$ 200,00 desconto é de 10%
# #Se o valor for entre R$ 100,00 e R$ 200,00 desconto de 5%
# #Valores abaixo de R$ 100,00 não recebem desconto

# valor = float(input("O valor da sua compra: R$ "))

# if(valor >= 200):
#     desconto = 0.10
#     valorDoDesconto = valor * desconto
#     novoValor = valor - valorDoDesconto
#     print(f"Sua compra foi de R$ {valor}")
#     print(f"O valor do desconto é R$ {valorDoDesconto}")
#     print(f"O seu novo valor é R$ {novoValor}")
# elif(valor >= 100 and valor < 200):
#     desconto = 0.05
#     valorDoDesconto = valor * desconto
#     novoValor = valor - valorDoDesconto
#     print(f"Sua compra foi de R$ {valor}")
#     print(f"O valor do desconto é R$ {valorDoDesconto}")
#     print(f"O seu novo valor é R$ {novoValor}")
# else:
#     print(f"Sua compra foi de R$ {valor}")
#     print(f"Não há desconto para a compra")

#Verificar os tipos de pagamento disponível
# saldo = 200
# credito = 1000

# valor = float(input("Digite o valor da compra:"))

# if (valor <= saldo):
#     print("Compra no débito disponível.")
# else:
#     print("Saldo insuficiente para débito.")
    
# if (valor <= credito):
#     print("Compra no crédito disponível.")
# else:
#     print("Crédito insuficiente para compra no crédito.")


#Determinar o tipo de operação a ser usada na compra. Se saldo for suficiente, use débito. Senão, se crédito for suficiente, use crédito. Senão, não compre.

saldo = 200
credito = 1000

valor = float(input("Digite o valor da compra:"))

if(valor <= saldo):
    print("Produto comprado no débito!")
elif (valor <= credito):
    print("Produto comprado no crédito!")
elif (valor <= (saldo+credito)):
    print("Produto comprado utilizando crédito e débito.")
else:
    print("Sem dinheiro para comprar o produto.")


