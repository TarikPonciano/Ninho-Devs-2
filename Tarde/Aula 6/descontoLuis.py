valor = float(input("Insira valor do produto: "))
# desconto:float

if(valor>=200):
    desconto = valor * 0.1
elif(valor<200 and valor>=100):
    desconto = valor * 0.05
elif(valor<100 and valor > 0):
    desconto = 0
else:
    print("Valor inválido")
    
   
if (valor >= 0):
    print(f"Valor do produto: {valor:.2f}")
    print(f"Valor do desconto: {desconto:.2f}")
    print(f"Valor Final: {valor - desconto:.2f}")
else:
    print("Não foi possível calcular a nota fiscal!")