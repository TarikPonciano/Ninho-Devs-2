from Conexao import Conexao

# Configurar credenciais de conexão do banco (Criar objeto Conexao)
conexaoBD = Conexao("localhost", "root", "mysql", "")

# Criar o banco de dados
conexaoBD.manipular("DROP DATABASE IF EXISTS SilvaStyle")
conexaoBD.manipular("CREATE DATABASE SilvaStyle")

# Criar as tabelas do banco de dados
conexaoBD.manipular('''
CREATE TABLE SilvaStyle.cliente (
    id_cliente INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    telefone CHAR(11) NOT NULL,
    cpf CHAR(11) NOT NULL
);
''')

conexaoBD.manipular('''
CREATE TABLE SilvaStyle.produtos (
    id_produto INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    estoque INT NOT NULL DEFAULT 0,
    preco DECIMAL(10, 2) NOT NULL
);
''')

conexaoBD.manipular('''
CREATE TABLE SilvaStyle.compras (
    id_compra INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    qntd INT NOT NULL DEFAULT 1,
    total DECIMAL(10, 2) NOT NULL,
    id_produto INT NOT NULL,
    id_cliente INT NOT NULL,
    CONSTRAINT fk_produto FOREIGN KEY(id_produto) REFERENCES SilvaStyle.produtos(id_produto),
    CONSTRAINT fk_cliente FOREIGN KEY(id_cliente) REFERENCES SilvaStyle.cliente(id_cliente)
);
''')

# Inserir dados de exemplo
conexaoBD.manipular('''
INSERT INTO SilvaStyle.cliente (nome, telefone, cpf) VALUES
('Ana Souza', '11987654321', '12345678900'),
('Bruno Lima', '11987654322', '23456789012'),
('Carla Mendes', '11987654323', '34567890123'),
('Daniela Silva', '11987654324', '45678901234'),
('Eduardo Costa', '11987654325', '56789012345');
''')

conexaoBD.manipular('''
INSERT INTO SilvaStyle.produtos (nome, estoque, preco) VALUES
('Óculos do Gojo', 50, 80.00),
('Kimono do Goku', 30, 130.00),
('Terno do Lúcifer', 20, 200.00),
('Jaqueta do dante', 15, 300.00),
('Chapéu de Palha do Luffy', 100, 40.00);
''')
