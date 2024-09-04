
import mysql.connector
from mysql.connector import Error

class Conexao:
    def __init__(self, host, user, password, database):
        try:
            self.connection = mysql.connector.connect(
                host=host,
                user=user,
                password=password,
                database=database
            )
            if self.connection.is_connected():
                print("Conexão com o banco de dados bem-sucedida.")
        except Error as e:
            print(f"Erro ao conectar ao banco de dados: {e}")
            self.connection = None

    def manipular(self, sql, valores=None):
        try:
            cursor = self.connection.cursor()
            cursor.execute(sql, valores or ())
            self.connection.commit()
        except Error as e:
            print(f"Erro ao executar o comando: {e}")

    def consultar(self, sql, valores=None):
        try:
            cursor = self.connection.cursor()
            cursor.execute(sql, valores or ())
            return cursor.fetchall()
        except Error as e:
            print(f"Erro ao consultar o banco de dados: {e}")
            return None

    def __del__(self):
        if self.connection.is_connected():
            self.connection.close()
            print("Conexão com o banco de dados fechada.")
