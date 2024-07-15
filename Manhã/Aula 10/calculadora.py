#Criar uma calculadora. Seu programa deverá pedir dois números (float) e exibir um menu com as opções disponíveis, exemplo:
# 1. Soma (+)
# 2. Subtração
# 3. Divisão
# 4. Multiplicação
# 0. Sair
#Ao escolher uma das opções o programa irá executar a operação desejada e exibir o resultado na tela. O programa deverá executar ATÉ QUE a pessoa escolha a opção 0. Sair. Impeça de acontecer divisão por 0


while(True):
    
    num1 = float(input("Digite o número 1: "))
    
    num2 = float(input("Digite o número 2: "))
    
    print('''
    -----Calculadora Ninho de Desenvolvedores-----
    
    Menu:
    
    1. Soma (+)
    2. Subtração (-)
    3. Divisão (/)
    4. Multiplicação (*)
    0. Sair
    
          ''')
    
    op = input("Digite o número ou símbolo da operação desejada: ")
    
    
    if (op == "1" or op == "+"):
        resultado = num1 + num2
        print("A soma é:",resultado)
    elif (op == "2" or op == "-"):
        resultado = num1 - num2
        print("A subtração é:", resultado)
    elif(op=="3" or op == "/"):
        if(num2 != 0):
            resultado = num1 / num2
            print("A divisão é:", resultado)
        else:
            print("Não foi possível realizar a divisão. Divisão por zero detectada!")
    elif(op == "4" or op == "*"):
        resultado = num1 * num2
        print("A multiplicação é:", resultado)
    elif(op == "0"):
        print("Saindo do programa...")
        break
    else:
        print("Você digitou uma operação inválida!")
        
    saida = input("Para continuar tecle Enter. Para sair digite 'sair': ")
    if (saida == "sair"):
        break
        
