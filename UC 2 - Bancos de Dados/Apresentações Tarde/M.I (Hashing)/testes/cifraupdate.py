class VigenereCipher:
    def __init__(self, alfabeto='ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
        self.alfabeto = alfabeto

    def alligner(self, chave, mensagem):
        # Alinha a chave considerando apenas letras (ignora espaços e pontuações)
        chave_expandida = []
        j = 0
        for char in mensagem:
            if char in self.alfabeto:
                chave_expandida.append(chave[j % len(chave)])
                j += 1
            else:
                chave_expandida.append(char)  # Preserva espaços e caracteres não alfabéticos
        return ''.join(chave_expandida)

    def cifrar(self, mensagem, chave):
        mensagem = mensagem.upper()
        chave = chave.upper()
        nmsg = []  # Valor numérico da mensagem
        ncifra = []  # Valor numérico da mensagem CIFRADA
        cifra = []  # Lista para construção da mensagem cifrada

        keyout = self.alligner(chave, mensagem)

        for i, j in zip(mensagem, keyout):
            if i in self.alfabeto:
                posM = self.alfabeto.index(i)  # Índice da mensagem no alfabeto
                posK = self.alfabeto.index(j)  # Índice da chave no alfabeto
                nmsg.append(posM)
                ncifra.append((posM + posK) % len(self.alfabeto))
            else:
                cifra.append(i)  # Adiciona o caractere inalterado à mensagem cifrada

        # Converte os números cifrados em letras
        for i in ncifra:
            cifra.append(self.alfabeto[i])

        return ''.join(cifra)

    def decifrar(self, mensagem_cifrada, chave):
        mensagem_cifrada = mensagem_cifrada.upper()
        chave = chave.upper()
        nmsg = []  # Valor numérico da mensagem CIFRADA
        mensagem_decifrada = []  # Lista para construção da mensagem decifrada

        keyout = self.alligner(chave, mensagem_cifrada)

        for i, j in zip(mensagem_cifrada, keyout):
            if i in self.alfabeto:
                posC = self.alfabeto.index(i)  # Índice da mensagem cifrada no alfabeto
                posK = self.alfabeto.index(j)  # Índice da chave no alfabeto
                nmsg.append((posC - posK) % len(self.alfabeto))
            else:
                mensagem_decifrada.append(i)  # Adiciona o caractere inalterado à mensagem decifrada

        # Converte os números decifrados em letras
        for i in nmsg:
            mensagem_decifrada.append(self.alfabeto[i])

        return ''.join(mensagem_decifrada)

if __name__ ==  "__main__":
    # Teste
    cipher = VigenereCipher()

    mensagem = input("Insira a Mensagem: ")
    chave = input("Insira a chave: ")

    # Cifrar a mensagem
    mensagem_cifrada = cipher.cifrar(mensagem, chave)
    print("\nMensagem Cifrada:")
    print(mensagem_cifrada)

    # Decifrar a mensagem
    mensagem_decifrada = cipher.decifrar(mensagem_cifrada, chave)
    print("\nMensagem Decifrada:")
    print(mensagem_decifrada)
