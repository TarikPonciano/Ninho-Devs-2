from Conexao import Conexao

conexaoBD = Conexao("localhost", "root", "mysql", "Avilanca")

listanum = ['1','2','3','0']


while True:

    print('''
    |---------|Avilanca|---------|
            Bem Vindo

    1. Ver Voos
    2. Comprar passagem
    3. Ver passagem comprada
    0. Sair

        ''')


    opcao = input("Selecione uma opção: ")

    if opcao not in listanum:
        print("ERRO: Numero invalido")
    elif opcao == '0':
        break
    elif opcao == '1':
        voos = conexaoBD.consultar("SELECT * FROM voo")
        print("| Numero do Voo | Local de saida | Local de Chegada | Data de Partida | Data de Chegada | Preço |")
        for i in voos:
            print(f"{i[0]} - {i[2]} - {i[3]} - {i[4]} - {i[5]} - {i[6]}")
        i = input("Aperte enter para sair.")

    elif opcao == '2':

        print("Insira credenciais:")
        nomecli = input("NOME: ")
        cpfcli = input("CPF: ")
        datanasccli = input("DATA DE NASCIMENTO: ")
        nascionalidadecli = input("NASCIONALIDADE: ")
        telcli = input("TELEFONE: ")
        emailcli = input("EMAIL: ")
        numvoo = input("NUMERO DO VOO: ")
        assentos = input("NUMERO DO ASSENTO: ")
        print('''Escolha sua forma de pagamento:
1. Credito
2. Debito
3. Boleto
4. Pix
''')
        formadepagamento = input("> ")
        if formadepagamento == '1':
            formadepagamento == 'Credito'
        elif formadepagamento == '2':
            formadepagamento == 'Debito'
        elif formadepagamento == '3':
            formadepagamento == 'Boleto'
        elif formadepagamento == '4':
            formadepagamento == 'Pix'
        else:
            print("ERRO: Numero invalido")

        conexaoBD.manipularComParametros("INSERT INTO cliente VALUES(DEFAULT, %s, %s, %s, %s, %s, %s, DEFAULT)", (nomecli, cpfcli, datanasccli, nascionalidadecli, telcli, emailcli))
        idcliente = conexaoBD._cursor.lastrowid
        conexaoBD.manipularComParametros("INSERT INTO passagem VALUES(DEFAULT, %s, %s, DEFAULT, %s, %s)", (idcliente, numvoo, formadepagamento, assentos))

        informacoes = conexaoBD.consultarComParametros("SELECT * FROM cliente WHERE id_cliente = %s", (idcliente, ))
        informacoes2 = conexaoBD.consultarComParametros("SELECT * FROM passagem WHERE id_cliente = %s", (idcliente, ))
        informacoes3 = conexaoBD.consultarComParametros("SELECT * FROM voo WHERE id_voo = %s", (numvoo, ))

        print(f'''
INFORMAÇÕES DA PASSAGEM:
ID da passagem: {informacoes2[0][0]}
CPF do cliente: {informacoes[0][2]}
Avião: {informacoes2[0][2]}
Data de partida: {informacoes3[0][4]}
Ponto de partida: {informacoes3[0][2]}
Destino final: {informacoes3[0][3]}
N. do Assento: {informacoes2[0][5]}
''')        
        
        input("Aperte enter para sair.")

    elif opcao == '3':
    
        while True:
            selecao = input("Digite ID da passagem: ")

            passagem = conexaoBD.consultarComParametros("SELECT * FROM passagem WHERE id_passagem = %s", (selecao,))
            if passagem == []:
                print("Passagem não encontrada")
                break
            else:

                cliente = passagem[0][1]
                voo = passagem [0][2]
                cliente2 = conexaoBD.consultarComParametros("SELECT * FROM cliente WHERE id_cliente = %s", (cliente,))
                voo2 = conexaoBD.consultarComParametros("SELECT * FROM voo WHERE id_voo = %s", (voo,))
                print(f'''
INFORMAÇÕES DA PASSAGEM:
ID da passagem: {passagem[0][0]}
CPF do cliente: {cliente2[0][2]}
Avião: {passagem[0][2]}
Data de partida: {voo2[0][4]}
Ponto de partida: {voo2[0][2]}
Destino final: {voo2[0][3]}
N. do Assento: {passagem[0][5]}
''')    
                input("Tecle Enter: ")
            print('''
------Menu------
1. Cancelar passagem
2. Sair
''')    
            choice1 = input("Digite o numero da sua escolha: ")
            if choice1 == ("1"):
                conexaoBD.manipularComParametros("DELETE FROM passagem WHERE id_passagem = %s", (selecao,))
                break
            elif choice1 == ("2"):
                break
            else:
                print("Erro!!!")
                break
        input("Tecle Enter: ")



