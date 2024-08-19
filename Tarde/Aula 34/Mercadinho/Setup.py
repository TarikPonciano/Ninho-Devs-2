from Conexao import Conexao

#Configurar credenciais de conexão do banco (Criar objeto Conexao)
conexaoBD = Conexao("localhost", "root", "mysql", "")

#Criar o banco de dados
conexaoBD.manipular("DROP DATABASE IF EXISTS mercadojoa")
conexaoBD.manipular("CREATE DATABASE mercadojoa")

#Criar as tabelas do banco de dados
conexaoBD.manipular('''
    CREATE TABLE mercadojoa.produtos(
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
    CREATE TABLE mercadojoa.vendas(
        id_venda INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
        data_venda DATETIME DEFAULT CURRENT_TIMESTAMP,
        valor_total_venda DECIMAL(10, 2) DEFAULT 0.00
    );
                    ''')
#Criar tabela itens
#   - Cadastrar as chaves estrangeiras
conexaoBD.manipular('''
    CREATE TABLE mercadojoa.itens(
        id_item INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
        id_produto INT NOT NULL,
        id_venda INT NOT NULL,
        quantidade_item INT NOT NULL DEFAULT 1,
        preco_unitario_item DECIMAL(6,2) DEFAULT 0.00,
        CONSTRAINT fk_produto FOREIGN KEY(id_produto) REFERENCES produtos(id_produto),
        CONSTRAINT fk_venda FOREIGN KEY (id_venda) REFERENCES vendas(id_venda));
                    ''')
#Inserir dados iniciais da tabela Produtos (10 produtos)

conexaoBD.manipular('''
INSERT INTO mercadojoa.produtos (nome_produto, preco_produto, estoque_produto) VALUES
('Arroz 5kg', 20.50, 30),
('Feijão 1kg', 8.90, 25),
('Açúcar 1kg', 5.75, 50),
('Leite 1L', 4.20, 40),
('Macarrão 500g', 3.60, 60),
('Óleo 900ml', 6.00, 15),
('Sabão em Pó 1kg', 9.80, 20),
('Café 250g', 12.30, 35),
('Bisnaga de Maionese 500g', 7.40, 12),
('Suco de Laranja 1L', 5.20, 45);    
''')