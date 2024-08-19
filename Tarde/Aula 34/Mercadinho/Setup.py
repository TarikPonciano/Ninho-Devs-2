from Conexao import Conexao

#Configurar credenciais de conexão do banco (Criar objeto Conexao)
conexaoBD = Conexao("localhost", "root", "mysql", "")

#Criar o banco de dados
conexaoBD.manipular("DROP DATABASE IF EXISTS mercadojoa")
conexaoBD.manipular("CREATE DATABASE mercadojoa")

#Criar as tabelas do banco de dados

conexaoBD.manipular('''
    CREATE TABLE produtos(
    id_produto INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    nome_produto VARCHAR(255) NOT NULL,
    preco_produto DECIMAL(6,2) NOT NULL DEFAULT 0.00,
    estoque_produto INT NOT NULL DEFAULT 0,
    CONSTRAINT chk_estoque CHECK(estoque_produto >= 0)
    );
                    ''')

#Criar tabela vendas
#   - No atributo data da venda, guardar o momento da venda (Data e hora)
#Criar tabela itens
#   - Cadastrar as chaves estrangeiras

#Inserir dados iniciais da tabela Produtos (10 produtos)