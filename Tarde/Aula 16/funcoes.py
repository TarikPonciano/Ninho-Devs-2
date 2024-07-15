#Crie uma função que pede o nome do usuário e imprime na tela "Hello, fulano!". Execute 3 vezes.
def hello():
    print("------------------")
    print("HELLO")
    print("WORLD")
    
def hello2():
    nome = input("Digite seu nome: ")
    
    print("------------------")
    
    print(f"Olá, {nome}!")


#Crie uma função que pede ao usuário dois números inteiros, verifica e imprime na tela se cada um é par ou impar. Se ambos forem par faz a soma, se ambos forem impar faz a subtração, se forem par e impar faz a multiplicação. Exiba o resultado do cálculo na tela. Execute 3 vezes.

def calc_par_impar():
    n1 = int(input("Digite o número 1: "))
    n2 = int(input("Digite o número 2: "))
    n1Tipo = ""
    n2Tipo = ""
    
    if n1 % 2 == 0:
        n1Tipo = "Par"
    else:
        n1Tipo = "Impar"
        
    if n2 % 2 == 0:
        n2Tipo = "Par"
    else:
        n2Tipo = "Impar"
    
    print(f"O número 1 é {n1Tipo}!")
    print(f"O número 2 é {n2Tipo}!")
    
    if n1Tipo == "Par" and n2Tipo == "Par":
        resultado = n1 + n2
        operacao = "Soma"
        equacao = f"{n1} + {n2}"
    elif n1Tipo == "Impar" and n2Tipo == "Impar":
        resultado = n1 - n2
        operacao = "Subtração"
        equacao = f"{n1} - {n2}"
    elif n1Tipo != n2Tipo:
        resultado = n1 * n2
        operacao = "Multiplicação"
        equacao = f"{n1} * {n2}"
    else:
        resultado = "INVÁLIDO!"    
    
    
    print(f"O resultado da {operacao} é: {equacao} = {resultado}")
    
#Crie uma função que pede uma palavra ao usuário e exibe na tela a quantidade de vogais e quais vogais estão presentes na palavra. Execute 3 vezes.

def conta_vogais():
    
    palavra = input("Digite uma palavra: ")
    
    listaVogais = []
    qtdVogais = 0
    
    for letra in palavra.upper():
        
       if letra in ["A", "E", "I", "O", "U"]:
            qtdVogais += 1
            
            if letra not in listaVogais:
                listaVogais.append(letra)
    
    print(f"Quantidade de Vogais: {qtdVogais} ")
    print(f"Vogais: {listaVogais}")
    
#Faça um programa que pede o nome e o ano de nascimento de uma pessoa e imprima "Olá fulano, você tem x anos!"

def calcular_idade():
    anoNasc = int(input("Digite o ano de nascimento: "))
    anoAtual = 2024
    fezAniversario = input("Você já fez aniversário? (Sim/Não)")
    
    idade = anoAtual - anoNasc
    
    if fezAniversario == "Sim":
        pass
    else:
        idade -= 1
        
    return idade
    

# Máximo de uma lista:

# Descrição: Crie uma função chamada maximo que peça ao usuário para digitar uma lista de números (separados por espaços) e retorne o maior número.
# Exemplo: Se o usuário digitar 1 3 2 5 4, a função deve retornar 5.    

def maior_numero():
    
    numeros = input("Digite os números separados por espaço: ")
    
    "10 20 30 50 120"
    
    numero = ""
    listaNumeros = []
    for n in numeros:
        
        if n != " ":
            numero += n 
        else:
            listaNumeros.append(int(numero)) 
            numero = ""
            print(listaNumeros)
    else:
        listaNumeros.append(int(numero))
        print(listaNumeros)
        
    for i in range(len(numeros)):
        if numeros[i] != " ":
            numero += numeros[i]
            if i == (len(numeros)-1):
                listaNumeros.append(int(numero))
        else:
            listaNumeros.append(int(numero))
            numero = ""
            print(listaNumeros)
    
    maior = listaNumeros[0]
    
    for numero in listaNumeros:
        if numero > maior:
            maior = numero
            
    return maior

def maior_numero_v2():
    numeros = input("Digite uma lista de números separada por espaço: ")
    
    listaNumeros = numeros.split(" ")
        
    listaNumerosFinal = []
    for numero in listaNumeros:
        listaNumerosFinal.append(float(numero))
        
    maior = listaNumerosFinal[0]
    for numero in listaNumerosFinal:
        if numero > maior:
            maior = numero
            
    return maior
    