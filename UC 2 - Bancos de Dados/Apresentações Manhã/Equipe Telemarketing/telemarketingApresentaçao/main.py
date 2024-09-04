from Conexao15 import Conexao

conexaoBD = Conexao("localhost", "root", "mysql", "telemarketing")#Colocar credenciais
def verCliente():
    cliente = conexaoBD.consultar("SELECT * FROM cliente")
    print("ID | Nome | CPF | Telefone")
    for cliente in cliente:
        print(f"{cliente[0]} | {cliente[1]} | {cliente[2]} | {cliente[3]}") 


while True:
    
    print('''
    Bem vindo a Contax
    
    Menu:
    
    1. Ver cliente
    2. Cadastrar cliente
    3. Alterar dados do cliente
    4. Remover cliente
    0. Sair      
          ''')
    
    op = input("Digite a opção do menu desejada: ")
    
    if (op == "1"):
                        
        cliente = conexaoBD.consultar("Select * from cliente")
        
        print("ID | Nome | CPF | Telefone ")
        
        for cliente in cliente:
            
            print(f"{cliente[0]} | {cliente[1]} | {cliente[2]} | {cliente[3]} ")
        
        
        try:    
            idcliente = int(input("Digite o id do cliente escolhido:"))
        except Exception as e:
            print("Erro:",e)
            idcliente = 0
            
        if idcliente == 0:
            print("Encerrando Operação")
        else:
            clienteEscolhido = conexaoBD.consultarComParametro("SELECT * FROM cliente WHERE id_cliente = %s", (idcliente,))
            
            if clienteEscolhido == []:
                print("cliente não encontrado!")
            else:
                print(f'''
        ID: {clienteEscolhido[0][0]}
        Nome: {clienteEscolhido[0][1]}
        CPF: {clienteEscolhido[0][2]}
        Telefone: {clienteEscolhido[0][3]}
       ''')

    elif (op == "2"):
        print("Cadastro de cliente")
        
        nome = input("Digite o nome:")
        CPF = int(input("Digite a CPF:"))
        telefone = int(input("Digite o telefone:"))
                
        sql = '''
        INSERT INTO cliente VALUES (DEFAULT, %s, %s, %s);
        '''
    
        conexaoBD.manipularComParametro(sql, (nome, CPF, telefone))
        
        print("cliente cadastrado com sucesso!")

    elif (op == "3"):
        #Exibir a lista de cliente na tela
        verCliente()
        #Pedir o id de um cliente específico para o usuário
        try:
         idcliente = int(input("Digite o id do cliente que deseja alterar:"))
        except Exception as e:
            print("Erro:", e)
            idcliente = 0  
            
        if idcliente == 0:
            print("Operação Cancelada!")
        else:
            #Exibir as informações do cliente na tela
            clienteEscolhido = conexaoBD.consultarComParametro("SELECT * FROM cliente WHERE id_cliente = %s", (idcliente,))
            
            if clienteEscolhido == []:
                print("cliente não encontrado")
            else:
                print(f'''
            ID: {clienteEscolhido[0][0]}                  
            Nome: {clienteEscolhido[0][1]}
            CPF: {clienteEscolhido[0][2]}
            Telefone: {clienteEscolhido[0][3]}                  
                      ''')
                nome = clienteEscolhido[0][1]
                CPF = clienteEscolhido[0][2]
                telefone = clienteEscolhido[0][3]
                
                #Pedir as novas informações do cliente (nome, CPF, telefone)
                novoNome = input("Digite o novo nome:")
                if (novoNome == ""):
                    novoNome = nome
                novoCPF = int(input("Digite  novo CPF:"))
                if (novoCPF == ""):
                    novoCPF = CPF
                novoTelefone = int(input("Digite o novo telefone:"))
                if (novoTelefone == 0):
                    novoTelefone = telefone
                
                #Enviar as novas informações através de manipulação UPDATE
                sql = '''
                UPDATE cliente
                SET
                nome_cliente = %s,
                CPF_cliente = %s,
                telefone_cliente = %s,
                WHERE
                id_cliente = %s;
                '''
                conexaoBD.manipularComParametro(sql, (novoNome, novoCPF, novoTelefone, idcliente))
                print("cliente atualizado com sucesso!")
    
    elif (op == "4"):
        
        # Exibir a lista de cliente na tela
        cliente = conexaoBD.consultar("SELECT * FROM cliente")
        print("ID | Nome | CPF  telefone ")
        for cliente in cliente:
            print(f"{cliente[0]} | {cliente[1]} | {cliente[2]} | {cliente[3]} ")
        
        
        try:
         idcliente = int(input("Digite o id do cliente que deseja remover: "))
        except Exception as e:
            print("Erro:",e)
            idcliente   = 0
        
        if idcliente == 0:
            print("Operação Cancelada!")    
        # Exibir as informações do cliente mostrado na tela
        else:        
            clienteEscolhido = conexaoBD.consultarComParametro("SELECT * FROM cliente WHERE id_cliente = %s", (idcliente,))
            
            if (clienteEscolhido == []):
                print("cliente não encontrado!")
            else:
                print(f'''
            ID: {clienteEscolhido[0][0]}          
            Nome: {clienteEscolhido[0][1]}          
            CPF: {clienteEscolhido[0][2]}
            Telefone: {clienteEscolhido[0][3]}''')
            
        # Perguntar se a pessoa deseja remover o cliente
            confirmacao = input("Confirme se deseja remover o cliente (sim/não):")
        
        # Se sim, realizar uma manipulação do tipo DELETE para remover o cliente do banco 
            if (confirmacao == "sim"):
                conexaoBD.manipularComParametro("DELETE FROM cliente WHERE id_cliente = %s",(idcliente,))
                print("cliente removido com sucesso!")
            else:
                print("Operação Cancelada")
        
        pass
    elif (op == "0"):
        break
    else:
        print("Você digitou uma opção inválida!")
    
    input("Tecle ENTER para continuar")

# Implemente a funcionalidade ver cliente