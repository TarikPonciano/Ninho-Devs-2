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
    
    listaNumerosFinal = ajustar_numeros(numeros, " ")
        
    maior = listaNumerosFinal[0]
    for numero in listaNumerosFinal:
        if numero > maior:
            maior = numero
            
    return maior
    
def maior_numero_v3(numeros, modo):
    listaNumeros = numeros.split(" ")
        
    listaNumerosFinal = []
    for numero in listaNumeros:
        if modo == "numero":
            listaNumerosFinal.append(float(numero))
        elif modo == "texto":
            listaNumerosFinal.append(numero)
        else:
            listaNumerosFinal.append("ERRO")
    
    
    maior = listaNumerosFinal[0]
    
    for numero in listaNumerosFinal:
        
        if modo == "numero":
            if numero > maior:
                maior = numero
        elif modo == "texto":
            if len(numero) > len(maior):
                maior = numero            
    return maior

# Calcular a média:

# Descrição: Crie uma função chamada media que recebe uma lista de números (separados por espaços) e retorne a média dos números.
# Exemplo: Se o usuário digitar 1 2 3 4 5, a função deve retornar 3.

def media(numeros, separador):
        
    numerosFinal = ajustar_numeros(numeros, separador)
        
    resultado = sum(numerosFinal)/len(numerosFinal)
    
    return resultado

def ajustar_numeros(numeros, separador):
    numeros = numeros.split(separador)
    
    numerosFinal = []
    for numero in numeros:
        numerosFinal.append(float(numero))
        
    return numerosFinal

# Verificar palíndromo:

# Descrição: Crie uma função chamada e_palindromo que recebe uma string e retorne True se a string for um palíndromo e False caso contrário.
# Exemplo: Se o usuário digitar "radar", a função deve retornar True.


def e_palindromo(palavra):
    
    palavraInvertida = ""
    
    for i in range(len(palavra)):
        
        palavraInvertida += palavra[-1-i]
    
    if palavra.lower() == palavraInvertida.lower():
        return True
    else:
        return False
    
# Contar caracteres:

# Descrição: Crie uma função chamada contar_caracteres que receba uma string e retorne um dicionário com a contagem de cada caractere na string.
# Exemplo: Se o usuário digitar "hello", a função deve retornar {'h': 1, 'e': 1, 'l': 2, 'o': 1}.

    
def contar_caracteres(palavra):
    
    caracteres = {}
    
    for letra in palavra.lower():
        
        if letra in caracteres:
            caracteres[letra] += 1
        else:
            caracteres[letra] = 1
        
    
    return caracteres

def contar_caracteres2(palavra):
    
    caracteres = {}
    
    for letra in palavra.lower():

        caracteres[letra] = palavra.lower().count(letra)

    
    return caracteres

def contar_caracteres3(palavra):
    
    caracteres = {}
    
    palavraSemDuplicatas = set(palavra.lower())
    
    for letra in palavraSemDuplicatas:
        
        caracteres[letra] = palavra.lower().count(letra)
    
    
    return caracteres
        
        
def calculo_imc (peso, altura):
    
    print(peso/altura**2)
    
def calculo_imc(peso,altura, modificador):
    print("Nova versão")
    
calculo_imc(10,10)
    