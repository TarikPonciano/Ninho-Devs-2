from Conexao import Conexao

conexaoBD = Conexao("localhost", "root", "mysql", "")

#Criar um BD para o mercado do seu joaquim
conexaoBD.manipular("DROP DATABASE IF EXISTS jomart;")
conexaoBD.manipular("CREATE DATABASE jomart;")

#Criar as tabelas Vendas, Itens, Produtos
conexaoBD.manipular('''
CREATE TABLE jomart.produtos(
id_produto INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
nome_produto VARCHAR(255) NOT NULL,
preco_produto DECIMAL(6,2) NOT NULL DEFAULT 0.00,
estoque_produto INT NOT NULL DEFAULT 0 ,
CONSTRAINT chk_estoque CHECK(estoque_produto>=0)
);
''')

conexaoBD.manipular('''
CREATE TABLE jomart.vendas(
id_venda INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
data_venda DATETIME DEFAULT CURRENT_TIMESTAMP,
valor_venda DECIMAL(10,2) NOT NULL DEFAULT 0.00
);                 
''')

conexaoBD.manipular('''
CREATE TABLE jomart.itens(
id_item INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
id_produto INT NOT NULL,
id_venda INT NOT NULL,
quantidade_item INT NOT NULL DEFAULT 1,
preco_unitario_item DECIMAL (6,2) NOT NULL DEFAULT 0.00,
CONSTRAINT fk_produto FOREIGN KEY(id_produto) REFERENCES produtos(id_produto),
CONSTRAINT fk_venda FOREIGN KEY(id_venda) REFERENCES vendas(id_venda));''')

#Preencher a tabela produtos com 10 produtos ficcionais

conexaoBD.manipular('''
INSERT INTO jomart.produtos (nome_produto, preco_produto, estoque_produto) VALUES
('Arroz Tipo 1kg', 5.99, 50),
('Feijão Preto 1kg', 7.49, 30),
('Açúcar Cristal 1kg', 4.99, 20),
('Óleo de Soja 900ml', 6.29, 25),
('Macarrão Espaguete 500g', 3.79, 15),
('Leite Integral 1L', 3.49, 40),
('Café Torrado e Moído 250g', 8.99, 10),
('Sal Refinado 1kg', 2.49, 60),
('Sabão em Pó 1kg', 5.29, 35),
('Detergente Líquido 500ml', 2.99, 45);
''')