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
    
    1. Ver Pacientes
    2. Cadastrar Novo Paciente
    3. Alterar Cadastro de Paciente
    4. Remover Paciente
    0. Sair      
          
          ''')
    
    op = input("Digite a opção do menu desejada:")
    
    if (op == "1"):
        # Conectar com o banco
        # Realizar consulta
        # Desconectar do banco
        # Mostrar resultados na tela
        
        host = "localhost"
        user = "root"
        password = "mysql"
        database = "hospitalvet"    
        
        con = None
        cursor = None
        pacientes = []
        
        try:
            con = mysql.connector.connect(host = host, user = user, password = password, database = database)
            cursor = con.cursor()
            
            cursor.execute("SELECT * FROM paciente")
            pacientes = cursor.fetchall() 
        except mysql.connector.Error as e:
            print("Erro de SQL:", e)
        except Exception as e:
            print("Erro:", e)
        finally:
            if cursor != None:
                cursor.close()
            if con != None and con.is_connected():
                con.close()
        
        if pacientes == []:
            print("Não foram encontrados pacientes!")
        else:
            print("ID | Nome | Tutor | Espécie | Peso")
            for paciente in pacientes:
                print(f"{paciente[0]} | {paciente[1]} | {paciente[2]} | {paciente[3]} | {paciente[4]}")
                
            #Pedir ao usuário o id do paciente que ele deseja visualizar e exibir no formato:
            #ID:
            #Nome:
            #Tutor:
            #Espécie:
            #Peso: 
        
            #Credenciais do banco
            #Criar as variáveis
            #Conectar com o banco
            #Consultar o banco
            #Desconectar
            #Mostrar resultado
            
            idPaciente = 0
            try:
                idPaciente = int(input("Digite o id do paciente desejado:"))
            except Exception as e:
                print("Erro:", e)
            
            if idPaciente == 0:
                print("Operação finalizada...")
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
                    
                    cursor.execute("SELECT * FROM paciente WHERE id_paciente = %s",(idPaciente,))
                    pacienteEscolhido = cursor.fetchall()
                                
                except mysql.connector.Error as e:
                    print("Erro de SQL:", e)
                except Exception as e:
                    print("Erro:", e)
                finally:
                    if cursor != None:
                        cursor.close()
                    if con != None and con.is_connected():
                        con.close()   
                        
                if pacienteEscolhido == []:
                    print("Paciente não encontrado!")
                else:
                    print(f'''
        ID: {pacienteEscolhido[0][0]}                  
        Nome: {pacienteEscolhido[0][1]}
        Tutor: {pacienteEscolhido[0][2]}
        Espécie: {pacienteEscolhido[0][3]}
        Peso: {pacienteEscolhido[0][4]} kg              
                          ''')
                         
                    
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