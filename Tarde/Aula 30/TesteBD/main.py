import mysql.connector
import credencial

host = credencial.host
user = credencial.user
password = credencial.password
database = credencial.database

conexaoBD = mysql.connector.connect(host=host, user=user, password=password, database=database)

print("Conexão Estabelecida!")

cursor = conexaoBD.cursor()

cursor.execute("SELECT VERSION()")

resultado = cursor.fetchall()

print(resultado)
#Imprimir na tela a mensagem "A VERSÃO DO MYSQL É x.xxx"
print(f"A VERSÃO DO MYSQL É {resultado[0][0]}")

#Faça uma consulta e exiba na tela todos os alunos cadastrados na tabela aluno

cursor.execute("SELECT * FROM aluno")
resultado = cursor.fetchall()

print(resultado)

#Exiba na tela a matricula e nome do primeiro aluno e do último aluno. No formato "<matricula>. <nome>"
print(f"{resultado[0][0]}. {resultado[0][2]} - {resultado[0][6]}")

print(f"{resultado[-1][0]}. {resultado[-1][2]} - {resultado[-1][-1]}")

#Imprima todos os alunos no formato "<matricula>. <nome>"

for aluno in resultado:
    print(f"{aluno[0]}. {aluno[2]}")