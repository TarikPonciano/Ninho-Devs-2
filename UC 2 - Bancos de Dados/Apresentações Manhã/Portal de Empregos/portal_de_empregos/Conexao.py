import mysql.connector
class Conexao:
    
    def __init__(self, host, user, password, database):
        self._host = host
        self._user = user
        self._password = password
        self._database = database
        
        self._con = None
        self._cursor = None
        
    def conectar(self):
        
        try:
            self._con = mysql.connector.connect(host=self._host, user=self._user, password=self._password, database=self._database)
        except mysql.connector.Error as e:
            print("Erro de SQL:",e)
        except Exception as e:
            print("Erro:",e)
            
        try:
            self._cursor = self._con.cursor()
        except mysql.connector.Error as e:
            print("Erro de SQL:",e)
        except Exception as e:
            print("Erro:",e)
            
    def desconectar(self):
        try:
            self._cursor.close()
            # self._cursor = None
        except mysql.connector.Error as e:
            print("Erro de SQL:",e)
        except Exception as e:
            print("Erro:",e)
            
        try:
            self._con.close()
            # self._con = None
        except mysql.connector.Error as e:
            print("Erro de SQL:",e)
        except Exception as e:
            print("Erro:",e)
            
    def consultar(self, sql):
        self.conectar()
        resultado = []
        
        try:
            self._cursor.execute(sql)
            resultado = self._cursor.fetchall()
        except mysql.connector.Error as e:
            print("Erro de SQL:",e)
        except Exception as e:
            print("Erro:",e)
            
        self.desconectar()
        
        return resultado    
    
    def consultarComParametro(self, sql, parametros):
        self.conectar()
        resultado = []
        
        try:
            self._cursor.execute(sql, parametros)
            resultado = self._cursor.fetchall()
        except mysql.connector.Error as e:
            print("Erro de SQL:",e)
        except Exception as e:
            print("Erro:",e)
            
        self.desconectar()
        
        return resultado
    
    def manipular(self, sql):
        self.conectar()
        
        resultado = 0
        
        try:
            self._cursor.execute(sql)
            resultado = self._cursor.lastrowid
            self._con.commit()
        except mysql.connector.Error as e:
            print("Erro de SQL:", e)
        except Exception as e:
            print("Erro:", e)
        
        self.desconectar()
        return resultado
            
    def manipularComParametro(self, sql, parametros):
        self.conectar()
        resultado = 0
        
        try:
            self._cursor.execute(sql, parametros)
            resultado = self._cursor.lastrowid
            self._con.commit()
        except mysql.connector.Error as e:
            print("Erro de SQL:", e)
        except Exception as e:
            print("Erro:", e)
        
        self.desconectar()
        return resultado
            
        