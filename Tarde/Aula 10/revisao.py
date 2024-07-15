#Criar um programa que recebe 4 notas válidas e imprime a média do aluno ao final.

#Criar um programa que pergunta quantas notas deverão ser inseridas e após esse número de notas válidas serem inseridas, imprime a média ao final.

#Criar um jogo de advinhação onde é definido um número secreto no início da execução do programa e o usuário deve dar um palpite. Dê dicas para o usuário a cada erro. O programa encerra ao acertar.

#Criar uma calculadora. Seu programa deverá pedir dois números (float) e exibir um menu com as opções disponíveis, exemplo:
# 1. Soma (+)
# 2. Subtração
# 3. Divisão
# 4. Multiplicação
# 0. Sair
#Ao escolher uma das opções o programa irá executar a operação desejada e exibir o resultado na tela. O programa deverá executar ATÉ QUE a pessoa escolha a opção 0. Sair. Impeça de acontecer divisão por 0


#Crie um programa em que a pessoa digita um número que representa os 10 primeiros números pares e imprima cada um deles na tela.

# numero = 0
# qtdPares = 0

# while qtdPares < 100:
    
#     if (numero % 2) == 0:
#         print(numero)
#         qtdPares += 1
    
#     numero += 1
    
# Crie um sistema de carrinho de compras, onde o usuário insere o valor de uma compra e ao decidir parar vê na tela o total da compra.

# total = 0
# # continuar = "Sim"
# qtdProdutos = 0

# while (qtdProdutos < 10):
    
#     valor = float(input("Digite o valor da sua compra: "))
    
#     if(valor >= 0 and valor <= 100):
    
#         total += valor
#         qtdProdutos += 1
#     else:
#         print("Digite um valor válido!")
#     # continuar = input("Deseja continuar? (Sim/Não)")
    

# print("O total da sua compra é: R$",total)

# total = 0

# while (True):
    
#     valor = input("Digite um valor: (Digite 'sair' para encerrar)")
    
#     if (valor.lower() == "sair"):
#         print("Encerrando processo de compras!")
#         break
#     else:
#         total += float(valor)
    

    
# print(total)

#CRUD
# C - Create > Inserir
# R - Read > Ver/Ler
# U - Update > Alterar/Atualizar
# D - Delete > Remover/Deletar
while(True):
    print('''
    ------Sistema de Gerenciamento Ninho Devs------
    
    Menu:
    1. Ver Funcionários
    2. Inserir Funcionário
    3. Alterar Funcionário
    4. Remover Funcionário
    0. Sair      
          ''')
    
    op = input("Digite a opção desejada: ")
    
    if (op == "1"):
        print("Executando Ver Funcionários")
    elif (op == "2"):
        print("Executando Inserir Funcionário")
    elif (op == "3"):
        print("Executando Alterar Funcionário")
    elif (op == "4"):
        print("Executando Remover Funcionário")
    elif (op == "0"):
        print("Saindo do programa...")
        break
    else:
        print("Digite uma opção válida.")
        
    input("Digite ENTER para continuar")

