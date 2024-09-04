from Conexao import Conexao


conexaoBd = Conexao("localhost", "root", "mysql", "")

conexaoBd.manipular("DROP DATABASE IF EXISTS portaldeempregos;")
conexaoBd.manipular("CREATE DATABASE portaldeempregos;")

conexaoBd.manipular('''
CREATE TABLE portaldeempregos.empresa(
id_empresa INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
nome_empresa VARCHAR(255) NOT NULL,
cnpj_empresa CHAR(14) NOT NULL UNIQUE,
localizacao_empresa VARCHAR(255),
porte_empresa VARCHAR(45),
descricao_empresa VARCHAR(255)              
);
''')


conexaoBd.manipular('''
CREATE TABLE portaldeempregos.candidato(
id_candidato INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
nome_candidato VARCHAR(255) NOT NULL,
cpf_candidato CHAR(11) NOT NULL UNIQUE,
telefone_candidato VARCHAR(14) DEFAULT '00000000000',
endereco_candidato VARCHAR(255) DEFAULT 'SEM ENDEREÇO',
email_candidato VARCHAR(255) DEFAULT 'SEM E-MAIL'
);
''')



conexaoBd.manipular('''
CREATE TABLE portaldeempregos.vagas(
id_vaga INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
id_empresa INT NOT NULL,
nome_vaga VARCHAR(255) NOT NULL,
funcao_vaga VARCHAR(255),
salario_vaga DECIMAL(7,2),
CONSTRAINT fk_empresa FOREIGN KEY(id_empresa) REFERENCES empresa (id_empresa)
);
''')



conexaoBd.manipular('''
CREATE TABLE portaldeempregos.aplicacao(
id_aplicacao INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
id_candidato INT NOT NULL,
id_vaga INT NOT NULL,
data_aplicacao DATETIME DEFAULT CURRENT_TIMESTAMP,
status_aplicacao VARCHAR(255) default 'AGUARDANDO RESULTADO',
CONSTRAINT fk_vaga FOREIGN KEY (id_vaga) REFERENCES vagas(id_vaga),
CONSTRAINT fk_candidato FOREIGN KEY (id_candidato) REFERENCES candidato(id_candidato)
);
''')

conexaoBd.manipular('''
INSERT INTO portaldeempregos.empresa (nome_empresa, cnpj_empresa, localizacao_empresa, porte_empresa, descricao_empresa)
VALUES
('Tech Innovators', '11111111000101', 'São Paulo, SP', 'Grande', 'Líder em inovação tecnológica e soluções digitais.'),
('Health Solutions', '22222222000102', 'Curitiba, PR', 'Médio', 'Empresa especializada em tecnologia para a saúde.'),
('EducaTech', '33333333000103', 'Porto Alegre, RS', 'Pequeno', 'Startup focada em plataformas educacionais.'),
('EcoEnergy', '44444444000104', 'Belo Horizonte, MG', 'Grande', 'Soluções sustentáveis em energia renovável.'),
('FinancExpert', '55555555000105', 'Rio de Janeiro, RJ', 'Grande', 'Consultoria financeira com atuação global.');''')

conexaoBd.manipular('''
INSERT INTO portaldeempregos.vagas (id_empresa, nome_vaga, funcao_vaga, salario_vaga)
VALUES
(1, 'Engenheiro de Software', 'Desenvolvimento de software', 7000.00),
(1, 'Gerente de Projetos', 'Gestão de projetos de tecnologia', 9000.00),
(2, 'Analista de Suporte Técnico', 'Suporte técnico e atendimento ao cliente', 4000.00),
(3, 'Desenvolvedor Full Stack', 'Desenvolvimento de plataformas web', 6500.00),
(4, 'Engenheiro de Energia', 'Desenvolvimento de soluções em energia renovável', 8000.00),
(4, 'Consultor de Sustentabilidade', 'Consultoria em práticas sustentáveis', 7500.00),
(5, 'Analista Financeiro', 'Análise financeira e consultoria', 5000.00),
(5, 'Consultor de Investimentos', 'Consultoria em investimentos financeiros', 8500.00);
''')


conexaoBd.manipular('''
INSERT INTO portaldeempregos.candidato (nome_candidato, cpf_candidato, telefone_candidato, endereco_candidato, email_candidato)
VALUES
('Ana Pereira', '12345678901', '11987654321', 'Rua das Flores, 100, São Paulo, SP', 'ana.pereira@example.com'),
('Carlos Almeida', '23456789012', '21987654321', 'Av. Brasil, 2000, Rio de Janeiro, RJ', 'carlos.almeida@example.com'),
('Beatriz Santos', '34567890123', '31987654321', 'Rua das Palmeiras, 500, Belo Horizonte, MG', 'beatriz.santos@example.com'),
('Diego Costa', '45678901234', '41987654321', 'Av. Paraná, 1500, Curitiba, PR', 'diego.costa@example.com'),
('Fernanda Oliveira', '56789012345', '51987654321', 'Rua Bento Gonçalves, 700, Porto Alegre, RS', 'fernanda.oliveira@example.com');
''')



conexaoBd.manipular('''
INSERT INTO portaldeempregos.aplicacao (id_candidato, id_vaga)
VALUES
(1, 1),
(2, 2),
(3, 1),
(5, 5);
''')
