#App 1: Termômetro

#Crie um aplicativo termômetro. Peça a temperatura em graus Celsius da pessoa e imprima na tela se essa pessoa está ou não com febre. Febre é 37.5 ou mais

#Melhore o aplicativo termômetro, indique se a pessoa está com febre baixa, febre média ou febre elevada. Febre baixa deverá começar a partir de 37.5 e os critérios restantes serão a critério da dupla.

# 1. Pedir temperatura
# 2. Verificar se é >= 37.5
# 3. Se for = febre
# 4. Senão = sem febre

# temp = float(input("Digite sua temperatura em °C:"))

# if (temp >= 37.5):
#     print("Você está com febre!")
# else:
#     print("Sua temperatura não indica febre!")

# 1. Pedir temperatura
# 2. Verificar temperatura
# 2.1 Se >= 37.5 e < 38.5 - > Febre baixa
# 2.2 Se >= 38.5 e < 39 -> Febre média
# 2.3 Se >= 39 -> Febre elevada
# 2.4 Senão "Sem febre"

temp = float(input("Digite sua temperatura em °C:"))

if (temp >= 37.5 and temp < 38.5):
    print("Você está com febre baixa")
elif (temp>= 38.5 and temp < 39):
    print("Você está com febre média")
elif (temp >= 39):
    print("Você está com febre elevada!")
else:
    print("Você está sem febre.")
