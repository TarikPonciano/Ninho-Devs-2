from Conexao15 import Conexao
conexaoBD = Conexao("localhost", "root", "mysql", "telemarketing")
def verAtendimento():
    atendimento = conexaoBD.consultar("SELECT * FROM atendimento")
    print("ID")
    for atendimento in atendimento:
        print(f"{atendimento[0]} ")


while True:
    
    print('''
        
    Menu:
    
    1. Ver atendimento
    2. Cadastrar atendimento
    3. Remover atendimento
    0. Sair      
          ''')
    
    op = input("Digite a opção do menu desejada: ")
    
    if (op == "1"):
                        
        atendimento = conexaoBD.consultar("Select * from atendimento")
        
        print("IDatendente | IDcliente ")
        
        for atendimento in atendimento:
            
            print(f"{atendimento[0]} | {atendimento[1]}  ")
        
        
        try:    
            idatendimento = int(input("Digite o id do atendimento escolhido:"))
        except Exception as e:
            print("Erro:",e)
            idatendimento = 0
            
        if idatendimento == 0:
            print("Encerrando Operação")
        else:
            atendimentoEscolhido = conexaoBD.consultarComParametro("SELECT * FROM atendimento WHERE id_atendimento = %s", (idatendimento,))
            
            if atendimentoEscolhido == []:
                print("atendimento não encontrado!")
            else:
                print(f'''
        ID: {atendimentoEscolhido[0][0]}
        IDcliente: {atendimentoEscolhido[0][1]}
        
       ''')
                
    elif (op == "2"):
        print("Cadastro de atendimento")
        
        IDcliente = input("Digite o IDcliente:")
        IDatendente = input("Digite o IDatendente:")
        sql = '''
        INSERT INTO atendimento VALUES (DEFAULT, %s, %s);
        '''
    
        conexaoBD.manipularComParametro(sql, (IDcliente, 1))
        
        print("atendimento cadastrado com sucesso!")

    elif (op == "3"):
        
        atendimento = conexaoBD.consultar("SELECT * FROM atendimento")
        print("IDatendente | IDcliente ")
        for atendimento in atendimento:
            print(f"{atendimento[0]} | {atendimento[1]}  ")
        
        
        try:
         idatendimento = int(input("Digite o id do atendimento que deseja remover: "))
        except Exception as e:
            print("Erro:",e)
            idatendimento   = 0
        
        if idatendimento == 0:
            print("Operação Cancelada!")    
       
        else:        
            atendimentoEscolhido = conexaoBD.consultarComParametro("SELECT * FROM atendimento WHERE id_atendimento = %s", (idatendimento,))
            
            if (atendimentoEscolhido == []):
                print("atendimento não encontrado!")
            else:
                print(f'''
            ID: {atendimentoEscolhido[0][0]}          
            IDcliente: {atendimentoEscolhido[0][1]}          
            ''')
            
    
            confirmacao = input("Confirme se deseja remover o atendimento (sim/não):")
        
        
            if (confirmacao == "sim"):
                conexaoBD.manipularComParametro("DELETE FROM atendimento WHERE id_atendimento = %s",(idatendimento,))
                print("atendimento removido com sucesso!")
            else:
                print("Operação Cancelada")
            pass
    elif (op == "0"):
        break
    else:
        print("Você digitou uma opção inválida!")
    
        input("Tecle ENTER para continuar")