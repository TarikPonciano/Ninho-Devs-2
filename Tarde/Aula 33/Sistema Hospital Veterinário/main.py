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
        print("Ver Pacientes")
        
        pacientes = conexaoBD.consultar("SELECT * FROM paciente")
        
        if pacientes == []:
            print("Não foi possível acessar os pacientes.")
        else:
            print("ID | Nome | Tutor | Espécie | Peso")
            
            for paciente in pacientes:
                print(f"{paciente[0]} | {paciente[1]} | {paciente[2]} | {paciente[3]} | {paciente[4]} kg")
            
            idPaciente = 0
            try:
                idPaciente = int(input("Digite o id do paciente desejado:"))
            except Exception as e:
                print("Erro:", e)
                
            if idPaciente == 0:
                print("Operação Cancelada!")     
            else:
                pacienteEspecifico = conexaoBD.consultarComParametros("SELECT * FROM paciente WHERE id_paciente = %s", (idPaciente,))
                
                if pacienteEspecifico == []:
                    print("Paciente não encontrado!")
                else:
                    print(pacienteEspecifico)  #[(1, 'Marcos', 123, )]
                    print(f'''
        ID: {pacienteEspecifico[0][0]}                  
        Nome: {pacienteEspecifico[0][1]}
        Tutor: {pacienteEspecifico[0][2]}
        Espécie: {pacienteEspecifico[0][3]}
        Peso: {pacienteEspecifico[0][4]}kg                  
                          
                          ''')                 
    elif (op == "2"):
        #Pedir as informações de um novo paciente (nome, tutor, espécie, peso)
        #Executar uma manipulação do tipo Insert
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