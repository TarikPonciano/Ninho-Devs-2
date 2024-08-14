import mysql.connector
# Crie um programa de gerenciamento de um hospital veterinário. Esse programa deve conter um menu no formato:

# 1. Ver pacientes
# 2. Cadastrar paciente
# 3. Alterar cadastro de paciente
# 4. Remover paciente
# 0. Sair

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
        host = "localhost"
        user = "root"
        password = "mysql"
        database = "hospitalvet"
        
        con = None
        cursor = None
        pacientes = []
        
        try:
            con = mysql.connector.connect(host=host, user=user, password=password, database=database)
            cursor = con.cursor()
            
            cursor.execute("SELECT * FROM paciente")
            pacientes = cursor.fetchall()
            
        except mysql.connector.Error as e:
            #O que fazer/imprimir em caso de erro
            print("Erro de SQL:", e)
        except Exception as e:
            #O que fazer/imprimir em caso de erro
            print("Erro:", e)
        finally:
            #Fechar conexão e cursor
            if cursor!= None:
                cursor.close()
            if con != None and con.is_connected():
                con.close()
                
        print("ID | NOME | ESPÉCIE | TUTOR | PESO")
            
        for paciente in pacientes:
            print(f"{paciente[0]} | {paciente[1]} | {paciente[2]} | {paciente[3]} | {paciente[4]}")
        
        
        
        # Escolher um paciente pelo id
        idPaciente = 0
                
        try:    
            idPaciente = int(input("Digite o id do paciente que deseja ver mais detalhes: "))
        except Exception as e:
            print("Você digitou um id inválido!")
            
        if idPaciente == 0:
            print("Finalizando consulta!")
        else:
            host = "localhost"
            user = "root"
            password = "mysql"
            database = "hospitalvet"
            
            con = None
            cursor = None
            pacienteEscolhido = []
            
            try:
                con = mysql.connector.connect(host=host, user=user, password=password, database=database)
                cursor = con.cursor()
                
                cursor.execute("SELECT * FROM paciente WHERE id_paciente = %s", (idPaciente,))
                pacienteEscolhido = cursor.fetchall()
                
            except mysql.connector.Error as e:
                #O que fazer/imprimir em caso de erro
                print("Erro de SQL:", e)
            except Exception as e:
                #O que fazer/imprimir em caso de erro
                print("Erro:", e)
            finally:
                #Fechar conexão e cursor
                if cursor!= None:
                    cursor.close()
                if con != None and con.is_connected():
                    con.close()
                    
            if pacienteEscolhido == []:
                print("Paciente não encontrado!")
            else:
                print(pacienteEscolhido) # [(10, 'Nome', 'Espécie', 'Tutor', 20.0)] 
                
                print(f'''
    ID: {pacienteEscolhido[0][0]}
    Nome: {pacienteEscolhido[0][1]}    
    Espécie: {pacienteEscolhido[0][2]}
    Tutor: {pacienteEscolhido[0][3]}
    Peso: {pacienteEscolhido[0][4]}kg
                      ''')
            #Imprima as informações do paciente no formato:
            
            #Id:
            #Nome:
            #Espécie:
            #Tutor:
            #Peso:
            
            #Lógica apenas com lista
            # pacienteEscolhido = None
            # for paciente in pacientes:
            #     if paciente[0] == idPaciente:
            #         pacienteEscolhido = paciente
            #         break
                
            # if pacienteEscolhido == None:
            #     print("Paciente não encontrado")
            # else:
            #     print(pacienteEscolhido)
            
        
        
            
        
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