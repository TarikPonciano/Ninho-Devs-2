#App 1: Termômetro

# #Crie um aplicativo termômetro. Peça a temperatura em graus Celsius da pessoa e imprima na tela se essa pessoa está ou não com febre. Febre é 37.5 ou mais

# #1. Pedir a informação temperatura
# #2. Verificar a temperatura e decidir (Febre/Não Febre)
# #3. Imprimir na tela o resultado da decisão
# temp = float(input("Digite sua temperatura em °C:"))

# if (temp >= 37.5):
#     print("Você está com febre!")
# else:
#     print("Você não está com febre.")


#Melhore o aplicativo termômetro, indique se a pessoa está com febre baixa, febre ou febre elevada. Febre baixa deverá começar a partir de 37.5 e os critérios restantes serão a critério da dupla.

temp = float(input("Digite sua temperatura em °C:"))

if (temp >= 37.5 and temp <= 38.1):
    print("Febre baixa!")
elif (temp>38.1 and temp <= 39):
    print("Febre media!")
elif (temp > 39):
    print("Febre elevada!")
else:
    print("Sem febre!")
    
