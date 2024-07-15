# # Crie um programa que recebe dois números e exibe na tela o resultado das operações Soma, Subtração, Divisão e Multiplicação.

# # n1 = float(input("Digite o número 1:"))
# # n2 = float(input("Digite o número 2:"))
# n1 = input("Digite o número 1:")
# n1 = float(n1)

# n2 = input("Digite o número 2:")
# n2 = float(n2)

# soma = n1 + n2
# subtracao = n1 - n2
# divisao = n1 / n2
# multiplicacao = n1 * n2

# print(f"Soma: {soma}")
# print(f"Subtração: {subtracao}")
# print(f"Divisão: {round(divisao,2)}")
# print(f"Multiplicação: {multiplicacao}")


#Calculadora V2
#Crie um programa que recebe dois números decimais e um operador (+,-,*,/). Imprima na tela o resultado da operação escolhida.


# print(eval(f"{n1} {op} {n2}"))

# if (op == "+"):
#     soma = n1 + n2
#     print(f"Soma: {soma}")
    
# if (op == "-"):
#     subtracao = n1 - n2
#     print(f"Subtracao: {subtracao}")
    
# if (op == "/"):
#     divisao = n1 / n2
#     print(f"Divisao: {divisao}")
    
# if (op == "*"):
#     multiplicacao = n1 * n2
#     print(f"Multiplicação: {multiplicacao}")
    
# if (op != "+" and op != "-" and op != "/" and op != "*"):
#     print("Operador Inválido")

# Impedir a divisão por zero de acontecer

# if (op == "+"):
#     soma = n1 + n2
#     print(f"Soma: {soma}")
# elif (op == "-"):
#     subtracao = n1 - n2
#     print(f"Subtração: {subtracao}")
# elif (op == "/"):
#     if (n2 == 0):
#         print("Não é possível realizar divisão por zero!")
#     else:
#         divisao = n1 / n2
#         print(f"Divisão: {divisao}")
# elif (op == "*"):
#     multiplicacao = n1 * n2
#     print(f"Multiplicação: {multiplicacao}")
# else:
#     print("Operador inválido! Tente novamente")

n1 = float(input("Digite o número 1:"))

op = input("Digite o operador (+,-,/,*):")

n2 = float(input("Digite o número 2:"))

resultado = None

if (op == "+"):
    resultado = n1 + n2
    
elif (op == "-"):
    resultado = n1 - n2
    
elif (op == "/"):
    if (n2 == 0):
        resultado = "Não é possível dividir por zero!"
    else:
        resultado = n1 / n2
        
elif (op == "*"):
    resultado = n1 * n2
    
else:
    resultado = "Operador inválido!"
    
if type(resultado) == float:
    nomeDaOperacao = {"+": "Soma", "-": "Subtracao", "**": "Exponenciação"}
    print(f"{nomeDaOperacao[op]}: {resultado}")
else:
    print(resultado)
    
    
