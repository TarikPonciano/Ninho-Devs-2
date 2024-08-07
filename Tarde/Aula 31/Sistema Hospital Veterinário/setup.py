import mysql.connector
#Programa para criar banco de dados hospitalvet, criar a tabela paciente e inserir 30 pacientes na tabela.

host = "localhost"
user = "root"
password = "mysql"

conexao = None
cursor = None
#Estabelecer conexão com o banco de dados
#Criar o cursor
#Executar comando SQL de criação do Banco de Dados hospitalvet
try:
    #Criação da conexão e execução das operações SQL
    conexao = mysql.connector.connect(host=host,user=user,password=password)
    cursor = conexao.cursor()
    
    cursor.execute("DROP DATABASE IF EXISTS hospitalvet")
    cursor.execute("CREATE DATABASE hospitalvet")
    
    #Criar tabela paciente
    #id
    #nome
    #id_tutor
    #especie
    #peso
    
    cursor.execute('''CREATE TABLE paciente()''')
      
except mysql.connector.Error as e:
    #Tratamento de erros e impressão de erros
    print("Erro SQL:", e)
except Exception as e:
    print("Erro Python:", e)
finally:
    #Finalizar as variáveis cursor e conexao
    if cursor != None:
        cursor.close()
    if conexao != None and conexao.is_connected():
        conexao.close()



