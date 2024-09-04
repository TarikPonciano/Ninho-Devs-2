from Conexao import Conexao


conexaoBD = Conexao("localhost", "root", "mysql", "")


conexaoBD.manipular("CREATE DATABASE IF NOT EXISTS Esports")

conexaoBD = Conexao("localhost", "root", "mysql", "Esports")


sql_create_table_jogadores = """
CREATE TABLE IF NOT EXISTS Jogadores (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    Nome VARCHAR(100) NOT NULL,
    Nickname VARCHAR(50) NOT NULL UNIQUE,
    Idade INT,
    Nacionalidade VARCHAR(50)
);
"""
conexaoBD.manipular(sql_create_table_jogadores)


sql_create_table_equipes = """
CREATE TABLE IF NOT EXISTS Equipes (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    Nome VARCHAR(100) NOT NULL,
    Pais VARCHAR(50)
);
"""
conexaoBD.manipular(sql_create_table_equipes)


sql_create_table_torneios = """
CREATE TABLE IF NOT EXISTS Torneios (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    Nome VARCHAR(100) NOT NULL,
    Data_Inicio DATE,
    Data_Fim DATE,
    Premiacao DECIMAL(10, 2)
);
"""
conexaoBD.manipular(sql_create_table_torneios)


sql_create_table_jogadores_equipes = """
CREATE TABLE IF NOT EXISTS Jogadores_Equipes (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    ID_Jogador INT,
    ID_Equipe INT,
    Posicao ENUM('Titular', 'Reserva'),
    FOREIGN KEY (ID_Jogador) REFERENCES Jogadores(ID),
    FOREIGN KEY (ID_Equipe) REFERENCES Equipes(ID)
);
"""
conexaoBD.manipular(sql_create_table_jogadores_equipes)

sql_create_table_equipes_torneios = """
CREATE TABLE IF NOT EXISTS Equipes_Torneios (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    ID_Equipe INT,
    ID_Torneio INT,
    FOREIGN KEY (ID_Equipe) REFERENCES Equipes(ID),
    FOREIGN KEY (ID_Torneio) REFERENCES Torneios(ID)
);
"""
conexaoBD.manipular(sql_create_table_equipes_torneios)

print("Banco de dados e tabelas criados com sucesso!")
