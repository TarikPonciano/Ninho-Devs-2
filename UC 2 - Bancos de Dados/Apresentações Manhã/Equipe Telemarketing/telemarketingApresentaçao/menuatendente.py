from Conexao15 import Conexao

conexaoBD = Conexao("localhost", "root", "mysql", "telemarketing")
def verAtendente():
    atendente = conexaoBD.consultar("SELECT * FROM atendente")
    print("ID | Nome ")
    for atendente in atendente:
        print(f"{atendente[0]} | {atendente[1]} ") 


while True:
    
    print('''   
    Menu:
    
    1. Ver atendente
    2. Cadastrar atendente
    3. Alterar dados do atendente
    4. Remover atendente
    0. Sair      
          ''')
    
    
    op = input("Digite a opção do menu desejada: ")
        
    if (op == "1"):
                            
            atendente = conexaoBD.consultar("Select * from atendente")
            
            print("ID | Nome ")
            
            for atendente in atendente:
                
                print(f"{atendente[0]} | {atendente[1]}  ")
            
            
            try:    
                idatendente = int(input("Digite o id do atendente escolhido:"))
            except Exception as e:
                print("Erro:",e)
                idatendente = 0
                
            if idatendente == 0:
                print("Encerrando Operação")
            else:
                atendenteEscolhido = conexaoBD.consultarComParametro("SELECT * FROM atendente WHERE id_atendente = %s", (idatendente,))
                
                if atendenteEscolhido == []:
                    print("atendente não encontrado!")
                else:
                    print(f'''
            ID: {atendenteEscolhido[0][0]}
            Nome: {atendenteEscolhido[0][1]}
        ''')
    elif (op == "2"):
            print("Cadastro de atendente")
            
            nome = input("Digite o nome:")
                    
            sql = '''
            INSERT INTO atendente VALUES (DEFAULT, %s);
            '''
        
            conexaoBD.manipularComParametro(sql, (nome,))
            
            print("atendente cadastrado com sucesso!")

    elif (op == "3"):
        
            verAtendente()
            try:
                idatendente = int(input("Digite o id do atendente que deseja alterar:"))
            except Exception as e:
                print("Erro:", e)
                idatendente = 0  
                
            if idatendente == 0:
                print("Operação Cancelada!")
            else:
                
                atendenteEscolhido = conexaoBD.consultarComParametro("SELECT * FROM atendente WHERE id_atendente = %s", (idatendente,))
                
                if atendenteEscolhido == []:
                    print("atendente não encontrado")
                else:
                    print(f'''
                ID: {atendenteEscolhido[0][0]}                  
                Nome: {atendenteEscolhido[0][1]}
                                
                        ''')
                    nome = atendenteEscolhido[0][1]              
                    
                    novoNome = input("Digite o novo nome:")
                    if (novoNome == ""):
                        novoNome = nome
                                
                
                    sql = '''
                    UPDATE atendente
                    SET
                    nome_atendente = %s;
                    '''
                    conexaoBD.manipularComParametro(sql, (novoNome, idatendente))
                    print("atendente atualizado com sucesso!")
        
    elif (op == "4"):
            
            
            atendente = conexaoBD.consultar("SELECT * FROM atendente")
            print("ID | Nome  ")
            for atendente in atendente:
                print(f"{atendente[0]} | {atendente[1]}  ")
            
            
            try:
                idatendente = int(input("Digite o id do atendente que deseja remover: "))
            except Exception as e:
                print("Erro:",e)
                idatendente   = 0
            
            if idatendente == 0:
                print("Operação Cancelada!")    
            
            else:        
                atendenteEscolhido = conexaoBD.consultarComParametro("SELECT * FROM atendente WHERE id_atendente = %s", (idatendente,))
                
                if (atendenteEscolhido == []):
                    print("atendente não encontrado!")
                else:
                    print(f'''
                ID: {atendenteEscolhido[0][0]}          
                Nome: {atendenteEscolhido[0][1]}          
            ''')
                
        
                confirmacao = input("Confirme se deseja remover o atendente (sim/não):")
            
                if (confirmacao == "sim"):
                    conexaoBD.manipularComParametro("DELETE FROM atendente WHERE id_atendente = %s",(idatendente,))
                    print("atendente removido com sucesso!")
                else:
                    print("Operação Cancelada")
            
            pass
    elif (op == "0"):
        break
    else:
            print("Você digitou uma opção inválida!")
        
    input("Tecle ENTER para continuar")



