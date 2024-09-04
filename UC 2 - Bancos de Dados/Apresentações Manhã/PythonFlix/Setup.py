from conexao import Conexao

def criar_banco_e_tabelas():
    try:
        # Conectar ao MySQL sem especificar um banco de dados
        conexaoBanco = Conexao("localhost", "root", "mysql", "")
        conexaoBanco.conectar()

        # Criação do banco de dados
        conexaoBanco.manipular("DROP DATABASE IF EXISTS pythonflix")
        conexaoBanco.manipular("CREATE DATABASE pythonflix")
        print("Banco de dados 'pythonflix' criado com sucesso!")

        # Fechar a conexão atual
        conexaoBanco.desconectar()

        # Reconectar ao banco de dados 'pythonflix'
        conexaoBanco = Conexao("localhost", "root", "mysql", "pythonflix")
        conexaoBanco.conectar()
        
        # Criação das tabelas
        conexaoBanco.manipular('''
            CREATE TABLE usuario (
                id_cliente INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                nickname VARCHAR(20) NOT NULL DEFAULT 'CAMPO OBRIGATORIO',
                nome VARCHAR(255) NOT NULL DEFAULT 'SEM NOME',
                telefone CHAR(11) NOT NULL DEFAULT 'XXXXXXXXXXX',
                cpf CHAR(11) NOT NULL,
                CONSTRAINT check_cpf CHECK (LENGTH(cpf) = 11),
                CONSTRAINT check_telefone CHECK (LENGTH(telefone) = 11)
            )
        ''')

        conexaoBanco.manipular('''
            CREATE TABLE filmes (
                id_filme INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                nome VARCHAR(255) NOT NULL,
                genero VARCHAR(255) NOT NULL,
                ano YEAR,
                valor_locacao DOUBLE NOT NULL DEFAULT 8.00,
                disponibilidade BOOLEAN NOT NULL DEFAULT TRUE
            )
        ''')

        conexaoBanco.manipular('''
            CREATE TABLE aluguel (
                id_aluguel INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                id_filme INT NOT NULL,
                id_cliente INT NOT NULL,
                data_aluguel DATE NOT NULL,
                data_devolucao DATE NULL,
                CONSTRAINT fk_filme FOREIGN KEY (id_filme) REFERENCES filmes (id_filme),
                CONSTRAINT fk_cliente FOREIGN KEY (id_cliente) REFERENCES usuario (id_cliente)
            )
        ''')

        # Inserção de dados
        conexaoBanco.manipular('''
            INSERT INTO filmes (nome, genero, ano, valor_locacao) VALUES
            ('Um Sonho de Liberdade', 'Drama', 1994, 8.00),
            ('O Poderoso Chefão', 'Crime', 1972, 8.00),
            ('O Cavaleiro das Trevas', 'Ação', 2008, 8.00),
            ('Pulp Fiction', 'Crime', 1994, 8.00),
            ('Forrest Gump', 'Drama', 1994, 8.00),
            ('A Origem', 'Ficção Científica', 2010, 8.00),
            ('Matrix', 'Ficção Científica', 1999, 8.00),
            ('Clube da Luta', 'Drama', 1999, 8.00),
            ('O Senhor dos Anéis: O Retorno do Rei', 'Fantasia', 2003, 8.00),
            ('Os Vingadores', 'Ação', 2012, 8.00),
            ('Titanic', 'Romance', 1997, 8.00),
            ('Jurassic Park', 'Aventura', 1993, 8.00),
            ('Star Wars: Episódio IV - Uma Nova Esperança', 'Ficção Científica', 1977, 8.00),
            ('O Rei Leão', 'Animação', 1994, 8.00),
            ('Gladiador', 'Ação', 2000, 8.00),
            ('Os Infiltrados', 'Crime', 2006, 8.00),
            ('Coração Valente', 'Drama', 1995, 8.00),
            ('A Lista de Schindler', 'Drama', 1993, 8.00),
            ('O Poderoso Chefão II', 'Crime', 1974, 8.00),
            ('Os Suspeitos', 'Crime', 1995, 8.00);
        ''')

        conexaoBanco.manipular('''INSERT INTO usuario (nickname, nome, telefone, cpf) VALUES
                               ('thompsbr', 'Thomas Andersson', '85995234125', '41269812341'),
                               ('marinny', 'Marianny Fernandes', '88744259632', '12345678910');''')

        print("Tabelas e dados inseridos com sucesso!")

    except Exception as e:
        print(f"Erro ao executar o comando: {e}")

if __name__ == "__main__":
    criar_banco_e_tabelas()
