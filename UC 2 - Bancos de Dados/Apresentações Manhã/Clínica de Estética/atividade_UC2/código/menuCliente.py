from Conexao import Conexao

conexaoBD = Conexao("localhost", "root", "mysql", "estetica")

def verClientes():

    consultaClientes = conexaoBD.consultar("SELECT * FROM clientes")

    print(f"{'ID':<5} | {'NOME':<20} | {'NASCIMENTO'} | {'TELEFONE'}")
    for cliente in consultaClientes:
        print(f"{cliente[0]:<5} | {cliente[1]:<20} | {cliente[2]} | {cliente[3]}")


def menuCliente():

    while True:
            print('''
    Menu Clientes

    4. Listar clientes
    5. Adicionar cliente
    6. Atualizar informações de cliente
    7. Remover cliente
    0. Voltar ao menu principal
            ''')

            op2 = input("Digite a opção do menu desejada: ")

            if op2 == "4":
                verClientes()
            
            elif op2 == "5":
                print("\nCadastro de Cliente\n")
                nome=input("Digite o nome do(a) cliente: ")
                nascimento=input("Digite a data de nascimento (AAAA-MM-DD): ")
                telefone=input("Digite o número de telefone (11 dígitos): ")
                                             
                conexaoBD.manipularComParametro("INSERT INTO clientes VALUES (DEFAULT, %s, %s, %s)",(nome, nascimento, telefone))

                print("Cliente cadastrado com sucesso!")

            elif op2 == "6":
            
                verClientes()

                try:
                    idCliente = int(input("Digite o id do(a) cliente escolhido: "))
                except Exception as e:
                    print("Erro: ",e)
                    idCliente = 0

                if idCliente == 0:
                    print("Encerrando Operação...")
                else:
                    clienteEscolhido = conexaoBD.consultarComParametro("SELECT * FROM clientes WHERE id_cliente = %s", (idCliente,))

                if clienteEscolhido == []:
                    print("Cliente não encontrado!")
                else:
                    print(f'''
ID: {clienteEscolhido[0][0]}
Nome: {clienteEscolhido[0][1]}
Data de nascimento: {clienteEscolhido[0][2]}
Telefone: {clienteEscolhido[0][3]}
                    ''')

                    nome = clienteEscolhido[0][1]
                    nascimento = clienteEscolhido[0][2]
                    telefone = clienteEscolhido[0][3]

                    novoNome = input("Digite o novo nome: ")
                    if novoNome == "":
                        novoNome = nome
                    novoNascimento = input("Digite a nova data de nascimento: ")
                    if novoNascimento == "":
                        novoNascimento = nascimento
                    novoTelefone = input("Digite o novo número de telefone: ")
                    if novoTelefone == "":
                        novoTelefone = telefone

                    sql = '''
                    UPDATE clientes
                    SET
                        nome_cliente = %s,
                        nascimento_cliente = %s,
                        telefone_cliente = %s
                    WHERE
                        id_cliente = %s;
                    '''
                    conexaoBD.manipularComParametro(sql, (novoNome, novoNascimento, novoTelefone, idCliente))
                    print("Cliente atualizado com sucesso!")


            elif op2 == "7":
                verClientes()

                try:
                    idCliente = int(input("Digite o id do(a) cliente escolhido: "))
                except Exception as e:
                    print("Erro: ",e)
                    idCliente = 0
                
                if idCliente == 0:
                    print("Encerrando Operação...")
                else:
                    clienteEscolhido = conexaoBD.consultarComParametro("SELECT * FROM clientes WHERE id_cliente = %s", (idCliente,))

                if clienteEscolhido == []:
                    print("Cliente não encontrado!")
                else:
                    print(f'''
ID: {clienteEscolhido[0][0]}
Nome: {clienteEscolhido[0][1]}
Data de nascimento: {clienteEscolhido[0][2]}
Telefone: {clienteEscolhido[0][3]}
                    ''')

                confirmacao = input(f"Deseja remover a cliente {clienteEscolhido[0][1]} (s/n)?: ").lower()
        
                if confirmacao == 's':
                    conexaoBD.manipularComParametro("DELETE FROM clientes WHERE id_cliente = %s", (idCliente,))
                    print("Cliente removido com sucesso!")
                else:
                    print("Operação cancelada.")
                
            elif op2 == "0":
                break
            else:
                print("Opção inválida!")
            
            input("Tecle ENTER para continuar")