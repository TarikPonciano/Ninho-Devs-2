import mysql.connector
from conexao import Conexao
# Crie um programa de gerenciamento de um hospital veterinário. Esse programa deve conter um menu no formato:

# 1. Ver pacientes
# 2. Cadastrar paciente
# 3. Alterar cadastro de paciente
# 4. Remover paciente
# 0. Sair

conexaoBD = Conexao("localhost", "root", "mysql", "hospitalvet")

while True:
    
    print('''
    Bem vindo ao PETVET
    
    Menu:
    
    1. Ver Pacientes
    2. Cadastrar Novo Paciente
    3. Alterar Cadastro de Paciente
    4. Remover Paciente
    0. Sair      
          
          ''')
    
    op = input("Digite a opção do menu desejada:")
    
    if (op == "1"):
                  
    elif (op == "2"):
        pass
    elif (op=="3"):
        pass
    elif (op=="4"):
        pass
    elif (op == "0"):
        print("Saindo do programa...")
        break
    else:
        print("Você escolheu uma opção inválida")
    
    input("TECLE ENTER PARA CONTINUAR")
# Implemente a funcionalidade Ver Pacientes