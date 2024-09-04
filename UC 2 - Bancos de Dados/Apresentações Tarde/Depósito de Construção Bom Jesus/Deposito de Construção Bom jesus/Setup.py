from conexao import Conexao

#Configurar credenciais de conexão do banco (Criar objeto Conexao)
conexaoBD = Conexao("localhost", "root", "mysql", "")

#Criar o banco de dados
conexaoBD.manipular("DROP DATABASE IF EXISTS depositobomjesus")
conexaoBD.manipular("CREATE DATABASE depositobomjesus")

#Criar a tabela clientes 
conexaoBD.manipular('''
    CREATE TABLE depositobomjesus.cliente(
    id_cliente INT NOT NULL AUTO_INCREMENT PRIMARY KEY,                
    nome_cliente VARCHAR(255) NOT NULL,
    cpf_cliente CHAR(11) NOT NULL UNIQUE,
    telefone_cliente CHAR(15) NOT NULL);
                        ''')

#Criar as tabelas do banco de dados
conexaoBD.manipular('''
    CREATE TABLE depositobomjesus.produtos(
    id_produto INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    nome_produto VARCHAR(255) NOT NULL,
    preco_produto DECIMAL(6,2) NOT NULL DEFAULT 0.00,
    estoque_produto INT NOT NULL DEFAULT 0,
    CONSTRAINT chk_estoque CHECK(estoque_produto >= 0)
    );
                    ''')

#Criar tabela vendas
#   - No atributo data da venda, guardar o momento da venda (Data e hora)
conexaoBD.manipular('''
    CREATE TABLE depositobomjesus.vendas(
        id_venda INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
        data_venda DATETIME DEFAULT CURRENT_TIMESTAMP,
        valor_total_venda DECIMAL(10, 2) DEFAULT 0.00
    );
                    ''')

#Inserir dados iniciais da tabela Produtos

conexaoBD.manipular('''
INSERT INTO depositobomjesus.produtos (nome_produto, preco_produto, estoque_produto) VALUES
('Cimento Portland', 25.00, 100),
('Tijolo de Vidro', 3.00, 300),
('Tinta Látex Branca', 150.00, 80),
('Tinta Acrílica Colorida', 180.00, 70),
('Argamassa', 35.00, 150),
('Massa Corrida', 40.00, 100),
('Gesso Acartonado', 25.00, 200),
('Parafuso de Aço 3.5x25mm', 10.00, 500),
('Pregos de Aço 50mm', 15.00, 400),
('Ferramenta Multifunção', 250.00, 25),
('Serra Circular', 350.00, 15),
('Martelete Pneumático', 600.00, 10),
('Interruptor Simples', 8.00, 300),
('Tomada Tripla', 12.00, 250),
('Luminária LED', 60.00, 120),
("Caixa d'Água 1000L", 500.00, 30),
('Tubo PVC 50mm', 10.00, 150),
('Capa de Chuva para Obra', 25.00, 100),
('Escada de Alumínio 3 degraus', 150.00, 20),
('Curva de 25mm',7.00, 70);''')

conexaoBD.manipular('''  
INSERT INTO depositobomjesus.cliente (nome_cliente , cpf_cliente , telefone_cliente) VALUES
('Ana Silva', '12345678901', '(85) 98765-4321'),
('Bruno Santos', '23456789012', '(85) 97654-3210'),
('Carlos Oliveira', '34567890123', '(85) 96543-2109'),
('Daniela Costa', '45678901234', '(85) 95432-1098'),
('Eduardo Almeida', '56789012345', '(85) 94321-0987'),
('Fernanda Lima', '67890123456', '(85) 93210-9876'),
('Gabriel Souza', '78901234567', '(85) 92109-8765'),
('Helena Martins', '89012345678', '(85) 91098-7654'),
('Igor Pereira', '90123456789', '(85) 90987-6543'),
('Juliana Ferreira', '01234567890', '(85) 90876-5432');
''')


