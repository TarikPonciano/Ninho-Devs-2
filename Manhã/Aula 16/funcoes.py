def hello(): #Ao invés de imprimir "WORLD", peça o nome da pessoa e imprima em maiúsculo
    nome = input("Digite seu nome: ")
    print("------------------")
    print(f"HELLO {nome.upper()}!")
#Crie uma função que pede o nome da pessoa, mostra uma saudação e na sequência pede dois números, exibe na tela se cada um é par ou impar e exibe na tela o resultado de sua multiplicação. Rode essa função 3 vezes

def mult_par_impar():
    hello()
    
    num1 = int(input("Digite o número 1: "))
    num2 = int(input("Digite o número 2: "))
    
    if (num1 % 2) == 0:
        print("Número 1 é par!")
    else:
        print("Número 1 é impar!")
        
    if (num2 % 2) == 0:
        print("Número 2 é par!")
    else:
        print("Número 2 é impar!")
        
    multiplicacao = num1 * num2
    
    print(multiplicacao) 
    
# for i in range(3):
#     mult_par_impar()

#Crie uma função que pede uma palavra e conta quantas vogais estão presentes nessa palavra. Exiba na tela essa contagem. Rode pelo menos uma vez.

def conta_vogal():
    
    palavra = input("Digite uma palavra: ")
    contador = 0
    listaVogais = []
    
    for letra in palavra:
        # if letra == "A" or letra == "E" or letra == "I" or letra == "O" or letra == "U":
        #     contador += 1
        if letra.lower() in ("a", "e", "i", "o", "u"):
            contador+=1
            listaVogais.append(letra)
            
    print("O número de vogais é:", contador)
    print("As vogais são:", listaVogais)


# Crie um programa que pede o nome de uma pessoa, calcula sua idade e exibe na tela a frase "Olá fulano, você tem x anos"
def calcular_idade():
    anoNasc = int(input("Digite o ano de nascimento:"))
    fezAniversario = input("Fez aniversário? Sim/Não?")
    anoAtual = 2024
    if fezAniversario == "Sim":
        idade = anoAtual - anoNasc #Já fez aniversário
    else:
        idade = anoAtual - anoNasc - 1
        
    return idade
    
    
# Contar caracteres:

# Descrição: Crie uma função chamada contar_caracteres que peça ao usuário para digitar uma string e retorne um dicionário com a contagem de cada caractere na string.
# Exemplo: Se o usuário digitar "hello", a função deve retornar {'h': 1, 'e': 1, 'l': 2, 'o': 1}.

# Calcular a média:

# Descrição: Crie uma função chamada media que peça ao usuário para digitar uma lista de números (separados por espaços) e retorne a média dos números.
# Exemplo: Se o usuário digitar 1 2 3 4 5, a função deve retornar 3.

def media(numeros):
    # numeros = input("Digite os números desejados, separados por espaço: ")
    # # "10 30 5 67 89 36" > ["10", "30" , "5" , "67", "89", "36"]
    # listaNumeros = numeros.split(" ")
    # # listaNumerosInteiros = [int(numero) for numero in listaNumeros]
    # listaNumerosInteiros = []
    
    # for numero in listaNumeros:
    #     listaNumerosInteiros.append(int(numero))
        
    listaNumerosInteiros = ajustar_numeros(numeros)
        
    resultado = sum(listaNumerosInteiros)/len(listaNumerosInteiros)
    return resultado

def maximo(numeros):
    
    listaNumerosInteiros = ajustar_numeros(numeros)
    
    maior = listaNumerosInteiros[0]
    for numero in listaNumerosInteiros:
        if numero > maior:
            maior = numero
    
    return maior
    # return max(listaNumerosInteiros)

def ajustar_numeros(numeros):
    listaNumeros = numeros.split(",")
    listaFinal = []
    for numero in listaNumeros:
        listaFinal.append(int(numero))
        
    return listaFinal

entrada = input("Digite os números separados por espaço: ")

print(f"A média é {media(entrada)}")
print(f"O maior número é {maximo(entrada)}")
# Máximo de uma lista:

# Descrição: Crie uma função chamada maximo que peça ao usuário para digitar uma lista de números (separados por espaços) e retorne o maior número.
# Exemplo: Se o usuário digitar 1 3 2 5 4, a função deve retornar 5.

# Verificar palíndromo:

# Descrição: Crie uma função chamada e_palindromo que peça ao usuário para digitar uma string e retorne True se a string for um palíndromo e False caso contrário.
# Exemplo: Se o usuário digitar "radar", a função deve retornar True.
