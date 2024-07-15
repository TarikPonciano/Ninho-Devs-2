# Crie um dicionário dos sabores de sorvete de uma sorveteria. O dicionario deverá ser formado pela chave representado pelo código do sabor e pelo valor representado pelo nome do sabor. Crie 5 sabores. Exemplo:
#"001": Chocolate

#Utilizando esse dicionário, crie um programa que pede que o usuário digite o código do sabor desejado e imprime o sabor na tela.

#Melhore o programa e agora permita que o usuário possa escolher sabores até digitar "sair". Ao final imprima todos os sabores escolhidos.

#CRUD - Create Read Update Delete
# Inserir
# Ler
# Atualizar
# Deletar

# print('''
# 001 - Chocolate - R$ 3.00
# 002 - Morango - R$ 2.90
# 003 - Baunilha - R$ 3.20
# 004 - Creme - R$ 3.00
# 005 - Limão - R$ 2.50
# ''')

# dictSabores = {
#     "001": "Chocolate",
#     "002": "Morango",
#     "003": "Baunilha",
#     "004": "Creme",
#     "005": "Limão",
#     "006": "Flocos",
#     "007": "Sonho de Valsa"
# }

# dictPrecos = {
#     "001": 3.0,
#     "002": 3.2,
#     "003": 2.9,
#     "004": 3.0,
#     "005": 2.5,
#     "006": 3.5,
#     "007": 4.0
# }

#Modificações
# Crie um programa que permite ao usuário cadastrar 1 sabor de sorvete, o programa deverá pedir código, nome e preço do sorvete e cadastra-lo no dicionário de sorvetes. Na sequência o programa irá mostrar o cardápio atualizado, o usuário deverá escolher um sabor específico e a quantidade de bolas, no final o programa deverá imprimir o valor total do sorvete.
sorvete = {
    "nome"
    "preco"
}
dictSorvetes = {
    "001": {"nome": "Chocolate", "preco": 3},
    "002": {"nome": "Morango", "preco": 3.2},
    "003": {"nome": "Menta", "preco": 4},
    "004": {"nome": "Abacaxi", "preco": 4.1},
    "005": {"nome": "Limão", "preco": 3.3},
    "006": {"nome": "Flocos", "preco": 4.2}
}

#Se a pessoa digitar "Sair" no campo código, para de cadastrar
while (True):
    
    print("Cadastre um sabor: ")
    codigo = input("Digite o código do sorvete: ")

    if (codigo == "Sair"):
        break
    
    nome = input("Digite o nome do sabor: ")

    preco = float(input("Digite o preco do sorvete: "))

    dictSorvetes[codigo] = {"nome": nome, "preco": preco}

for codigo in dictSorvetes:
    
    sorvete = dictSorvetes[codigo]
    
    print(f"{codigo} - {sorvete["nome"]} - {sorvete["preco"]}")
    
    # print(f"{codigo} - {dictSorvetes[codigo]["nome"]} - {dictSorvetes[codigo]["preco"]}")

while (True):
    codigo = input("Digite o código do sabor que você deseja: ")

    if (codigo in dictSorvetes):

        quantidade = int(input("Quantas unidades de sorvete você deseja: "))

        valorTotal = quantidade * dictSorvetes[codigo]["preco"]

        print("O sabor escolhido foi: ",dictSorvetes[codigo]["nome"])

        print(F"Você pediu {quantidade} unidade(s) e custou: R$ {valorTotal}")
        
        break
    else:
        print("O código inserido não existe!")