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
    
    #Criar banco hospitalvet
    cursor.execute("DROP DATABASE IF EXISTS hospitalvet;")
    cursor.execute("CREATE DATABASE hospitalvet;")
    cursor.execute("USE hospitalvet;")
    
    #Criar tabela paciente
    # id
    # nome
    # especie
    # tutor
    # peso
    
    sqlCreatePaciente = '''
    CREATE TABLE paciente(
      id_paciente INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
      nome_paciente VARCHAR(255) NOT NULL DEFAULT 'Não Identificado',
      especie_paciente VARCHAR(255) NOT NULL DEFAULT 'Indefinido',
      id_tutor INT NOT NULL DEFAULT 100,
      peso_paciente DECIMAL(5,2)  
    );
    '''
    cursor.execute("DROP TABLE IF EXISTS paciente;")
    cursor.execute(sqlCreatePaciente)
    
    #Inserir 30 pacientes gerados 
    
    cursor.execute('''
INSERT INTO paciente (nome_paciente, especie_paciente, id_tutor, peso_paciente) VALUES
('Rex', 'Cachorro', 101, 30.50),
('Luna', 'Gato', 102, 4.20),
('Bobby', 'Cachorro', 103, 25.00),
('Mimi', 'Gato', 104, 3.80),
('Thor', 'Cachorro', 105, 40.00),
('Lola', 'Coelho', 106, 2.50),
('Max', 'Cachorro', 107, 22.00),
('Mia', 'Gato', 108, 3.90),
('Jack', 'Cachorro', 109, 35.00),
('Sophie', 'Gato', 110, 4.10),
('Bella', 'Cachorro', 111, 28.00),
('Charlie', 'Gato', 112, 4.00),
('Buddy', 'Cachorro', 113, 30.00),
('Simba', 'Gato', 114, 3.50),
('Rocky', 'Cachorro', 115, 27.00),
('Nala', 'Gato', 116, 4.30),
('Toby', 'Cachorro', 117, 25.50),
('Chloe', 'Gato', 118, 3.70),
('Oscar', 'Cachorro', 119, 32.00),
('Lily', 'Gato', 120, 4.40),
('Duke', 'Cachorro', 121, 29.00),
('Tiger', 'Gato', 122, 3.60),
('Zeus', 'Cachorro', 123, 33.00),
('Ruby', 'Gato', 124, 4.50),
('Bentley', 'Cachorro', 125, 31.00),
('Lucy', 'Gato', 126, 3.80),
('Shadow', 'Cachorro', 127, 26.00),
('Jasper', 'Gato', 128, 4.20),
('Daisy', 'Coelho', 129, 2.60),
('Rusty', 'Cachorro', 130, 28.50);
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
        
    