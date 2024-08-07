import mysql.connector

host = "localhost"
user = "root"
password = "mysql"
database = "escola"

conexaoBD = None
cursor = None

try:
    conexaoBD = mysql.connector.connect(host=host, user=user, password = password, database=database)

    print("Conexão Estabelecida!")
    cursor = conexaoBD.cursor()
    
    cursor.execute("SELECT * FROM aluno")
    resultado = cursor.fetchall()
    
    
    #OPERAÇÕES SQL 
    
    #Visualizar os alunos do banco escola no padrão
    #<matricula>. <nome> - <cpf>
    
    for aluno in resultado:
        print(f"{aluno[0]}. {aluno[2]} - {aluno[1]}")
    
    #Peça ao usuário um número de matricula e exiba as informações completas do aluno escolhido
    matricula = int(input("Digite a matricula do aluno que deseja ver mais detalhes:"))
    
    alunoEscolhido = None
    
    for aluno in resultado:
        
        if aluno[0] == matricula:
            alunoEscolhido = aluno
            break
        
    if alunoEscolhido:
        print(f"{alunoEscolhido[2]}")
    else:
        print("Aluno não encontrado!")
    
    #Dica: cursor.execute(f"SELECT * FROM aluno WHERE matriculaaluno = {matricula}")
    
    cursor.execute(f"SELECT * FROM aluno WHERE matriculaaluno = {matricula}")
    
    resultado = cursor.fetchall()
    
    if resultado == []:
        print("Aluno não encontrado")
        
    else:
        print(resultado[0][2])
        
    #Peça ao usuário nome, cpf, e ano de nascimento e insira essas informações no banco de dados
    
    nome = input("Digite seu nome:")
    cpf = input("Digite seu cpf:")
    anoNascimento = input("Digite seu ano de nascimento:")
    
    cursor.execute('''
    INSERT INTO aluno
    VALUES (DEFAULT, %s, %s,DEFAULT, DEFAULT, %s, DEFAULT);               
                   ''', (cpf, nome, anoNascimento))
    conexaoBD.commit()
    
    # cursor.execute(sql)
    # conexaoBD.commit()
    
       
except mysql.connector.Error as e:
    print(e.msg)
finally:
    if cursor != None:
        cursor.close()
    if conexaoBD != None:
        conexaoBD.close()
        
        
# 
    


