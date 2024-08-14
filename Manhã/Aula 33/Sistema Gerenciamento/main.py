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
        print("Cadastro de Paciente")
        
        nome = input("Digite o nome:")
        especie = input("Digite a especie:")
        tutor = int(input("Digite o tutor:"))
        peso = float(input("Digite o peso em kg:"))
        
        sql = '''
        INSERT INTO paciente VALUES (DEFAULT, %s, %s, %s, %s);
        '''
    
        conexaoBD.manipularComParametro(sql, (nome, especie, tutor, peso))
        
        print("Paciente cadastrado com sucesso!")
        
        
    elif (op == "3"):
        pass
    elif (op == "4"):
        
        # Exibir a lista de pacientes na tela
        pacientes = conexaoBD.consultar("SELECT * FROM paciente")
        print("ID | Nome | Espécie | Tutor | Peso")
        for paciente in pacientes:
            print(f"{paciente[0]} | {paciente[1]} | {paciente[2]} | {paciente[3]} | {paciente[4]}")
        
        # Pedir para a pessoa selecionar um paciente pelo id
        
        try:
            idPaciente = int(input("Digite o id do paciente que deseja remover: "))
        except Exception as e:
            print("Erro:",e)
            idPaciente = 0
        
        if idPaciente == 0:
            print("Operação Cancelada!")    
        # Exibir as informações do paciente mostrado na tela
        else:        
            pacienteEscolhido = conexaoBD.consultarComParametro("SELECT * FROM paciente WHERE id_paciente = %s", (idPaciente,))
            
            if (pacienteEscolhido == []):
                print("Paciente não encontrado!")
            else:
                print(f'''
            ID: {pacienteEscolhido[0][0]}          
            Nome: {pacienteEscolhido[0][1]}          
            Espécie: {pacienteEscolhido[0][2]}
            Tutor: {pacienteEscolhido[0][3]}
            Peso: {pacienteEscolhido[0][4]}''')
        
        # Perguntar se a pessoa deseja remover o paciente
            confirmacao = input("Confirme se deseja remover o paciente (sim/não):")
        
        # Se sim, realizar uma manipulação do tipo DELETE para remover o paciente do banco 
            if (confirmacao == "sim"):
                conexaoBD.manipularComParametro("DELETE FROM paciente WHERE id_paciente = %s",(idPaciente,))
                print("Paciente removido com sucesso!")
            else:
                print("Operação Cancelada")
        
        pass
    elif (op == "0"):
        break
    else:
        print("Você digitou uma opção inválida!")
    
    input("Tecle ENTER para continuar")

# Implemente a funcionalidade ver pacientes