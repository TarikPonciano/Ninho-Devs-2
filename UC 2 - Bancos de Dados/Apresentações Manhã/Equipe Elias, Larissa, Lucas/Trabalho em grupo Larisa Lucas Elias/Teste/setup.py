import mysql.connector
from mysql.connector import Error

def criar_banco_e_tabelas():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',  # Substitua pelo seu usuário do MySQL
            password='mysql'  # Substitua pela sua senha do MySQL
        )
        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("DROP DATABASE IF EXISTS biblioteca")
            cursor.execute("CREATE DATABASE biblioteca")
            cursor.execute("USE biblioteca")
            
            # Criar tabelas
            cursor.execute('''
                CREATE TABLE Usuario (
                    ID_Usuario INT AUTO_INCREMENT PRIMARY KEY,
                    Nome VARCHAR(255) NOT NULL,
                    Email VARCHAR(255) UNIQUE NOT NULL
                )
            ''')

            cursor.execute('''
                CREATE TABLE Livro (
                    ID_Livro INT AUTO_INCREMENT PRIMARY KEY,
                    Titulo VARCHAR(255) NOT NULL,
                    Autor VARCHAR(255) NOT NULL,
                    Ano_Publicacao INT NOT NULL
                )
            ''')

            cursor.execute('''
                CREATE TABLE Emprestimo (
                    ID_Emprestimo INT AUTO_INCREMENT PRIMARY KEY,
                    Data_Emprestimo DATE NOT NULL,
                    Data_Devolucao DATE,
                    ID_Usuario INT,
                    ID_Livro INT,
                    FOREIGN KEY (ID_Usuario) REFERENCES Usuario(ID_Usuario),
                    FOREIGN KEY (ID_Livro) REFERENCES Livro(ID_Livro)
                )
            ''')

            # Inserir dados iniciais
            cursor.execute("INSERT INTO Usuario (Nome, Email) VALUES ('João Silva', 'joao.silva@example.com')")
            cursor.execute("INSERT INTO Usuario (Nome, Email) VALUES ('Maria Oliveira', 'maria.oliveira@example.com')")
            
            cursor.execute("INSERT INTO Livro (Titulo, Autor, Ano_Publicacao) VALUES ('Dom Casmurro', 'Machado de Assis', 1899)")
            cursor.execute("INSERT INTO Livro (Titulo, Autor, Ano_Publicacao) VALUES ('A Moreninha', 'Joaquim Manuel de Macedo', 1844)")

            cursor.execute("INSERT INTO Emprestimo (Data_Emprestimo, Data_Devolucao, ID_Usuario, ID_Livro) VALUES ('2024-08-20', NULL, 1, 1)")
            
            connection.commit()
            print("Banco de dados e tabelas criados e preenchidos com sucesso.")
    
    except Error as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

if __name__ == "__main__":
    criar_banco_e_tabelas()
