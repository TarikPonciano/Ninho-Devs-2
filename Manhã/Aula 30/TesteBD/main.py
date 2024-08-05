import mysql.connector

host = "localhost"
user = "root"
password = "mysql"
database = "escol"

conexaoBD = None
cursor = None
try:
    conexaoBD = mysql.connector.connect(host = host, user = user, password = password, database = database)

    print("Conexão Estabelecida!")
    cursor = conexaoBD.cursor()
    
    cursor.execute("asdasdasd")
    #OPERAÇÕES SQL
    
    matricula = int(input("Digite a matricula:"))
    
    f"SELECT * FROM aluno WHERE matriculaaluno = {matricula}"

    
except mysql.connector.Error as e:
    print(e.msg)
    
finally:
    if cursor:
        cursor.close()
    if conexaoBD:
        conexaoBD.close()
    

#Faça um programa que se conecta ao banco de dados escola, realiza uma consulta e mostra na tela todos os alunos no formato "<matricula>. <nome>" e na sequência pede que o usuário escreva a matricula e mostra na tela as informações do aluno da matricula especificada.
