# Crie um programa que pede 5 nomes e ao fim os imprime de forma numerada na sequência que foram inseridos.

def revisao1():
    nomes = ""
    for i in range(5):
        nome = input("Digite um nome:")
        
        nomes += f"{i+1}. {nome}\n"
        
    print(nomes)
    
def revisao1Alternativa():
    nomes = []
    for i in range(5):
        nome = input("Digite um nome:")
        
        nomes.append(f"{i+1}. {nome}")
        
    for n in nomes:
        print(n)
        
    
# Crie um programa que checa se um número específico é primo.

def revisao2():
    numero = int(input("Digite um número inteiro:"))
    divisores = 0
    
    for i in range(2, numero+1):
        if (numero % i == 0):
            divisores += 1
            
    if divisores>1:
        print(f"O número {numero} não é primo.")
    else:
        print(f"O número {numero} é primo.")
        
# numero % divisor == 0

# Crie um programa que imprime na tela os primos entre 0 e 100.

def revisao3():
    for i in range(2,101):
        divisores = 0
        for j in range(2, i+1):
            if (i % j ==0):
                divisores+= 1
        
        if (divisores <= 1):
            print(f"{i} é primo")


def revisao3Alternativa():
    for i in range(2,10001):
        divisores = 0
        for j in range(2, i):
            if (i == 2):
                break
            if (i % j == 0):
                divisores += 1
                break
        
        if (divisores == 0):
            print(f"{i} é primo")

                