from conec_musicfy import Connection

config = {"user": "root", "host": "127.0.0.1", "password": "mysql", "database": ""}

con_db = Connection(**config)

# create DB

query_database = """CREATE DATABASE musicfy"""

# cerate tables
query_table_user = """
CREATE TABLE usuario (
id_usuario INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
nome_usuario VARCHAR(255) NOT NULL,
login_usuario VARCHAR(255) NOT NULL,
senha_usuario VARCHAR(50) NOT NULL,
role_usuario VARCHAR(50) NOT NULL DEFAULT 'user',
idade_usuario INT,
CONSTRAINT check_idade CHECK(idade_usuario > 0 and idade_usuario < 150)
);
"""

query_table_songs = """
CREATE TABLE musica (
id_musica INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
nome_musica VARCHAR(255) NOT NULL,
tipo_musica VARCHAR(255) NOT NULL,
duracao_musica DECIMAL(4,2) NOT NULL
);
"""

query_table_listen = """
CREATE TABLE escuta (
id_escuta INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
id_usuario INT NOT NULL,
id_musica INT NOT NULL,
vezes_tocadas INT DEFAULT 0,
dia_reproducao_musica DATE,
CONSTRAINT fk_usuario FOREIGN KEY(id_usuario) REFERENCES usuario(id_usuario),
CONSTRAINT fk_musica FOREIGN KEY(id_musica) REFERENCES musica(id_musica)
);
"""


# add items
query_add_songs = """
INSERT INTO musica (id_musica, nome_musica, tipo_musica, duracao_musica) VALUES
(1, 'Bohemian Rhapsody', 'Rock', '5.55'),
(2, 'Imagine', 'Pop', '3.03'),
(3, 'Smells Like Teen Spirit', 'Grunge', '5.01'),
(4, 'Billie Jean', 'Pop', '4.54'),
(5, 'Hotel California', 'Rock', '6.30'),
(6, 'Like a Rolling Stone', 'Rock', '6.09'),
(7, 'What a Wonderful World', 'Jazz', '2.59'),
(8, 'Sweet Child O Mine', 'Rock', '5.56'),
(9, 'Uptown Funk', 'Pop', '4.30'),
(10, 'Stairway to Heaven', 'Rock', '8.02');
"""

con_db.setup_db(
    query_database,
    query_add_songs,
    query_table_user,
    query_table_songs,
    query_table_listen,
)
