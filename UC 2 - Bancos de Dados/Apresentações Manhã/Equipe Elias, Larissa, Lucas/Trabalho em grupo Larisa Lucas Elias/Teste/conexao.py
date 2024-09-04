import mysql.connector
from mysql.connector import Error

def conectar():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',  # Substitua pelo seu usuário do MySQL
            password='mysql',  # Substitua pela sua senha do MySQL
            database='biblioteca'
        )
        if connection.is_connected():
            print("Conectado ao banco de dados MySQL")
            return connection
    except Error as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None
