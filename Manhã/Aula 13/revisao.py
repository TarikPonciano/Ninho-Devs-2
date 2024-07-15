# CRUD > CREATE READ UPDATE DELETE
# Inserir
# Ler
# Update
# Delete

#Sorveteria.
#Dicionario > Sabor: Preço

# sorveteria = {"Chocolate": 3.5,
#               "Morango": 3,
#               "Menta": 4.3,
#               "Milho": 3.2,
#               "Flocos": 3.7,
#               "Creme": 3}

# for sabor in sorveteria:
#     print(f"{sabor} - R$ {sorveteria[sabor]}")


# sabor = input("Digite um sabor de sorvete:")

# print("Preço: R$", sorveteria[sabor])

# Mostre o cardápio e peça o código e quantidade de bolas para o usuário. Ao final imprima o valor a ser cobrado pelo sorvete.

# print('''
# 001 - Chocolate - R$ 3.00
# 002 - Menta - R$ 4.00
# 003 - Morango - R$ 3.50
# 004 - Creme - R$ 3.70
#       ''')

#Versão 1 - Dicionário Separados
# dictSabores = {"001": "Chocolate",
#                "002": "Menta",
#                "003": "Morango",
#                "004": "Creme",
#                "005": "Creme com Passas"}
# dictPrecos = {"001":3.0,
#               "002":4.0,
#               "003":3.5,
#               "004":3.7,
#               "005":4.0}

# for codigo in dictSabores:
#     print(f"{codigo} - {dictSabores[codigo]} - R$ {dictPrecos[codigo]}")

# codigo = input("Digite o código do sabor desejado: ")

# print(f"Sabor Escolhido: {dictSabores[codigo]}")
# print(f"Preço: R$ {dictPrecos[codigo]}")

#

#Faça um programa que exibe um catálogo de sorvetes (modifique o dicionário para adicionar seus próprios sabores), o cardápio deve conter código, nome e preço. Depois, peça para que o usuário escolha um sabor através do código. Pergunte quantas bolas o cliente deseja e exiba o valor do sorvete no final do programa.

# dictSorvetes = {
# "001": {"nome": "Morango", "preco": 4},
# "002": {"nome": "Flocos", "preco": 3.5},
# "003": {"nome": "Biscoito", "preco":3.7}
# }

# print("Cód | Nome | Preço")
# for codigo in dictSorvetes:

#     print(f"{codigo} - {dictSorvetes[codigo]['nome']} - R$ {dictSorvetes[codigo]['preco']}")
# while (True):
#     codigo = input("Digite o código do sabor desejado: ")

#     if codigo in dictSorvetes:

#         bolas = int(input("Quantas bolas de sorvete você deseja: "))

#         valorTotal = bolas * dictSorvetes[codigo]['preco']

#         print(f"Seu sorvete de {dictSorvetes[codigo]['nome']} custou R$ {valorTotal:.2f}")
#         break
#     else:
#         print("Você escolheu um sabor inexistente. Tente novamente.")

# dictSorvete = {
# "001": {"nome": "Chocolate", "preço": 3},
# "002": {"nome": "Menta", "preço": 4},
# "003": {"nome": "Morango", "preço": 3.5},
# "004": {"nome": "Creme", "preço": 3}
# }

# for codigo in dictSorvete:
#     sorvete = dictSorvete[codigo]
    
#     print(f"{codigo} - {sorvete['nome']} - {sorvete['preço']}")
    
#     # print(f"{codigo} - {dictSorvete[codigo]["nome"]} - {sorvete["preço"]}")


#Crie um sistema de sorveteria onde um funcionário adiciona sabores ao cardápio da sorveteria. Cada sabor deve ser formado por código, nome e preço. A cada sabor será perguntado ao funcionário se ele deseja ou não continuar. Se não desejar continuar, o programa é encerrado e é impresso um cardápio com os sabores inseridos. 

dictSorvetes = {}

codigo = input("Digite o código do sabor: ")
nome = input("Digite o nome do sabor: ")
preco = float(input("Digite o preço do sabor: "))

dictSorvetes[codigo] = {"nome": nome, "preco": preco}


print(dictSorvetes)



