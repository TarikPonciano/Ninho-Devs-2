# for (int i = 0; i < 10; i++){
#     print(i)
# }

#Imprima na tela, todos os números pares de 0 a 100
# for i in range(101):
    
#     if (i % 2) == 0:
#         print(i)
        
# #Imprima na tela, a soma desses números pares


# soma = 0

# for i in range(101):
#     if (i % 2)==0:
#         print(i)
#         soma += i
        
# print("A soma dos números é:", soma)

#Imprima a média de todos os números pares entre 1 e 1000

soma = 0
qtdPares = 0

for i in range(1,5001):
    
    if (i % 2) == 0:
        soma += i
        qtdPares += 1
        
media = soma/qtdPares

print("Média dos pares é:", media)

# Crie um programa que pede 10 notas, entre 0 e 10, ao fim calcula a média e imprime a situação de um aluno. Aprovado, Recuperação, Reprovado. Restrições: Use apenas 1 variável para nota. Você deve utilizar for. Você deve validar se a nota é válida ou não. Dica: não é preciso ter 10 notas válidas. 