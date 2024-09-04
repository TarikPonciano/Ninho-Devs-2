from Conexao import Conexao

conexaoBD = Conexao("localhost", "root", "mysql", "estetica")

def verServicos():

    consultaServicos = conexaoBD.consultar("SELECT * FROM servicos")

    print(f"{'ID':<5} | {'SERVIÇO':<30} | {'PREÇO':<10}")
    for servico in consultaServicos:
        print(f"{servico[0]:<5} | {servico[1]:<30} | {servico[2]:<10}")

def menuServico():

    while True:
            print('''
    Menu Serviços

    8. Listar serviços
    9. Adicionar serviço
    10. Atualizar informações de serviço
    11. Remover serviço
    0. Voltar ao menu principal
            ''')

            op3 = input("Digite a opção do menu desejada: ")

            if op3 == "8":
                verServicos()

            elif op3 == "9":
                print("\nCadastro de Serviço\n")
                servico=input("Digite o nome do novo serviço: ")
                valor=input("Digite o valor do novo serviço: ")
                                             
                conexaoBD.manipularComParametro("INSERT INTO servicos VALUES (DEFAULT, %s, %s)",(servico, valor))

                print("Serviço cadastrado com sucesso!")

            elif op3 == "10":

                verServicos()

                try:
                     idServico = int(input("Digite o id do serviço escolhido: "))
                except Exception as e:
                    print("Erro: ", e)
                    idServico = 0

                if idServico == 0:
                    print("Encerrando Operação...")
                else:
                    servicoEscolhido = conexaoBD.consultarComParametro("SELECT * FROM servicos WHERE id_servico = %s", (idServico,))

                if servicoEscolhido == []:
                    print("Serviço não encontrado!")
                else:
                    print(f'''
ID: {servicoEscolhido[0][0]}
Serviço: {servicoEscolhido[0][1]}
Valor: {servicoEscolhido[0][2]}
        ''')

                servico = servicoEscolhido[0][1]
                valor = servicoEscolhido[0][2]

                novoServico = input("Digite o nome do novo serviço: ")
                if novoServico == "":
                    novoServico = servico
                novoValor = input("Digite o novo valor do serviço: ")
                if novoValor == "":
                    novoValor = valor

        
                sql = '''
        UPDATE servicos
        SET
            nome_servico = %s,
            preco_servico = %s
        WHERE
            id_servico = %s;
        '''
                conexaoBD.manipularComParametro(sql, (novoServico, novoValor, idServico))
                print("Serviço atualizado com sucesso!")

            elif op3 == "11":

                verServicos()

                try:
                    idServico = int(input("Digite o id do serviço escolhido: "))
                except Exception as e:
                    print("Erro: ",e)
                    idServico = 0
                
                if idServico == 0:
                    print("Encerrando Operação...")
                else:
                    servicoEscolhido = conexaoBD.consultarComParametro("SELECT * FROM servicos WHERE id_servico = %s", (idServico,))

                if servicoEscolhido == []:
                    print("Serviço não encontrado!")
                else:
                    print(f'''
ID: {servicoEscolhido[0][0]}
Serviço: {servicoEscolhido[0][1]}
Valor: {servicoEscolhido[0][2]}
                    ''')

                confirmacao = input(f"Deseja remover o serviço {servicoEscolhido[0][1]} (s/n)? ").lower()
        
                if confirmacao == 's':
                    conexaoBD.manipularComParametro("DELETE FROM servicos WHERE id_servico = %s", (idServico,))
                    print("Serviço removido com sucesso!")
                else:
                    print("Operação cancelada.")

            elif op3 == "0":
                break
            else:
                print("Opção inválida!")
            
            input("Tecle ENTER para continuar")