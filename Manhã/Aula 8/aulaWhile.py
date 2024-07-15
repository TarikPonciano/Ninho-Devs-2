# Imprima os números de 1 a 500
# contador = 1
# while contador <= 500:
#     print(contador)
#     contador += 1
# Imprima os números pares de 1 a 500
# contador = 1
# while(contador <= 500):
#     if(contador % 2 == 0):
#         print(contador)
#     contador += 1

# Imprima a soma de 1 a 500

# contador = 1
# soma = 0

# while (contador <= 500):
#     if (contador % 2 == 0):
#         soma += contador
#     contador += 1
    

# print(soma)

#Crie um jogo onde o jogador deve advinhar o número secreto. O jogo deve parar apenas quando o jogador acertar o número.

# secreto = 8

# palpite = int(input("Digite seu palpite:"))

# while (palpite != secreto):
#     print("Você errou! Tente novamente!")
#     palpite = int(input("Digite um novo palpite:"))
    
# print("Você acertou!")


secreto = 8
tentativas = 0

while (True):
    palpite = int(input("Digite um palpite:"))
    tentativas += 1
   
    
    if (palpite == secreto):
        print(f"Parabéns, você acertou! Em {tentativas} tentativas!")
        break
    else:
        print("Que pena, você errou. Tente novamente.")
        
        if (palpite > secreto):
            print("O número secreto é menor que seu palpite.")
        else:
            print("O número secreto é maior que seu palpite.")

#Mostrar o número de tentativas do jogador
#Dar uma dica para o jogador. Avisar se o número secreto é mais alto ou mais baixo do que o palpite
            
#Menu usando while(True)      
# while(True):
#     print('''
# Bem vindo ao sistema XYZ

# Menu:

# 1. Ver Funcionários
# 2. Inserir Funcionário
# 3. Remover Funcionário
# 0. Sair do Programa
#           ''')
#     op = input("Escolha uma opção do menu:")
    
#     if (op == "1"):
#         print("Você está acessando o Ver Funcionários!")
#     elif (op == "2"):
#         print("Você está acessando o Inserir Funcionário!")
#     elif(op == "3"):
#         print("Você está acessando o Remover Funcionário!")
#     elif(op == "0"):
#         print("Você está saindo do programa...")
#         break
#     else:
#         print("Você digitou uma operação inválida.")
        
#     input("TECLE ENTER PARA CONTINUAR!")
    


    