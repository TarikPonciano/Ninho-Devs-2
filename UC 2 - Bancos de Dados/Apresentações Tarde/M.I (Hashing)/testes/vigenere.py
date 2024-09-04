#Cifra de Vigenére por Luís Alarcon - Maio de 2024
alfabeto = str('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

msg = input("Insira a Mensagem: ").upper()
keyin = input("Insira a chave: ").upper()
nmsg = [] #Valor numérico da mensagem
ncifra = [] #Valor numérico da mensagem CIFRADA
cifra = "" #Mensagem cifrada Traduzida dos números
nkey = [] #Valor numérico da chave

def alligner(chave, size):
    return (chave * ((len(size) // len(chave)) + 1))[:len(size)]

keyout = alligner(keyin, msg) #Chave Estendida pela mensagem
print(""*2)
print(" "*7, "Mensagem", " "*8, "|      Chave")
for i, j in zip(msg, keyout):
    posM = alfabeto.index(i) #+ 1
    posK = alfabeto.index(j) #+ 1
    print(i, "------------------->", "{:02}".format(posM), "| ", j, "------------------->", "{:02}".format(posK))
    nmsg.append(posM)
    nkey.append(posK)

for i, j in zip(nmsg, nkey):
    ncifra.append((i + j)%26)
    #print("Mensagem Cifrada:?", ncifra)

for i in ncifra:
    cifra += alfabeto[i]

print(msg)
print("")
print("Valor Numérico da Mensagem")
print(nmsg)
print("")
print("Valor Numérico da Chave após alinhamento:")
print(nkey)
print("")
print("Alinhamento de chave: ", keyout)
print("")
print("Mensagem Cifrada:?")
print(ncifra)
#nota: tirar a posição da chave tbm : FEITO
#      Repetir a chave até o tamanho da string mensagem : FEITO
print(cifra)