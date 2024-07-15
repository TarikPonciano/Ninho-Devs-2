largura = int(input("Digite a largura desejada:"))
altura = int(input("Digite a altura desejada:"))

linhaLargura = "#"*largura
linhaMeio = "#"+ (' ' *(largura-2)) + "#"


print(linhaLargura)
for i in range(altura-2):
    print(linhaMeio)
print(linhaLargura)
    
    
