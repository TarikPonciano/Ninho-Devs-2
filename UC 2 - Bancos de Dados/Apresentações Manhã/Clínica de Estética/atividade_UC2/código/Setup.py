from Conexao import Conexao

conexaoBD = Conexao("localhost", "root", "mysql", "")

conexaoBD.manipular("DROP DATABASE IF EXISTS estetica;")
conexaoBD.manipular("CREATE DATABASE estetica;")

conexaoBD.manipular('''
CREATE TABLE estetica.clientes(
id_cliente INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
nome_cliente VARCHAR(255) NOT NULL,
nascimento_cliente DATE NOT NULL,
telefone_cliente CHAR(11) NOT NULL
);
''')

conexaoBD.manipular('''
CREATE TABLE estetica.servicos(
id_servico INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
nome_servico VARCHAR(255) NOT NULL,
preco_servico DECIMAL (6,2) NOT NULL DEFAULT 0.00
);                 
''')

conexaoBD.manipular('''
CREATE TABLE estetica.atendimento (
id_atendimento INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
id_cliente INT NOT NULL,
data_atendimento DATETIME DEFAULT CURRENT_TIMESTAMP,
valor_atendimento DECIMAL (10,2) NOT NULL DEFAULT 0.00,
CONSTRAINT fk_cliente FOREIGN KEY (id_cliente) REFERENCES clientes(id_cliente)
);
''')

conexaoBD.manipular('''
CREATE TABLE estetica.itens (
id_item INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
id_atendimento INT NOT NULL,
id_servico INT NOT NULL,
quantidade_item INT NOT NULL DEFAULT 1,
preco_unitario_item DECIMAL (6,2) NOT NULL DEFAULT 0.00,
CONSTRAINT fk_atendimento FOREIGN KEY (id_atendimento) REFERENCES atendimento(id_atendimento),
CONSTRAINT fk_servico FOREIGN KEY (id_servico) REFERENCES servicos(id_servico)
);
''')

conexaoBD.manipular('''
INSERT INTO estetica.clientes (nome_cliente, nascimento_cliente, telefone_cliente) VALUES
('Ana Silva', '1990-05-12', '85987654321'),
('Carlos Oliveira', '1985-07-23', '85976543210'),
('Maria Santos', '1992-02-15', '85987654322'),
('João Pereira', '1980-11-30', '85976543211'),
('Fernanda Lima', '1988-03-07', '85987654323'),
('Roberto Costa', '1995-06-18', '85976543212'),
('Patrícia Martins', '1982-12-22', '85987654324'),
('Eduardo Rocha', '1991-09-29', '85976543213'),
('Juliana Alves', '1986-04-04', '85987654325'),
('Ricardo Mendes', '1993-08-14', '85976543214');
''')

conexaoBD.manipular('''
INSERT INTO estetica.servicos (nome_servico, preco_servico) VALUES
('Limpeza de Pele', 120.00),
('Tratamento Facial', 150.00),
('Massagem Relaxante', 100.00),
('Depilação Total', 80.00),
('Hidratação Capilar', 90.00),
('Manicure e Pedicure', 60.00),
('Esfoliação Corporal', 110.00),
('Tratamento Anticelulite', 140.00),
('Maquiagem Completa', 200.00),
('Penteado e Escova', 70.00);
''')