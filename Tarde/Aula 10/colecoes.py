#Utilizando listas, receba 3 notas e calcule a média de um aluno. Ao final exiba as notas e a média.

notas = []

for i in range(3):
    nota = float(input(f"Nota {i+1}: "))
    
    notas.append(nota)
    
# soma = 0
    
# for i in range(len(notas)):
#     soma += notas[i]   

#[10,8,9]
# for n in notas:
#     soma += n
    
media = sum(notas)/len(notas)

print("Sua média é:", media)

for n in notas:
    print(n)