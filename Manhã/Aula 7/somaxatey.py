inicial = int(input("Digite o número inicial:"))
final = int(input("Digite o número final:"))

soma = 0

if (inicial < final):
    for i in range(inicial, final+1):
        soma += i
else:
    for i in range(final, inicial+1):
        soma += i
        
print(soma)
    