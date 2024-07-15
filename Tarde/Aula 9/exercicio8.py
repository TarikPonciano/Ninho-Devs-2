for i in range(5):
    numero = int(input("Digite um número:"))
    
    if(i == 0):
        menor = numero
    
    if (numero < menor):
        print("Trocou")
        print("Saiu", menor)
        print("Entrou",numero)
        menor = numero
        

print(menor)