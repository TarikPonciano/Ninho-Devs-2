for i in range(5):
    numero = int(input("Digite um número:"))
    
    if (i == 0):
        menor = numero
    
    if (numero < menor):
        menor = numero
        
print("O menor número digitado foi:",menor)