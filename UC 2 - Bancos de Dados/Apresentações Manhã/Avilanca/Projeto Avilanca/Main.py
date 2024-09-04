from Conexao import Conexao

conexaoBD = Conexao("localhost", "root", "mysql", "avilanca")

while True:
        print('''
|---------|Avilanca|---------|
        Banco de Dados

1. Passagens
2. Voos
3. Clientes
0. Sair

''')
        opcao = input("Selecione uma opção: ")

        if opcao == '1':
                while True:

                        print('''
        ---------
        1. Ver passagens
        2. Editar passagem
        0. Voltar

                        ''')
                        op_1 = input("Selecione uma opção: ")

                        if op_1 == '0':
                                break

                        elif op_1 == '1':
                                passagens = conexaoBD.consultar("SELECT * FROM passagem")
                                print("|ID Passagem |ID Cliente |ID Voo |Data de compra |Forma de Pagamento |N. do Assento |")
                                for i in passagens:
                                        print(f"{i[0]} - {i[1]} - {i[2]} - {i[3]} - {i[4]} - {i[5]}")
                                input("\nAperte enter para prosseguir")
                        elif op_1 == '2':
                                while True:
                                        selecao = input("Digite ID da passagem: ")

                                        passagem = conexaoBD.consultarComParametros("SELECT * FROM passagem WHERE id_passagem = %s", (selecao,))
                                        if passagem == []:
                                                print("Passagem não encontrada")
                                                break
                                        else:

                                                print(f'''
        -Informações basicas-
        ID da passagem: {passagem[0][0]}
        ID do cliente: {passagem[0][1]}
        
        Outras informações (Selecione opção a ser alterada):
        1. ID do voo: {passagem[0][2]}
        2. Data da compra: {passagem[0][3]}
        3. Forma de pagamento: {passagem[0][4]}
        4. Numero do assento: {passagem[0][5]}  
        5. Remover todos os dados
        0. Sair                 
                                                ''')
                                                
                                                opcaoedit = input("> ")
                                                if opcaoedit == '0':
                                                        break
                                                if opcaoedit == '1':
                                                        opcaoedit = "id_voo"
                                                if opcaoedit == '2':
                                                        opcaoedit = "data_venda"
                                                if opcaoedit == '3':
                                                        opcaoedit = "forma_pagamento"
                                                if opcaoedit == '4':
                                                        opcaoedit = "n_do_assento"
                                                if opcaoedit2 == '5':
                                                        conexaoBD.manipularComParametros("DELETE FROM passagem WHERE id_passsagem = %s", (selecao,))
                                                        print("Dados excluidos.")
                                                        input("Aperte enter para prosseguir\n")
                                                        break
                                                
                                                modific = input("Escreva alteração: ")
                                                

                                                edit = conexaoBD.manipularComParametros(f'''
        UPDATE passagem
        SET 
        {opcaoedit} = %s
        WHERE id_passagem = %s
        ''', (modific, selecao,))
                                

                                        passagemnovo = conexaoBD.consultarComParametros("SELECT * FROM passagem WHERE id_passagem = %s", (selecao,))
                                        print(f'''
        -Informações Atualizadas-
        ID da passagem: {passagemnovo[0][0]}
        ID do cliente: {passagemnovo[0][1]}
        ID do voo: {passagemnovo[0][2]}
        Data da compra: {passagemnovo[0][3]}
        Forma de pagamento: {passagemnovo[0][4]}
        Numero do assento: {passagemnovo[0][5]}                 
                                                ''')
                                        input("\nAperte enter para prosseguir")
                                        break
                        else:
                                print("ERRO")

        elif opcao == '2':
                while True:
                        print('''
        ---------
        1. Ver voos
        2. Editar voo
        3. Adicionar voo
        0. Voltar
                        ''')
                        
                        op_2 = input("Selecione uma opção: ")

                        if op_2 == '0':
                                break

                        elif op_2 == "3":
                                desi = input("Digite o destino inicial: ")
                                desf = input("Digite o destino final: ")
                                dats = input("Digite a data de saida: ")
                                datc = input("Digite a data de chegada: ")
                                prec = input("Digite o preço da passagem: ")
                                conexaoBD.manipularComParametros("INSERT INTO voo VALUES(DEFAULT, DEFAULT, %s, %s, %s, %s, %s)", (desi, desf, dats, datc, prec))

                                input("\nAperte enter para prosseguir")
                                
                        elif op_2 == '1':
                                voos213 = conexaoBD.consultar("SELECT * FROM voo")
                                print("|ID Voo |ID Avião |Destino Inicial |Destino Final |Data de Saida |Data de chegada |Preço |")
                                for i2 in voos213:
                                        print(f"{i2[0]} - {i2[1]} - {i2[2]} - {i2[3]} - {i2[4]} - {i2[5]} - {i2[6]}")
                                input("\nAperte enter para prosseguir")
                        elif op_2 == '2':
                                while True:
                                        selecao2 = input("Digite ID do voo: ")

                                        voo111 = conexaoBD.consultarComParametros("SELECT * FROM voo WHERE id_voo = %s", (selecao2,))
                                        if voo111 == []:
                                                print("Voo não encontrado")
                                                break
                                        else:

                                                print(f'''
        -Informações basicas-
        ID do voo: {voo111[0][0]}

        Outras informações (Selecione opção a ser alterada):
        1. ID do avião: {voo111[0][1]}
        2. Destino inicial: {voo111[0][2]}
        3. Destino final: {voo111[0][3]}
        4. Data de saida: {voo111[0][4]}
        5. Data de chegada: {voo111[0][5]}
        6. Preço: {voo111[0][6]}  
        7. Remover todos os dados
        0. Sair                 
                                                ''')
                                                
                                                opcaoedit2 = input("> ")
                                                if opcaoedit2 == '0':
                                                        break
                                                if opcaoedit2 == '1':
                                                        opcaoedit2 = "id_aviao"
                                                if opcaoedit2 == '2':
                                                        opcaoedit2 = "destino_inicial"
                                                if opcaoedit2 == '3':
                                                        opcaoedit2 = "destino_final"
                                                if opcaoedit2 == '4':
                                                        opcaoedit2 = "data_saida"
                                                if opcaoedit2 == '5':
                                                        opcaoedit2 = "data_chegada"
                                                if opcaoedit2 == '6':
                                                        opcaoedit2 = "preco"
                                                if opcaoedit2 == '7':
                                                                conexaoBD.manipularComParametros("DELETE FROM passagem WHERE id_voo = %s", (selecao2,))
                                                                conexaoBD.manipularComParametros("DELETE FROM voo WHERE id_voo = %s", (selecao2,))
                                                                print("Dados excluidos.")
                                                                input("Aperte enter para prosseguir\n")
                                                                break
                                                
                                                modific2 = input("Escreva alteração: ")
                                                

                                                edit = conexaoBD.manipularComParametros(f'''
        UPDATE voo
        SET 
        {opcaoedit2} = %s
        WHERE id_voo = %s
        ''', (modific2, selecao2,))
                                

                                        voonovo = conexaoBD.consultarComParametros("SELECT * FROM voo WHERE id_voo = %s", (selecao2,))
                                        print(f'''
        -Informações Atualizadas-
        ID do voo: {voonovo[0][0]}
        ID do aviao: {voonovo[0][1]}
        Destino inicial: {voonovo[0][2]}
        Destino final: {voonovo[0][3]}
        Data de saida: {voonovo[0][4]}
        Data de chegada: {voonovo[0][5]}
        Preço: {voonovo[0][6]}                  
                                                ''')
                                        input("\nAperte enter para prosseguir")
                                        break
                        else:
                                print("ERRO")
     
        elif opcao == '3':
                while True:
                        print('''
---------
1. Ver clientes
2. Editar cliente
0. Voltar
                        ''')
                        
                        op_3 = input("Selecione uma opção: ")

                        if op_3 == '0':
                                break
                                
                        elif op_3 == '1':
                                cliente32 = conexaoBD.consultar("SELECT * FROM cliente")
                                print("|ID Cliente |Nome |CPF |Data de nascimento |Nacionalidade |Telefone |Email |Requisitos Especiais |")
                                for i3 in cliente32:
                                        print(f"{i3[0]} - {i3[1]} - {i3[2]} - {i3[3]} - {i3[4]} - {i3[5]} - {i3[6]} - {i3[7]}")
                                input("\nAperte enter para prosseguir")
                        elif op_3 == '2':
                                while True:
                                        selecao3 = input("Digite ID do cliente: ")

                                        cliente321 = conexaoBD.consultarComParametros("SELECT * FROM cliente WHERE id_cliente = %s", (selecao3,))
                                        if cliente321 == []:
                                                print("Cliente não encontrado")
                                                break
                                        
                                        else:

                                                print(f'''
-Informações basicas-
ID do Cliente: {cliente321[0][0]}

Outras informações (Selecione opção a ser alterada):
1. Nome: {cliente321[0][1]}
2. CPF: {cliente321[0][2]}
3. Data de nascimento: {cliente321[0][3]}
4. Nacionalidade: {cliente321[0][4]}
5. Telefone: {cliente321[0][5]}
6. Email: {cliente321[0][6]}  
7. Requisitos especiais: {cliente321[0][7]}
8. Remover todos os dados
0. Sair                 
                                                ''')
                                                
                                                opcaoedit3 = input("> ")
                                                if opcaoedit3 == '0':
                                                        break
                                                if opcaoedit3 == '1':
                                                        opcaoedit3 = "nome_cliente"
                                                if opcaoedit3 == '2':
                                                        opcaoedit3 = "documento_cliente"
                                                if opcaoedit3 == '3':
                                                        opcaoedit3 = "data_nasc_cliente"
                                                if opcaoedit3 == '4':
                                                        opcaoedit3 = "nacionalidade_cliente"
                                                if opcaoedit3 == '5':
                                                        opcaoedit3 = "telefone_cliente"
                                                if opcaoedit3 == '6':
                                                        opcaoedit3 = "email_cliente"
                                                if opcaoedit3 == '7':
                                                        opcaoedit3 = "requesitos_esp_cliente"
                                                if opcaoedit3 == '8':
                                                        conexaoBD.manipularComParametros("DELETE FROM passagem WHERE id_cliente = %s", (selecao3,))
                                                        conexaoBD.manipularComParametros("DELETE FROM cliente WHERE id_cliente = %s", (selecao3,))
                                                        print("Dados excluidos.")
                                                        input("Aperte enter para prosseguir\n")
                                                        break


                                                modific3 = input("Escreva alteração: ")
                                                

                                                edit = conexaoBD.manipularComParametros(f'''
        UPDATE cliente
        SET 
        {opcaoedit3} = %s
        WHERE id_cliente = %s
        ''', (modific3, selecao3,))
                                

                                        clientenovo = conexaoBD.consultarComParametros("SELECT * FROM cliente WHERE id_cliente = %s", (selecao3,))
                                        print(f'''
-Informações Atualizadas-
ID do Cliente: {clientenovo[0][0]}
Nome: {clientenovo[0][1]}
CPF: {clientenovo[0][2]}
Data de nascimento: {clientenovo[0][3]}
Nacionalidade: {clientenovo[0][4]}
Telefone: {clientenovo[0][5]}
Email: {clientenovo[0][6]}  
Requisitos especiais: {clientenovo[0][7]}
                                                ''')
                                        input("\nAperte enter para prosseguir")
                                        break
                        else:
                                print("ERRO")

        elif opcao == '0':
                break
        else:
                print("ERRO: Numero invalido")

