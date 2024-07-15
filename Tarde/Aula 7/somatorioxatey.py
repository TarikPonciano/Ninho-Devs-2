inicial = int(input("Digite o início do intervalo:"))

final = int(input("Digite o final do intervalo:"))

# if (final < inicial):
#     aux = inicial
#     inicial = final
#     final = aux 
    
#     inicial, final = final, inicial

# menor = min(inicial,final)
# maior = max(inicial,final)

soma = 0
if (final > inicial):
    for i in range(inicial, final+1):
        soma += i
else:
    for i in range(final, inicial+1):
        soma += i
    
# for i in range(menor,maior):
#     soma+=i
print(soma)