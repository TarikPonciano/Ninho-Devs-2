# for (int i = 0; i<10; i++){
    
    
# }
#Escreva um programa, que recebe 10 notas e calcula a média dessas notas. Você só deve ter uma variável para as notas. Você deve usar o for. Ao final, imprima a média obtida.


# nota1 = float(input("Digite a nota 1:"))

# nota2 = float(input("Digite a nota 2:"))

# nota3 = float(input("Digite a nota 3:"))

# media = (nota1 + nota2 + nota3)/3

# print("A média é", media)


soma = 0

for i in range(10):
    
    nota = float(input(f"Digite a nota {i+1}:"))
    #Verifique se a nota é válida. Some apenas se a nota for válida.
    if (nota >= 0 and nota <=10):
        
        soma += nota
    else:
        print("Nota inválida")
    
    
media = soma / 10

print("A média é", media)