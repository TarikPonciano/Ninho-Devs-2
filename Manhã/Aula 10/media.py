#Criar um programa que recebe 4 notas válidas e imprime a média do aluno ao final.

soma = 0
qtdNotas = 0
totalNotas = int(input("Quantas notas deseja inserir?"))

while(True):
    nota = float(input(f"Digite a nota {qtdNotas+1}:"))
    
    if(nota>=0 and nota<=10):
        soma += nota
        qtdNotas += 1
    else:
        print("Nota inválida!")
    
    if (qtdNotas == totalNotas):
        print("Todas as notas foram inseridas!")
        break
    
media = soma / qtdNotas

print("Sua média é: ", media)