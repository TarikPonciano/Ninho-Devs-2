# Cifra de Vigenère por Luís Alarcon - Maio de 2024
alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

msg = input("Insira a Mensagem: ").upper()
keyin = input("Insira a chave: ").upper()
nmsg = []  # Valor numérico da mensagem
ncifra = []  # Valor numérico da mensagem CIFRADA
cifra = ""  # Mensagem cifrada Traduzida dos números
nkey = []  # Valor numérico da chave

def alligner(chave, size):
    return (chave * ((len(size) // len(chave)) + 1))[:len(size)]

keyout = alligner(keyin, msg)  # Chave Estendida pela mensagem
print("\n")
print(" "*7, "Mensagem", " "*8, "|      Chave")

for i, j in zip(msg, keyout):
    if i in alfabeto:  # Ignorar caracteres que não estão no alfabeto (como espaços)
        posM = alfabeto.index(i)  # + 1
        posK = alfabeto.index(j)  # + 1
        print(i, "------------------->", "{:02}".format(posM), "| ", j, "------------------->", "{:02}".format(posK))
        nmsg.append(posM)
        nkey.append(posK)
    else:
        print(i, "------------------->", "  ", "| ", " ", "------------------->", "  ")
        nmsg.append(i)  # Mantém o caractere não alfabético (como espaços)
        nkey.append(' ')  # Coloca um espaço na chave para manter alinhamento

# Cifragem da mensagem
for i, j in zip(nmsg, nkey):
    if isinstance(i, int) and isinstance(j, int):
        ncifra.append((i + j) % 26)
    else:
        ncifra.append(i)  # Adiciona o espaço ou outros caracteres diretamente

# Conversão de números para caracteres
for i in ncifra:
    if isinstance(i, int):
        cifra += alfabeto[i]
    else:
        cifra += i  # Adiciona o espaço ou outros caracteres diretamente

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
print("Mensagem Cifrada:")
print(ncifra)
print(cifra)
