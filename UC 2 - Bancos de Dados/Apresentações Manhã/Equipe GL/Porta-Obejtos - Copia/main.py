import mysql.connector
from mysql.connector import Error
from datetime import datetime

def criar_conexao():
    """Estabelece uma conexão com o banco de dados."""
    try:
        conexao = mysql.connector.connect(
            host='localhost',
            user='root',
            password='mysql',
            database='portaobjetos'
        )
        if conexao.is_connected():
            print("Conexão estabelecida")
            return conexao
    except Error as e:
        print(f"Erro: {e}")
        return None

def adicionar_pessoa(conexao, nome, email):
    """Adiciona uma nova pessoa ao banco de dados e cria uma reserva padrão se possível."""
    try:
        cursor = conexao.cursor()
        cursor.execute("INSERT INTO Pessoa (nome, email) VALUES (%s, %s)", (nome, email))
        conexao.commit()
        pessoa_id = cursor.lastrowid
        print("Pessoa adicionada com sucesso.")
        
        # Tenta criar uma reserva padrão para a nova pessoa
        objeto_id = obter_objeto_id_padrao(conexao)
        if objeto_id:
            fazer_reserva(conexao, pessoa_id, objeto_id)
        else:
            print("Não há objetos disponíveis para reserva.")
        
    except Error as e:
        print(f"Erro: {e}")

def adicionar_objeto(conexao, descricao, categoria):
    """Adiciona um novo objeto ao banco de dados e tenta criar uma reserva padrão se possível."""
    try:
        cursor = conexao.cursor()
        cursor.execute("INSERT INTO Objeto (descricao, categoria) VALUES (%s, %s)", (descricao, categoria))
        conexao.commit()
        objeto_id = cursor.lastrowid
        print("Objeto adicionado com sucesso.")
        
        # Tenta criar uma reserva padrão para o novo objeto
        pessoa_id = obter_pessoa_id_padrao(conexao)
        if pessoa_id:
            fazer_reserva(conexao, pessoa_id, objeto_id)
        else:
            print("Não há pessoas disponíveis para reserva.")
        
    except Error as e:
        print(f"Erro: {e}")

def obter_pessoa_id_padrao(conexao):
    """Obtém o ID da primeira pessoa disponível."""
    try:
        cursor = conexao.cursor()
        cursor.execute("SELECT pessoa_id FROM Pessoa LIMIT 1")
        pessoa = cursor.fetchone()
        return pessoa[0] if pessoa else None
    except Error as e:
        print(f"Erro: {e}")
        return None

def obter_objeto_id_padrao(conexao):
    """Obtém o ID do primeiro objeto disponível."""
    try:
        cursor = conexao.cursor()
        cursor.execute("SELECT objeto_id FROM Objeto LIMIT 1")
        objeto = cursor.fetchone()
        return objeto[0] if objeto else None
    except Error as e:
        print(f"Erro: {e}")
        return None

def atualizar_pessoa(conexao, pessoa_id, nome, email):
    """Atualiza as informações de uma pessoa."""
    try:
        cursor = conexao.cursor()
        cursor.execute("UPDATE Pessoa SET nome = %s, email = %s WHERE pessoa_id = %s", (nome, email, pessoa_id))
        conexao.commit()
        print("Pessoa atualizada com sucesso.")
    except Error as e:
        print(f"Erro: {e}")

def atualizar_objeto(conexao, objeto_id, descricao, categoria):
    """Atualiza as informações de um objeto."""
    try:
        cursor = conexao.cursor()
        cursor.execute("UPDATE Objeto SET descricao = %s, categoria = %s WHERE objeto_id = %s", (descricao, categoria, objeto_id))
        conexao.commit()
        print("Objeto atualizado com sucesso.")
    except Error as e:
        print(f"Erro: {e}")

def resetar_banco(conexao):
    """Reseta o banco de dados, excluindo todas as tabelas e recriando-as."""
    try:
        cursor = conexao.cursor()
        cursor.execute("DROP DATABASE IF EXISTS portaobjetos")
        cursor.execute("CREATE DATABASE portaobjetos")
        cursor.execute("USE portaobjetos")
        
        cursor.execute("""
        CREATE TABLE Pessoa (
            pessoa_id INT AUTO_INCREMENT PRIMARY KEY,
            nome VARCHAR(255),
            email VARCHAR(255)
        )
        """)
        
        cursor.execute("""
        CREATE TABLE Objeto (
            objeto_id INT AUTO_INCREMENT PRIMARY KEY,
            descricao VARCHAR(255),
            categoria VARCHAR(255)
        )
        """)
        
        cursor.execute("""
        CREATE TABLE Reserva (
            reserva_id INT AUTO_INCREMENT PRIMARY KEY,
            pessoa_id INT,
            objeto_id INT,
            data_reserva DATETIME,
            FOREIGN KEY (pessoa_id) REFERENCES Pessoa(pessoa_id) ON DELETE CASCADE,
            FOREIGN KEY (objeto_id) REFERENCES Objeto(objeto_id)
        )
        """)
        
        print("Banco de dados resetado com sucesso.")
    except Error as e:
        print(f"Erro: {e}")

def visualizar_pessoas(conexao):
    """Visualiza todas as pessoas e suas informações, incluindo reservas."""
    try:
        cursor = conexao.cursor(dictionary=True)
        
        # Obtém informações das pessoas e suas reservas
        cursor.execute("""
        SELECT p.pessoa_id, p.nome, p.email, r.reserva_id, o.descricao AS objeto_descricao, o.categoria, r.data_reserva
        FROM Pessoa p
        LEFT JOIN Reserva r ON p.pessoa_id = r.pessoa_id
        LEFT JOIN Objeto o ON r.objeto_id = o.objeto_id
        """)
        pessoas = cursor.fetchall()
        
        if pessoas:
            pessoas_exibidas = set()  # Para evitar a duplicação de pessoas
            print("\nPessoas e suas informações:")
            for pessoa in pessoas:
                if pessoa['pessoa_id'] not in pessoas_exibidas:
                    print(f"\nID: {pessoa['pessoa_id']}")
                    print(f"Nome: {pessoa['nome']}")
                    print(f"Email: {pessoa['email']}")
                    pessoas_exibidas.add(pessoa['pessoa_id'])
                
                if pessoa['reserva_id']:
                    print(f"  Reserva ID: {pessoa['reserva_id']}")
                    print(f"  Descrição do Objeto: {pessoa['objeto_descricao']}")
                    print(f"  Categoria: {pessoa['categoria']}")
                    print(f"  Data da Reserva: {pessoa['data_reserva']}")
                    print("-" * 40)
                    
        else:
            print("Nenhuma pessoa encontrada.")
    except Error as e:
        print(f"Erro: {e}")

def visualizar_pessoa_por_id(conexao, pessoa_id):
    """Visualiza uma pessoa pelo ID, incluindo suas reservas."""
    try:
        cursor = conexao.cursor(dictionary=True)
        
        # Obtém informações da pessoa
        cursor.execute("SELECT * FROM Pessoa WHERE pessoa_id = %s", (pessoa_id,))
        pessoa = cursor.fetchone()
        
        if pessoa:
            print(f"\nInformações da Pessoa (ID {pessoa['pessoa_id']}):")
            print(f"Nome: {pessoa['nome']}")
            print(f"Email: {pessoa['email']}")
            
            # Obtém reservas da pessoa
            cursor.execute("""
            SELECT r.reserva_id, o.descricao, o.categoria, r.data_reserva
            FROM Reserva r
            JOIN Objeto o ON r.objeto_id = o.objeto_id
            WHERE r.pessoa_id = %s
            """, (pessoa_id,))
            reservas = cursor.fetchall()
            
            if reservas:
                print("\nReservas:")
                for reserva in reservas:
                    print(f"Reserva ID: {reserva['reserva_id']}")
                    print(f"Descrição do Objeto: {reserva['descricao']}")
                    print(f"Categoria: {reserva['categoria']}")
                    print(f"Data da Reserva: {reserva['data_reserva']}")
                    print("-" * 40)
            else:
                print("Nenhuma reserva encontrada.")
        else:
            print("Pessoa não encontrada.")
    except Error as e:
        print(f"Erro: {e}")

def remover_pessoa(conexao, pessoa_id):
    """Remove uma pessoa pelo ID."""
    try:
        cursor = conexao.cursor()
        cursor.execute("DELETE FROM Pessoa WHERE pessoa_id = %s", (pessoa_id,))
        conexao.commit()
        
        if cursor.rowcount > 0:
            print("Pessoa removida com sucesso.")
        else:
            print("Pessoa não encontrada.")
    except Error as e:
        print(f"Erro: {e}")

def remover_objeto(conexao, objeto_id):
    """Remove um objeto pelo ID."""
    try:
        cursor = conexao.cursor()
        cursor.execute("DELETE FROM reserva WHERE objeto_id = %s", (objeto_id,))
        conexao.commit()
        cursor = conexao.cursor()
        cursor.execute("DELETE FROM Objeto WHERE objeto_id = %s", (objeto_id,))
        conexao.commit()
        
        if cursor.rowcount > 0:
            print("Objeto removido com sucesso.")
        else:
            print("Objeto não encontrado.")
    except Error as e:
        print(f"Erro: {e}")

def fazer_reserva(conexao, pessoa_id, objeto_id):
    """Faz uma nova reserva se a pessoa e o objeto existirem."""
    try:
        cursor = conexao.cursor()
        
        # Verifica se a pessoa e o objeto existem
        cursor.execute("SELECT COUNT(*) FROM Pessoa WHERE pessoa_id = %s", (pessoa_id,))
        pessoa_existe = cursor.fetchone()[0]
        
        cursor.execute("SELECT COUNT(*) FROM Objeto WHERE objeto_id = %s", (objeto_id,))
        objeto_existe = cursor.fetchone()[0]
        
        if pessoa_existe and objeto_existe:
            data_reserva = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            cursor.execute("INSERT INTO Reserva (pessoa_id, objeto_id, data_reserva) VALUES (%s, %s, %s)", (pessoa_id, objeto_id, data_reserva))
            conexao.commit()
            print("Reserva realizada com sucesso.")
        else:
            print("Pessoa ou objeto não encontrados.")
    except Error as e:
        print(f"Erro: {e}")

def main():
    conexao = criar_conexao()
    if conexao:
        while True:
            print("\nMenu:")
            print("1. Adicionar Pessoa")
            print("2. Adicionar Objeto")
            print("3. Atualizar Pessoa")
            print("4. Atualizar Objeto")
            print("5. Resetar Banco de Dados")
            print("6. Visualizar Pessoas")
            print("7. Remover Pessoa pelo ID")
            print("8. Remover Objeto pelo ID")
            print("9. Sair")

            escolha = input("Digite sua escolha: ")

            if escolha == '1':
                nome = input("Digite o nome da pessoa: ")
                email = input("Digite o email da pessoa: ")
                adicionar_pessoa(conexao, nome, email)
            elif escolha == '2':
                descricao = input("Digite a descrição do objeto: ")
                categoria = input("Digite a categoria do objeto: ")
                adicionar_objeto(conexao, descricao, categoria)
            elif escolha == '3':
                pessoa_id = int(input("Digite o ID da pessoa: "))
                nome = input("Digite o novo nome: ")
                email = input("Digite o novo email: ")
                atualizar_pessoa(conexao, pessoa_id, nome, email)
            elif escolha == '4':
                objeto_id = int(input("Digite o ID do objeto: "))
                descricao = input("Digite a nova descrição: ")
                categoria = input("Digite a nova categoria: ")
                atualizar_objeto(conexao, objeto_id, descricao, categoria)
            elif escolha == '5':
                resetar_banco(conexao)
            elif escolha == '6':
                visualizar_pessoas(conexao)
            elif escolha == '7':
                pessoa_id = int(input("Digite o ID da pessoa para remover: "))
                remover_pessoa(conexao, pessoa_id)
            elif escolha == '8':
                objeto_id = int(input("Digite o ID do objeto para remover: "))
                remover_objeto(conexao, objeto_id)
            elif escolha == '9':
                conexao.close()
                break
            else:
                print("Escolha inválida. Tente novamente.")
            input("Tecle Enter para continuar")
if __name__ == "__main__":
    main()
