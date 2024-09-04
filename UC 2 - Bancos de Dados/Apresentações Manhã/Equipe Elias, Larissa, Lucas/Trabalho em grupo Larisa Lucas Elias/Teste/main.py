import conexao

def menu():
    print("1. Gerenciar Usuários")
    print("2. Gerenciar Livros")
    print("3. Gerenciar Empréstimos")
    print("4. Sair")
    return input("Escolha uma opção: ")

def gerenciar_usuarios():
    connection = conexao.conectar()
    if connection:
        cursor = connection.cursor()
        escolha = input("1. Ver\n2. Inserir\n3. Atualizar\n4. Remover\nEscolha uma opção: ")
       
        if escolha == '1':
            print("ID |  Nome usuário | Email |")
            cursor.execute("SELECT * FROM Usuario")
            for row in cursor.fetchall():
                print(f"{row[0]} | {row[1]} | {row[2]}")
            
        elif escolha == '2':
            nome = input("Nome do Usuário: ")
            email = input("Email do Usuário: ")
            cursor.execute("INSERT INTO Usuario (Nome, Email) VALUES (%s, %s)", (nome, email))
        
        elif escolha == '3':
            id_usuario = int(input("ID do Usuário a ser atualizado: "))
            novo_nome = input("Novo Nome: ")
            novo_email = input("Novo Email: ")
            cursor.execute("UPDATE Usuario SET Nome = %s, Email = %s WHERE ID_Usuario = %s", (novo_nome, novo_email, id_usuario))
        
        elif escolha == '4':
            id_usuario = int(input("ID do Usuário a ser removido: "))
            cursor.execute("DELETE FROM Usuario WHERE ID_Usuario = %s", (id_usuario,))
        
        connection.commit()
        cursor.close()
        connection.close()

def gerenciar_livros():
    connection = conexao.conectar()
    if connection:
        cursor = connection.cursor()
        escolha = input("1. Ver\n2. Inserir\n3. Atualizar\n4. Remover\nEscolha uma opção: ")
        
        if escolha == '1':
            cursor.execute("SELECT * FROM Livro")
            for row in cursor.fetchall():
                print(row)
        
        elif escolha == '2':
            titulo = input("Título do Livro: ")
            autor = input("Autor do Livro: ")
            ano_publicacao = int(input("Ano de Publicação: "))
            cursor.execute("INSERT INTO Livro (Titulo, Autor, Ano_Publicacao) VALUES (%s, %s, %s)", (titulo, autor, ano_publicacao))
        
        elif escolha == '3':
            id_livro = int(input("ID do Livro a ser atualizado: "))
            novo_titulo = input("Novo Título: ")
            novo_autor = input("Novo Autor: ")
            novo_ano_publicacao = int(input("Novo Ano de Publicação: "))
            cursor.execute("UPDATE Livro SET Titulo = %s, Autor = %s, Ano_Publicacao = %s WHERE ID_Livro = %s", (novo_titulo, novo_autor, novo_ano_publicacao, id_livro))
        
        elif escolha == '4':
            id_livro = int(input("ID do Livro a ser removido: "))
            cursor.execute("DELETE FROM Livro WHERE ID_Livro = %s", (id_livro,))
        
        connection.commit()
        cursor.close()
        connection.close()

def gerenciar_emprestimos():
    connection = conexao.conectar()
    if connection:
        cursor = connection.cursor()
        escolha = input("1. Ver\n2. Inserir\n3. Remover\nEscolha uma opção: ")
        
        if escolha == '1':
            cursor.execute('''
                SELECT e.ID_Emprestimo, e.Data_Emprestimo, e.Data_Devolucao, u.Nome, l.Titulo 
                FROM Emprestimo e
                JOIN Usuario u ON e.ID_Usuario = u.ID_Usuario
                JOIN Livro l ON e.ID_Livro = l.ID_Livro
            ''')
            for row in cursor.fetchall():
                print(row)
        
        elif escolha == '2':
            data_emprestimo = input("Data do Empréstimo (YYYY-MM-DD): ")
            data_devolucao = input("Data de Devolução (YYYY-MM-DD, deixe em branco se ainda não devolvido): ")
            id_usuario = int(input("ID do Usuário: "))
            id_livro = int(input("ID do Livro: "))
            cursor.execute("INSERT INTO Emprestimo (Data_Emprestimo, Data_Devolucao, ID_Usuario, ID_Livro) VALUES (%s, %s, %s, %s)", (data_emprestimo, data_devolucao, id_usuario, id_livro))
        
        elif escolha == '3':
            id_emprestimo = int(input("ID do Empréstimo a ser removido: "))
            cursor.execute("DELETE FROM Emprestimo WHERE ID_Emprestimo = %s", (id_emprestimo,))
        
        connection.commit()
        cursor.close()
        connection.close()

def main():
    while True:
        opcao = menu()
        if opcao == '1':
            gerenciar_usuarios()
        elif opcao == '2':
            gerenciar_livros()
        elif opcao == '3':
            gerenciar_emprestimos()
        elif opcao == '4':
            break

if __name__ == "__main__":
    main()
