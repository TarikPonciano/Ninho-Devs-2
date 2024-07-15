#App 1: Termômetro

#Crie um aplicativo termômetro. Peça a temperatura em graus Celsius da pessoa e imprima na tela se essa pessoa está ou não com febre. Febre é 37.5 ou mais

#Melhore o aplicativo termômetro, indique se a pessoa está com febre baixa, febre ou febre elevada. Febre baixa deverá começar a partir de 37.5 e os critérios restantes serão a critério da dupla.

#App 2: Sistema de Desconto

#Receba o valor das compras de um usuário. Determine qual será o desconto que esse usuário irá receber nas compras e exiba o valor original, o valor do desconto e valor final.
#Se o valor for superior a R$ 200,00 desconto é de 10%
#Se o valor for entre R$ 100,00 e R$ 200,00 desconto de 5%
#Valores abaixo de R$ 100,00 não recebem desconto


#Recebe um número inteiro positivo e determina se ele é par ou impar

# num = int(input("Digite um número inteiro:"))

# # (num % 2) == 0 -> Par

# #Checar se é inválido primeiro
# print("If chencado se é negativo")
# if (num < 0):
#     print("O número é inválido!")
# else:
#     if (num%2) == 0:
#         print("O número é par!")
#     else:
#         print("O número é impar!")  
        
# print()
# print("If verificando se o número é válido.")

# if(num >= 0):
#     if (num%2) == 0:
#         print("O número é par!")
#     else:
#         print("O número é impar!")
# else:
#     print("Número inválido.")    
    
# print()
# print("Elif checando se é negativo primeiro.")
    
# if(num < 0):
#     print("Número inválido.")
# elif(num %2)==0:
#     print("O número é par.")
# else:
#     print("O número é impar.")
    
# print()
# print("Elif checando se é par primeiro.")

# if (num % 2)==0:
#     print("O número é par.")
# elif(num <0):
#     print("O número é inválido.")
# else:
#     print("O número é impar.")
    
#Receba o valor da compra e a partir do saldo e do crédito do usuário, mostre na tela, as formas de pagamento disponíveis.

# valor = float(input("Digite o valor da compra:"))

# saldo = 200
# credito = 1000

# if(valor <= saldo):
#     print("Compra no débito disponível!")
# else:
#     print("Valor da compra alto demais. Débito indisponível para essa operação.")
    
# if (valor <= credito):
#     print("Compra no crédito disponível!")
# else:
#     print("Valor da compra alto demais. Crédito indisponível para essa operação.")


# Recebe o valor da compra e determine qual tipo de pagamento utilizar. Se houver saldo disponível, use débito, senão, use crédito, se também não houver crédito, não faça a compra.

valor = float(input("Digite o valor da compra:"))

saldo = 200
credito = 1000

if (valor <= saldo):
    print("Compra feita no débito!")
elif (valor <= credito):
    print("Compra feita no crédito!")
elif(valor <= (saldo+credito)):
    print("Compra feita na combinação de débito e crédito.")
else:
    print("Você não possui fundos para realizar essa compra!")
    
print('''
Tipos de Pagamento

1. Débito
2. Crédito
3. Débito + Crédito
      
      ''')
op = input("Escolha o tipo de pagamento:")

if (op == "1"):
    print("Você escolheu débito!")
elif(op == "2"):
    print("Você escolheu crédito!")
elif(op == "3"):
    print("Você escolheu combinar crédito e débito!")
    print(f"Você tem {saldo} de saldo!")
    debitoValor = float(input("Quantos reais gostaria de usar?"))
else:
    print("Operação inválida!")