from Conexao import Conexao

conexaoBD = Conexao("localhost", "root", "mysql", "estetica")

def buscarServicoPorId(id):
    
    resultado = conexaoBD.consultarComParametro("SELECT * FROM servicos WHERE id_servico = %s", (id,) )
    
    if (resultado == []):
        return None
    else:
        return resultado[0]
    
def gerarOrdemDeServico(idAtendimento):
    
    itens = conexaoBD.consultarComParametro('''
    SELECT servicos.nome_servico, itens.quantidade_item, itens.preco_unitario_item, atendimento.data_atendimento, atendimento.valor_atendimento FROM itens
    INNER JOIN servicos ON servicos.id_servico = itens.id_servico
    INNER JOIN atendimento ON atendimento.id_atendimento = itens.id_atendimento
    WHERE itens.id_atendimento = %s
                                            ''', (idAtendimento,))
    
    nomeCliente = conexaoBD.consultarComParametro("SELECT clientes.nome_cliente FROM atendimento INNER JOIN clientes ON clientes.id_cliente = atendimento.id_cliente WHERE atendimento.id_atendimento = %s ", (idAtendimento,))
 
    #atendimento = conexaoBD.consultarComParametro("SELECT * FROM atendimento WHERE id_atendimento = %s", (idAtendimento,))
    #idCliente = atendimento[0][1]
    #clienteAtendimento = conexaoBD.consultarComParametro("SELECT * FROM clientes WHERE id_cliente = %s", (idCliente,))

    if (itens != []):
    
    
        '''
            ------- Ordem de Serviço -------
            
            {nome} - {quantidade} - R${preco} - R$ {total}
            {nome} - {quantidade} - R${preco} - R$ {total}
            {nome} - {quantidade} - R${preco} - R$ {total}
            
            
            Total Bruto: R$ {totalBruto}
            Descontos: R$ 0.00
            Total Geral: R$ {totalBruto - desconto}
            Data do Atendimento: {data}
        '''
         
        
        
        ordemDeServico = "----- Ordem de serviço -----\n\n"

        ordemDeServico+= f"Cliente: {nomeCliente[0][0]}\n"

        ordemDeServico += f"{'Serviço realizado':<20} | {'Qtde.':<6} | {'Preço':<10} | {'Total':<10}\n"
        
        for item in itens:
            valorTotal = item[1] * item[2]
                      
            textoItem = f"{item[0]:<20} | {item[1]:6} | R$ {item[2]:.2f} | R$ {valorTotal:.2f}\n"
            
            ordemDeServico += textoItem
        
    
        finalOrdemDeServico = f'''
    Total Bruto: R$ {item[4]:.2f}
    Descontos: R$ 0.00
    Total Geral: R$ {item[4]:.2f}
    Data do Atendimento: {item[3]}
        '''
        ordemDeServico += finalOrdemDeServico
        print(ordemDeServico)
        
    else:
        print("Ordem de serviço não existe!")

def verClientes():

    consultaClientes = conexaoBD.consultar("SELECT * FROM clientes")

    print(f"{'ID':<5} | {'NOME':<20} | {'NASCIMENTO'} | {'TELEFONE'}")
    for cliente in consultaClientes:
        print(f"{cliente[0]:<5} | {cliente[1]:<20} | {cliente[2]} | {cliente[3]}")

def verServicos():

    consultaServicos = conexaoBD.consultar("SELECT * FROM servicos")

    print(f"{'ID':<5} | {'SERVIÇO':<30} | {'PREÇO':<10}")
    for servico in consultaServicos:
        print(f"{servico[0]:<5} | {servico[1]:<30} | {servico[2]:<10}")

def menuAtendimento():

    while True:
            print('''
    Menu Atendimento

    12. Listar ordens de serviço
    13. Adicionar ordem de serviço
    14. Remover ordem de serviço
    0. Voltar ao menu principal
            ''')

            op4 = input("Digite a opção do menu desejada: ")

            if op4 == "12":
                
                atendimentos = conexaoBD.consultar('''SELECT atendimento.id_atendimento, clientes.nome_cliente, atendimento.data_atendimento, atendimento.valor_atendimento FROM atendimento     INNER JOIN clientes ON atendimento.id_cliente = clientes.id_cliente''')    
               
                print(f"{'Nº Ordem':10} | {'Cliente':<20} | {'Data e Hora':<20} | {'Total (R$)':<10}")
                for atendimento in atendimentos:

                    
                    '''
                    %d > dia
                    %m > mês
                    %Y > ano
            
                    %H > hora
                    %M > minuto
                    %S > segundos
                    '''
                    dataConvertida = atendimento[2].strftime("%d/%m/%Y %H:%M:%S")
            
            
                    print(f"{atendimento[0]:<10} | {atendimento[1]:<20} | {dataConvertida:<20} | {atendimento[3]:<10}")
        
                
                numeroOrdem = int(input("Digite o número da ordem que deseja ver detalhes:"))
        
                
                gerarOrdemDeServico(numeroOrdem)

            elif op4 == "13":

                verClientes()
                
                idCliente = input("Digite o id do cliente: ")
     
                carrinhoDeCompras = {}
                
                while (True):
                    verServicos()
                    while (True):
                        idServico = int(input("Digite o id do serviço: "))
                        
                        servico = buscarServicoPorId(idServico) 
                        if (servico == None):
                            print("Escolha um serviço válido!")
                        else:
                            print(servico)
                            break
                
                    
                    while (True):
                        quantidadeServico = int(input("Digite a quantidade do serviço:"))
                        
                        
                        if (quantidadeServico>=1):
                            print("Serviço adicionado ao carrinho!")
                            break
                        else:
                            print("Insira uma quantidade adequada.")
                    
                    carrinhoDeCompras[idServico] = [quantidadeServico, servico]
            
                    sair = input("Deseja continuar (s/n)?: ").lower()
                    if(sair == "s"):
                        pass
                    else:
                        print("Carrinho finalizado!")
                        print(carrinhoDeCompras)
                        break
            
                
                conexaoBD.manipularComParametro("INSERT INTO atendimento VALUES (DEFAULT, %s, DEFAULT, DEFAULT)",(idCliente,))
                idAtendimento = conexaoBD._cursor.lastrowid
        
                valorAtendimento = 0
        
                for idServico in carrinhoDeCompras:
                    quantidadeComprada = carrinhoDeCompras[idServico][0]
                    informacoesServico = carrinhoDeCompras[idServico][1]
            
                    conexaoBD.manipularComParametro("INSERT INTO itens VALUES(DEFAULT, %s, %s, %s, %s)", (idAtendimento, idServico, quantidadeComprada, informacoesServico[2]))
        
                         
                    valorAtendimento += quantidadeComprada * informacoesServico[2]
                       
                conexaoBD.manipularComParametro('''
                UPDATE atendimento
                SET
                valor_atendimento = %s
                WHERE
                id_atendimento = %s
                ''', (valorAtendimento, idAtendimento))
        
                        
                gerarOrdemDeServico(idAtendimento)
                
                
            elif op4 == "14":

                atendimentos = conexaoBD.consultar("SELECT * FROM atendimento")
                       
                print(f"{'Nº Ordem':10} | {'Data e Hora':<20} | {'Total (R$)':<10}\n")
                
                for atendimento in atendimentos:

                    '''
                    %d > dia
                    %m > mês
                    %Y > ano
            
                    %H > hora
                    %M > minuto
                    %S > segundos
                    '''
                    
                    dataConvertida = atendimento[2].strftime("%d/%m/%Y %H:%M:%S")
            
            
                    print(f"{atendimento[0]:<10} | {dataConvertida:<20} | {atendimento[3]:<10}")
        
                
                numeroOrdem = int(input("Digite o número da ordem de serviço que deseja remover:"))
        
                
                gerarOrdemDeServico(numeroOrdem)


                confirmacao = input(f"Deseja remover a ordem de serviço escolhida (s/n)?: ").lower()

                if confirmacao == 's':
                    conexaoBD.manipularComParametro("DELETE FROM itens WHERE id_atendimento = %s", (numeroOrdem,))
                    conexaoBD.manipularComParametro("DELETE FROM atendimento WHERE id_atendimento = %s", (numeroOrdem,))
                    print("Ordem de serviço removida com sucesso!")
                else:
                    print("Operação cancelada.")

                
            elif op4 == "0":
                break
            else:
                print("Opção inválida!")
            
            input("Tecle ENTER para continuar")
