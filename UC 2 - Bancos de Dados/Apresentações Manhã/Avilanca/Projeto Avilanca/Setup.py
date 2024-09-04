from Conexao import Conexao

#Configurar credenciais de conexão do banco (Criar objeto Conexao)
conexaoBD = Conexao("localhost", "root", "mysql", "")

#Criar o banco de dados
conexaoBD.manipular("DROP DATABASE IF EXISTS Avilanca")
conexaoBD.manipular("CREATE DATABASE Avilanca")

#Criar as tabelas do banco de dados
conexaoBD.manipular('''
CREATE TABLE Avilanca.cliente(
id_cliente INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
nome_cliente VARCHAR(225) NOT NULL,
documento_cliente VARCHAR(225) NOT NULL,
data_nasc_cliente VARCHAR(225) NOT NULL,
nacionalidade_cliente VARCHAR(225) NOT NULL,
telefone_cliente VARCHAR(20) NOT NULL,
email_cliente VARCHAR(225) NOT NULL,
requesitos_esp_cliente VARCHAR(665) NOT NULL DEFAULT("N/A")
);
                ''')
conexaoBD.manipular('''
CREATE TABLE Avilanca.voo(
id_voo INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
id_aviao INT DEFAULT 0,
destino_inicial VARCHAR(225) NOT NULL,
destino_final VARCHAR(225) NOT NULL,
data_saida VARCHAR(255) NOT NULL,
data_chegada VARCHAR(225) NOT NULL,
preco decimal(10,2) not null
);
                ''')

conexaoBD.manipular('''
CREATE TABLE Avilanca.passagem(
id_passagem INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
id_cliente INT NOT NULL,
id_voo INT NOT NULL,
data_venda DATETIME DEFAULT CURRENT_TIMESTAMP,
forma_pagamento VARCHAR(225) NOT NULL,
n_do_assento VARCHAR(225) NOT NULL DEFAULT("N/A"),
CONSTRAINT fk_cliente FOREIGN KEY(id_cliente) REFERENCES Avilanca.cliente(id_cliente),
CONSTRAINT fk_voo FOREIGN KEY(id_voo) REFERENCES Avilanca.voo(id_voo));
                ''')

conexaoBD.manipular(''' INSERT INTO Avilanca.cliente (nome_cliente, documento_cliente, data_nasc_cliente, nacionalidade_cliente, telefone_cliente, email_cliente, requesitos_esp_cliente) VALUES
('João Silva', '123.456.789-00', '1985-05-15', 'Brasileiro', '11987654321', 'joao.silva@email.com', 'Nenhum'),
('Maria Oliveira', '987.654.321-00', '1990-07-22', 'Brasileira', '11987654322', 'maria.oliveira@email.com', 'Nenhum'),
('Carlos Pereira', '456.789.123-00', '1982-12-30', 'Brasileiro', '11987654323', 'carlos.pereira@email.com', 'Nenhum'),
('Deide Costa', '654.321.987-00', '1978-03-25', 'Brasileira', '11987654324', 'Deide.costa@email.com', 'Nenhum'),
('Pedro Santos', '321.987.654-00', '1995-08-14', 'Brasileiro', '11987654325', 'pedro.santos@email.com', 'Nenhum');
''')

conexaoBD.manipular('''
INSERT INTO Avilanca.voo (id_aviao, destino_inicial, destino_final, data_saida, data_chegada, preco) VALUES
(1, 'São Paulo', 'Rio de Janeiro', '2024-09-01', '2024-09-01', 200),
(2, 'Rio de Janeiro', 'Brasília', '2024-09-02', '2024-09-02', 250),
(3, 'Brasília', 'Salvador', '2024-09-03', '2024-09-03', 300),
(4, 'Salvador', 'Fortaleza', '2024-09-04', '2024-09-04', 210),
(5, 'Fortaleza', 'Recife', '2024-09-05', '2024-09-05', 145),
(6, 'Recife', 'São Paulo', '2024-09-06', '2024-09-06', 300),
(7, 'São Paulo', 'Curitiba', '2024-09-07', '2024-09-07', 220),
(8, 'Curitiba', 'Florianópolis', '2024-09-08', '2024-09-08', 153),
(9, 'Florianópolis', 'Porto Alegre', '2024-09-09', '2024-09-09', 152),
(10, 'Porto Alegre', 'São Paulo', '2024-09-10', '2024-09-10', 160);
''')