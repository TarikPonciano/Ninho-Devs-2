  
# Imprimir na tela os números de 0 a 500
def exercicio1():
    contador = 0
    
    while (contador <= 500):
        print(contador)
        contador += 1
        

# Imprimir na tela somente os pares de 0 a 500
def exercicio2():
    contador = 0
    
    while (contador <= 500):
        
        if contador % 2 == 0:
            print(contador)
        
        contador += 1
# Imprimir a soma dos números de 0 a 500
def exercicio3():
    contador = 0
    soma = 0
    while (contador <= 500):
        soma += contador
        contador += 1
        
    print(soma)
        
# Criar um programa onde é definido um número secreto e o usuário deve dar um palpite para descobrir esse número. O programa deve executar até que o usuário descubra o número.

def exercicio4():
    numeroSecreto = 8

    
    while(True):
        palpite = int(input("Digite um palpite de 0 a 10:"))
        
        if (palpite == numeroSecreto):
            print("Parabéns você acertou!")
            break
        else:
            print("Você errou. Tente novamente.")
        
    
exercicio4()