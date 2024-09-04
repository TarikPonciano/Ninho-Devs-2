class CifraVigenere:
    def __init__(self, alfabeto='ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
        self.alfabeto = alfabeto
    
    def alligner(self, chave, tamanho):
        # Função para alinhar a chave com o tamanho da mensagem
        return (chave * ((len(tamanho) // len(chave)) + 1))[:len(tamanho)]

    def cifrar(self, msg, chave):
        # Cifra a mensagem usando a chave fornecida
        msg = msg.upper()
        chave = chave.upper()
        nmsg = []  # Valor numérico da mensagem
        ncifra = []  # Valor numérico da mensagem CIFRADA
        cifra = ""  # Mensagem cifrada traduzida dos números
        nkey = []  # Valor numérico da chave

        keyout = self.alligner(chave, msg)  # Chave estendida pela mensagem
        
        for i, j in zip(msg, keyout):
            if i in self.alfabeto:
                posM = self.alfabeto.index(i)
                posK = self.alfabeto.index(j)
                nmsg.append(posM)
                nkey.append(posK)
            else:
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
                cifra += self.alfabeto[i]
            else:
                cifra += i  # Adiciona o espaço ou outros caracteres diretamente

        return cifra

    def decifrar(self, msg, chave):
        # Decifra a mensagem usando a chave fornecida
        msg = msg.upper()
        chave = chave.upper()
        nmsg = []  # Valor numérico da mensagem cifrada
        ndecifra = []  # Valor numérico da mensagem decifrada
        decifra = ""  # Mensagem decifrada traduzida dos números
        nkey = []  # Valor numérico da chave

        keyout = self.alligner(chave, msg)  # Chave estendida pela mensagem

        for i, j in zip(msg, keyout):
            if i in self.alfabeto:
                posM = self.alfabeto.index(i)
                posK = self.alfabeto.index(j)
                nmsg.append(posM)
                nkey.append(posK)
            else:
                nmsg.append(i)  # Mantém o caractere não alfabético (como espaços)
                nkey.append(' ')  # Coloca um espaço na chave para manter alinhamento

        # Decifragem da mensagem
        for i, j in zip(nmsg, nkey):
            if isinstance(i, int) and isinstance(j, int):
                ndecifra.append((i - j) % 26)
            else:
                ndecifra.append(i)  # Adiciona o espaço ou outros caracteres diretamente

        # Conversão de números para caracteres
        for i in ndecifra:
            if isinstance(i, int):
                decifra += self.alfabeto[i]
            else:
                decifra += i  # Adiciona o espaço ou outros caracteres diretamente

        return decifra

if __name__ =="__main__":
    # Exemplo de uso
    cifra = CifraVigenere()
    mensagem = input("Insira a Mensagem: ")
    chave = input("Insira a chave: ")

    mensagem_cifrada = cifra.cifrar(mensagem, chave)
    print("Mensagem Cifrada:", mensagem_cifrada)

    mensagem_decifrada = cifra.decifrar(mensagem_cifrada, chave)
    print("Mensagem Decifrada:", mensagem_decifrada)
