import mysql.connector

host = "localhost"
user = "root"
password = "mysql"

con = None
cursor = None

try:
    con = mysql.connector.connect(host=host, user=user, password=password)
        
    cursor = con.cursor()
            
    cursor.execute("SELECT VERSION()")
    resultado = cursor.fetchall()
            
    print(resultado[0][0])
      
    cursor.execute("DROP DATABASE IF EXISTS telemarketing;")
    cursor.execute("CREATE DATABASE telemarketing;")
    cursor.execute("USE telemarketing;")
    
    SqlcreateCliente = '''
    CREATE TABLE cliente(
        id_cliente INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
        nome_cliente VARCHAR(255) NOT NULL DEFAULT 'Não Identificado',
       CPF_cliente CHAR(11) NOT NULL DEFAULT 'Indefinido',
       telefone_cliente CHAR(11) NOT NULL
        );
        '''
    
    SqlcreateAtendente= '''
    CREATE TABLE Atendente(
        id_atendente  INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
        nome_atendente VARCHAR(255) NOT NULL
        );
        '''
    cursor.execute("DROP TABLE IF EXISTS atendente;")
    cursor.execute(SqlcreateAtendente)


    SqlcreateAtendimento = '''
    Create TABLE Atendimento(
    id_atendimento INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    id_cliente INT NOT NULL,
    Id_atendente INT NOT NULL, 
    CONSTRAINT fk_atendente FOREIGN KEY(id_atendente) REFERENCES atendente(id_atendente),
    CONSTRAINT fk_cliente FOREIGN KEY(id_cliente) REFERENCES cliente(id_cliente)
    );
    '''
    

    cursor.execute("DROP TABLE IF EXISTS cliente;")
    cursor.execute(SqlcreateCliente)

    cursor.execute("DROP TABLE IF EXISTS atendimento;")
    cursor.execute(SqlcreateAtendimento)

    cursor.execute('''

    INSERT INTO cliente (nome_cliente, CPF_cliente, telefone_cliente) VALUES
('Ana Silva', '12345678901', '11987654321'),
('João Santos', '23456789012', '21987654321'),
('Maria Oliveira', '34567890123', '31987654321'),
('Carlos Souza', '45678901234', '41987654321'),
('Fernanda Lima', '56789012345', '51987654321'),
('Roberto Costa', '67890123456', '61987654321'),
('Patricia Almeida', '78901234567', '71987654321'),
('Rafael Ferreira', '89012345678', '81987654321'),
('Juliana Pereira', '90123456789', '91987654321'),
('Lucas Martins', '01234567890', '02987654321'
);
''')
    cursor.execute('''              
                
INSERT INTO Atendente (nome_atendente) VALUES
('Ana Souza'),
('Carlos Silva'),
('Fernanda Oliveira'),
('João Santos'),
('Maria Lima');                               
    ''')
    
    con.commit()

except mysql.connector.Error as e:
    print("Erro de SQL:",e)
except Exception as e:
    print("Erro de Python:",e)
finally:
    if cursor != None:
        cursor.close()
    if con != None and con.is_connected():
        con.close()



