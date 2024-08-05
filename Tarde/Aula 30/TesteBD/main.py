import mysql.connector

host = "localhost"
user = "root"
password = "mysql"
database = "escol"

conexaoBD = None
cursor = None

try:
    conexaoBD = mysql.connector.connect(host=host, user=user, password = password, database=database)

    print("Conexão Estabelecida!")
    cursor = conexaoBD.cursor()
    
    #OPERAÇÕES SQL 
    
    #Visualizar os alunos do banco escola no padrão
    #<matricula>. <nome> - <cpf>
    
    #Peça ao usuário um número de matricula e exiba as informações completas do aluno escolhido
    #Dica: cursor.execute(f"SELECT * FROM aluno WHERE matriculaaluno = {matricula}")
       
except mysql.connector.Error as e:
    print(e.msg)
finally:
    if cursor != None:
        cursor.close()
    if conexaoBD != None:
        conexaoBD.close()
        
        
# 
    


