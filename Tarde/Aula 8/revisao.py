#Crie um programa que pede 5 nomes e os imprime como uma lista numerada na ordem em que foram inseridos. Exemplo: 
# 1. Nome 1
# 2. Nome 2
# 3. Nome 3

def revisao1():
    nomes = ""
    
    for i in range(5):
        
        nome = input("Digite um nome:")
        
        nomes += f"{i+1}. {nome} \n" 
              
    print(nomes)
        
def revisao1Alternativa():
    
    nomes = []
    
    for i in range(2):
        
        nome = input("Digite um nome:")
        
        nomes.append(nome)
    
    contador = 1
    
    for n in nomes:
        print(f"{contador}. {n}")
        contador+=1
        
# Crie um programa que determina se um número inteiro qualquer é primo ou não

#numero % divisor == 0

def revisao2():
    
    numero = int(input("Digite um número:"))
    divisores = 0
    for i in range(1, numero+1):
        
        if (numero % i == 0):
            divisores += 1
            
    if (divisores > 2):
        print("Não é primo!")
    else:
        print("É primo")
        
def revisao2Melhorada():
    
    numero = int(input("Digite um número:"))
    
    ehprimo = True
    
    for i in range(2, numero):
        
        if (numero % i == 0):
            ehprimo = False
            break
        
    if ehprimo:
        print("O número é primo!")
    else:
        print("O número não é primo!")
            
            
    
# Crie um programa que imprime na tela todos os números primos entre 0 e 100
def revisao3():
    for i in range(2,101):
        
        divisores = 0
        
        for j in range(1, i+1):
            
            if (i % j == 0):
                
                divisores += 1
                
        if divisores <= 2:
            print(i, "é primo")
            
            


def revisao3Melhorada():
    for i in range(2,100001):
        
        ehprimo = True
    
        for j in range(2, i):
            
            if (i % j == 0):
                ehprimo = False
                break
            
        if ehprimo:
            print(f"O número {i} é primo!")
    
revisao3Melhorada()
               