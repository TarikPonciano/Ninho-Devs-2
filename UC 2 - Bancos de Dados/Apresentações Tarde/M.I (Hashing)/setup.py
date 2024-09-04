from Conexao import Conexao
from CypherFinal import CifraVigenere
from luistools import tabber, filler, centerprint
import bcrypt
import base64
#Classe para user NOTA: nome apenas no lado do client
class Usuario:
    def __init__(self, nome, senha=None):
        self.nome = nome
        self.senha_hash = None
        if senha:
            self.senha_hash = self.hash_senha(senha)
    
    def hash_senha(self, senha):
        salt = bcrypt.gensalt()
        senha_hash = bcrypt.hashpw(senha.encode('utf-8'), salt)
        return senha_hash

    def verificar_senha(self, senha):
        return bcrypt.checkpw(senha.encode('utf-8'), self.senha_hash)

    def salvar_no_banco(self, database):
        # Verifica se o usuário já existe
        existe = database.consultarComParametros("SELECT * FROM SIS.CLIENT WHERE NOME = %s", (self.nome,))
        if not existe:
            # Converte o hash da senha para base64 para armazenamento no banco
            senha_hash_str = base64.b64encode(self.senha_hash).decode('utf-8')
            # Salva o usuário no banco de dados
            database.manipularComParametro(
                '''INSERT INTO SIS.CLIENT(NOME, PASSWORD_HASH) VALUES(%s, %s)''',
                (self.nome, senha_hash_str)
            )
            return True
        return False

    @staticmethod
    def buscar_no_banco(nome, database):
        result = database.consultarComParametros("SELECT * FROM SIS.CLIENT WHERE NOME = %s", (nome,))
        if result:
            usuario = Usuario(nome)
            # Converte o hash da senha de base64 de volta para bytes
            usuario.senha_hash = base64.b64decode(result[0][2])
            return usuario
        return None


cifra = CifraVigenere()
database = Conexao("localhost", "root", 'mysql', '')

database.manipular("DROP DATABASE IF EXISTS SIS")
database.manipular("CREATE DATABASE SIS")

#Crição do cliente
database.manipular("CREATE TABLE SIS.CLIENT(ID_CLIENT INT NOT NULL AUTO_INCREMENT PRIMARY KEY, NOME VARCHAR(255) NOT NULL,PASSWORD_HASH VARCHAR(255) NOT NULL)")

#Criação da tabvela de feed de mensagens
database.manipular("CREATE TABLE SIS.FEED(id_entry INT NOT NULL AUTO_INCREMENT PRIMARY KEY, SUBMITTED DATETIME NOT NULL DEFAULT NOW(), id_client INT,CONTENT MEDIUMTEXT, FOREIGN KEY(ID_CLIENT) REFERENCES CLIENT(ID_CLIENT))")

admin = Usuario('admin','admin')
hash1 = str(admin.senha_hash)
#print(hash1)
database.manipularComParametro('''INSERT INTO SIS.CLIENT(PASSWORD_HASH, NOME) VALUES("%s", 'ADMIN')''', (hash1,))

msg = "This message is a test of our upload capabillities and it s meant to be encrypted"
key = "King"
#Encriptação abaixo
crpt = cifra.cifrar(msg, key)

database.manipularComParametro('''INSERT INTO SIS.FEED(id_client, CONTENT) VALUES('1', "%s")''', (crpt,))
response = database.consultar("SELECT * FROM SIS.FEED ")
dresponse = cifra.decifrar(response[0][3], key)
print(response[0][3])
print(dresponse)
