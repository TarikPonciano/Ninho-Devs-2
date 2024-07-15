
# Crie um programa que pede 10 notas, entre 0 e 10, ao fim calcula a média e imprime a situação de um aluno. Aprovado, Recuperação, Reprovado. Restrições: Use apenas 1 variável para nota. Você deve utilizar for. Você deve validar se a nota é válida ou não. Dica: não é preciso ter 10 notas válidas. 

soma = 0
qtdNotas = 0

for i in range(3):
    
    nota = float(input("Digite uma nota entre 0 e 10:"))
    if (nota >= 0 and nota <= 10):
        soma += nota
        qtdNotas += 1
    else:
        print("Nota inválida!")

media = soma/qtdNotas

print("A média é:", media)

if ((media>= 7) and (media <= 10)):
    print("Você está aprovado!")
elif (media<7 and media >= 4):
    print("Você está de recuperação!")
elif(media>=0 and media <4):
    print("Você está reprovado!")
else:
    print("Erro inesperado!")
    
    
    