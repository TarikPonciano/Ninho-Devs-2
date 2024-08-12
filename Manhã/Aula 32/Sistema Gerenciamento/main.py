import mysql.connector
from Conexao import Conexao
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
    
    1. Ver pacientes
    2. Cadastrar novo paciente
    3. Alterar cadastro de paciente
    4. Remover paciente
    0. Sair      
          ''')
    
    op = input("Digite a opção do menu desejada: ")
    
    if (op == "1"):
        #Imprimir todos os pacientes no formato
        
        #ID | Nome | Espécie | Tutor | Peso
        
        pacientes = conexaoBD.consultar("Select * from paciente")
        
        print("ID | Nome | Espécie | Tutor | Peso")
        
        for paciente in pacientes:
            
            print(f"{paciente[0]} | {paciente[1]} | {paciente[2]} | {paciente[3]} | {paciente[4]}")
            
        try:    
            idPaciente = int(input("Digite o id do paciente escolhido:"))
        except Exception as e:
            print("Erro:",e)
            idPaciente = 0
            
        if idPaciente == 0:
            print("Encerrando Operação")
        else:
            pacienteEscolhido = conexaoBD.consultarComParametro("SELECT * FROM paciente WHERE id_paciente = %s", (idPaciente,))
            
            if pacienteEscolhido == []:
                print("Paciente não encontrado!")
            else:
                print(f'''
        ID: {pacienteEscolhido[0][0]}
        Nome: {pacienteEscolhido[0][1]}
        Espécie: {pacienteEscolhido[0][2]}
        Tutor: {pacienteEscolhido[0][3]}
        Peso: {pacienteEscolhido[0][4]} kg
                      ''')
    
        #Imprima as informações do paciente no formato:
        
        #Id:
        #Nome:
        #Espécie:
        #Tutor:
        #Peso:
        
        
    elif (op == "2"):
        pass
    elif (op == "3"):
        pass
    elif (op == "4"):
        pass
    elif (op == "0"):
        break
    else:
        print("Você digitou uma opção inválida!")
    
    input("Tecle ENTER para continuar")

# Implemente a funcionalidade ver pacientes