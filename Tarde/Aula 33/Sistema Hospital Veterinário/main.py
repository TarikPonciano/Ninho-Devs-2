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
        
        nome = input("Digite o nome do novo paciente:")  
        tutor = int(input("Digite o id do tutor:"))
        especie = input("Digite a espécie do paciente:")
        peso = float(input("Digite o peso do paciente em kg: "))
        
        #Executar uma manipulação do tipo Insert
        
        conexaoBD.manipularComParametros("INSERT INTO paciente VALUES (DEFAULT, %s, %s, %s, %s)", (nome, tutor, especie, peso))
        
        print("Paciente inserido com sucesso!")
        
    elif (op=="3"):
        # Exibir todos os pacientes na tela seguindo o formato ID | Nome | Tutor | Espécie | Peso
        
        pacientes = conexaoBD.consultar("SELECT * FROM paciente")
        
        if pacientes == []:
            print("Não foram encontrados pacientes!")
        else:
            print("ID | Nome | Tutor | Espécie | Peso")
            for paciente in pacientes:
                print(f"{paciente[0]} | {paciente[1]} | {paciente[2]} | {paciente[3]} | {paciente[4]}") 
            
            # Pedir o id do paciente que desejamos alterar
            try:    
                idEscolhido = int(input("Digite o id do paciente que deseja alterar:"))
            except Exception as e:
                print("Erro:", e)
                idEscolhido = 0
            
        # Mostrar as informações do paciente que deverá ser alterado

            pacienteEscolhido = conexaoBD.consultarComParametros("SELECT * FROM paciente WHERE id_paciente = %s", (idEscolhido,))
            
            if pacienteEscolhido == []:
                print("Paciente não encontrado!")
            else:
                print(f'''
    ID: {pacienteEscolhido[0][0]}
    Nome: {pacienteEscolhido[0][1]}
    Tutor: {pacienteEscolhido[0][2]}
    Espécie: {pacienteEscolhido[0][3]}
    Peso: {pacienteEscolhido[0][4]}
                      ''')
                nome = pacienteEscolhido[0][1]
                tutor = pacienteEscolhido[0][2]
                especie = pacienteEscolhido[0][3]
                peso = pacienteEscolhido[0][4]
        
        # Pedir as novas informações (nome, tutor, espécie, peso)
                novoNome = input("Digite o novo nome:")
                if novoNome == "":
                    novoNome = nome
                    
                novoTutor = int(input("Digite o id do novo tutor:"))
                if novoTutor == 0:
                    novoTutor = tutor
                    
                novaEspecie = input("Digite a nova espécie:")
                if novaEspecie=="":
                    novaEspecie = especie
                    
                novoPeso = float(input("Digite o novo peso:"))
                if novoPeso == 0:
                    novoPeso = peso
        # Executar a manipulação com o comando Update
                sqlAtualizar = '''
                UPDATE paciente
                SET
                nome_paciente = %s,
                id_tutor = %s,
                especie_paciente = %s,
                peso_paciente = %s
                WHERE
                id_paciente = %s
                '''
                conexaoBD.manipularComParametros(sqlAtualizar, (novoNome, novoTutor, novaEspecie, novoPeso, idEscolhido))
                print("Paciente atualizado com sucesso.")
    elif (op=="4"):
        # Exibir todos os pacientes na tela seguindo o formato ID | Nome | Tutor | Espécie | Peso
        
        pacientes = conexaoBD.consultar("SELECT * FROM paciente")
        
        if (pacientes == []):
            print("Não foram encontrados pacientes!")
        else:
            print("ID | Nome | Tutor | Espécie | Peso")
            
            for paciente in pacientes:
                print(f"{paciente[0]} | {paciente[1]} | {paciente[2]} | {paciente[3]} | {paciente[4]}")
        
            # Pedir que o usuário escreva o id do paciente que deseja remover
            try:
                idPaciente = int(input("Digite o id do paciente que deseja remover:"))
            except Exception as e:
                print("Erro:", e)
                idPaciente = 0
                
            if idPaciente == 0:
                print("Operação Cancelada!")
            else:
                
            # Exibir na tela as informações deste paciente no formato:
            # ID: <>
            # Nome: <>
            # Tutor: <>
            # Espécie: <>
            # Peso: <>kg
            
                pacienteEscolhido = conexaoBD.consultarComParametros("SELECT * FROM paciente WHERE id_paciente = %s", (idPaciente,))
                
                if pacienteEscolhido == []:
                    print("Paciente não foi encontrado!")
                else:
                    print(f'''
    ID: {pacienteEscolhido[0][0]}
    Nome: {pacienteEscolhido[0][1]}
    Tutor: {pacienteEscolhido[0][2]} 
    Espécie: {pacienteEscolhido[0][3]} 
    Peso: {pacienteEscolhido[0][4]}                       
                          ''')
                
                # Perguntar ao usuário se deseja, realmente, remover este paciente.
                
                confirmacao = input("Deseja remover este paciente? (sim/não)")
                
                if (confirmacao.lower() == "sim"):
                    # Se a resposta for sim, realize a manipulação do banco com o comando Delete
                    conexaoBD.manipularComParametros("DELETE FROM paciente WHERE id_paciente = %s", (idPaciente,))
                    print("Paciente Removido com sucesso!")
                else:
                    print("Remoção abortada!")
        
        
        
        
    elif (op == "0"):
        print("Saindo do programa...")
        break
    else:
        print("Você escolheu uma opção inválida")
    
    input("TECLE ENTER PARA CONTINUAR")
# Implemente a funcionalidade Ver Pacientes