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
            print(f"{paciente[0]} | {paciente[1]} | {paciente[2]} | {paciente[3]} |{paciente[4]}")
        
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