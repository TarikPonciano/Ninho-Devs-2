import mysql.connector

host = "localhost"
user = "root"
password = "mysql"
database = "escola"

conexaoBD = mysql.connector.connect(host = host, user = user, password = password, database = database)

print("Conexão Estabelecida!")

cursor = conexaoBD.cursor()

cursor.execute("SELECT VERSION()")

resultado = cursor.fetchall()

print(f"A VERSÃO DO MYSQL É {resultado[0][0]}")

cursor.execute("SELECT * FROM aluno")
resultado = cursor.fetchall()

for aluno in resultado:
    print(f"{aluno[0]}. {aluno[2]}")
    
cursor.execute("Insert into aluno values (default, '12345999', 'Novo Aluno', default, default, 99, default)")

print("Aluno inserido com sucesso!")

conexaoBD.commit()

