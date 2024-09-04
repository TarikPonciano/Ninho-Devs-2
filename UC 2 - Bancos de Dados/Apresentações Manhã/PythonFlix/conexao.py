import mysql.connector

class Conexao:
    def __init__(self, host, usuario, senha, banco):
        self.host = host
        self.usuario = usuario
        self.senha = senha
        self.banco = banco
        self.conexao = None
        self.cursor = None

    def conectar(self):
        if self.conexao is None or not self.conexao.is_connected():
            try:
                self.conexao = mysql.connector.connect(
                    host=self.host,
                    user=self.usuario,
                    password=self.senha,
                    database=self.banco
                )
                self.cursor = self.conexao.cursor()
                print("Conectado ao banco de dados com sucesso.")
            except mysql.connector.Error as err:
                print(f"Erro ao conectar ao banco de dados: {err}")

    def desconectar(self):
        if self.cursor:
            self.cursor.close()
        if self.conexao:
            self.conexao.close()
        print("Desconectado do banco de dados.")

    def manipular(self, sql, dados=None):
        try:
            self.conectar()
            if dados:
                self.cursor.execute(sql, dados)
            else:
                self.cursor.execute(sql)
            self.conexao.commit()
            print("Comando executado com sucesso.")
        except mysql.connector.Error as err:
            print(f"Erro ao executar o comando: {err}")
        finally:
            self.desconectar()

    def consultar(self, sql, dados=None):
        try:
            self.conectar()
            if dados:
                self.cursor.execute(sql, dados)
            else:
                self.cursor.execute(sql)
            resultados = self.cursor.fetchall()
            return resultados
        except mysql.connector.Error as err:
            print(f"Erro ao executar a consulta: {err}")
            return []
        finally:
            self.desconectar()
            
    def executar_com_parametros(self, sql, dados):
        try:
            self.conectar()
            self.cursor.execute(sql, dados)
            self.conexao.commit()
            print("Comando executado com sucesso.")
        except mysql.connector.Error as err:
            print(f"Erro ao executar o comando com parâmetros: {err}")
        finally:
            self.desconectar()
