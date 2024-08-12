import mysql.connector
#Programa para criar banco de dados hospitalvet, criar a tabela paciente e inserir 30 pacientes na tabela.

host = "localhost"
user = "root"
password = "mysql"

conexao = None
cursor = None
#Estabelecer conexão com o banco de dados
#Criar o cursor
#Executar comando SQL de criação do Banco de Dados hospitalvet
try:
    #Criação da conexão e execução das operações SQL
    conexao = mysql.connector.connect(host=host,user=user,password=password)
    cursor = conexao.cursor()
    
    
    
    cursor.execute("DROP DATABASE IF EXISTS hospitalvet")
    cursor.execute("CREATE DATABASE hospitalvet")
    cursor.execute("USE hospitalvet")
    
    #Criar tabela paciente
    #id
    #nome
    #id_tutor
    #especie
    #peso
    
    sqlCreateTable = '''
    CREATE TABLE paciente(
      id_paciente INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
      nome_paciente VARCHAR(255) NOT NULL DEFAULT 'Não Definido',
      id_tutor INT NOT NULL DEFAULT 100,
      especie_paciente VARCHAR(255) NOT NULL DEFAULT 'Não Definido',
      peso_paciente DECIMAL(5,2)
    );
    '''
    
    cursor.execute(sqlCreateTable)
    
    #Executar comando sql para inserir 30 pacientes na tabela
    
    cursor.execute('''
    INSERT INTO paciente (nome_paciente, id_tutor, especie_paciente, peso_paciente) VALUES
('Buddy', 101, 'Cachorro', 12.50),
('Max', 102, 'Gato', 4.30),
('Bella', 103, 'Cachorro', 9.80),
('Lucy', 104, 'Coelho', 1.20),
('Charlie', 105, 'Gato', 5.00),
('Daisy', 106, 'Cachorro', 7.40),
('Molly', 107, 'Cachorro', 8.90),
('Bailey', 108, 'Gato', 3.75),
('Lola', 109, 'Cachorro', 10.20),
('Sadie', 110, 'Coelho', 1.40),
('Maggie', 111, 'Gato', 4.80),
('Sophie', 112, 'Cachorro', 6.30),
('Chloe', 113, 'Gato', 4.10),
('Rocky', 114, 'Cachorro', 15.00),
('Roxy', 115, 'Coelho', 1.50),
('Gracie', 116, 'Gato', 3.90),
('Jack', 117, 'Cachorro', 11.70),
('Buster', 118, 'Gato', 4.50),
('Zoey', 119, 'Coelho', 1.30),
('Duke', 120, 'Cachorro', 9.50),
('Harley', 121, 'Gato', 3.60),
('Toby', 122, 'Cachorro', 14.20),
('Gizmo', 123, 'Coelho', 1.25),
('Coco', 124, 'Gato', 4.70),
('Penny', 125, 'Cachorro', 8.50),
('Lily', 126, 'Gato', 5.10),
('Oliver', 127, 'Coelho', 1.60),
('Bentley', 128, 'Cachorro', 12.00),
('Bandit', 129, 'Gato', 3.80),
('Milo', 130, 'Coelho', 1.45);                   
                   ''')
    conexao.commit()
    
    cursor.execute("SELECT VERSION()")
    resultado = cursor.fetchall()
    
    print(resultado[0][0])
    
      
except mysql.connector.Error as e:
    #Tratamento de erros e impressão de erros
    print("Erro SQL:", e)
except Exception as e:
    print("Erro Python:", e)
finally:
    #Finalizar as variáveis cursor e conexao
    if cursor != None:
        cursor.close()
    if conexao != None and conexao.is_connected():
        conexao.close()



