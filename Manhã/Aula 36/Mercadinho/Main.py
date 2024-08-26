from Conexao import Conexao

# Criar um menu de aplicação com as opções:
# 1. Ver Produtos
# 2. Cadastrar Venda
# 0. Sair

conexaoBD = Conexao("localhost", "root", "mysql", "jomart")

def buscarProdutoPorId(id):
    #Faz uma consulta usando where para buscar 1 produto só
    resultado = conexaoBD.consultarComParametro("SELECT * FROM produtos WHERE id_produto = %s", (id,) )
    #Retorna a tupla do primeiro produto encontrado se achar algum produto e retorna None se não achar nenhum produto
    if (resultado == []):
        return None
    else:
        return resultado[0]
    

def verProdutos():
    #Imprimir os produtos disponíveis no formato:
    #ID | Nome | Preço (R$) | Estoque

    consultaProdutos = conexaoBD.consultar("SELECT * FROM produtos")
    
    print("ID | Nome | Preço (R$) | Estoque ")
    for produto in consultaProdutos:
        print(f"{produto[0]} | {' '*round((15 - (len(produto[1]))/2))} {produto[1]} {' '*round((15 - (len(produto[1]))/2))} | {produto[2]} | {produto[3]} ")
        
def gerarNotaFiscal(idVenda):
    # Consultar o banco de dados para resgatar todos os itens associados a àquela venda. (Usar Select com Where)
    itens = conexaoBD.consultarComParametro('''
    SELECT produtos.nome_produto, itens.quantidade_item, itens.preco_unitario_item, vendas.data_venda, vendas.valor_venda FROM itens
    INNER JOIN produtos ON produtos.id_produto = itens.id_produto
    INNER JOIN vendas ON vendas.id_venda = itens.id_venda
    WHERE itens.id_venda = %s
                                            ''', (idVenda,))
    
    # Observar como vieram as informações > [()]
    # Consumir a informação para imprimir a nota fiscal seguindo o padrão:
    
    '''
        ------- Nota Fiscal -------
        
        {nome} - {quantidade} - R${preco} - R$ {total}
        {nome} - {quantidade} - R${preco} - R$ {total}
        {nome} - {quantidade} - R${preco} - R$ {total}
        
        
        Total Bruto: R$ {totalBruto}
        Descontos: R$ 0.00
        Total Geral: R$ {totalBruto - desconto}
        Data da Venda: {data}
    '''
    # Para construir essa mensagem crie uma variável de texto(string) e acrescente a ela as informações de cada item encontrado.  
    
    notaFiscal = "----- Nota Fiscal -----\n\n"
    notaFiscal += "Produto - Quantidade - Preço - Total\n\n"
    for item in itens:
        valorTotal = item[1] * item[2]
        
        #Melhorar a impressão do item para conter o nome do Produto, ao invés de id do Produto
        # produto = conexaoBD.consultarComParametro("SELECT nome_produto FROM produtos WHERE id_produto = %s", (item[1],)) 
        
        # textoItem = f"{produto[0][0]} - {item[3]} - R$ {item[4]:.2f} - R$ {valorTotal:.2f}\n "
        
        textoItem = f"{item[0]} - {item[1]} - R$ {item[2]:.2f} - R$ {valorTotal:.2f}\n "
        
        notaFiscal += textoItem
    
   
    finalNotaFiscal = f'''
Total Bruto: R$ {item[4]:.2f}
Descontos: R$ 0.00
Total Geral: R$ {item[4]:.2f}
Data da Venda: {item[3]}
    '''
    notaFiscal += finalNotaFiscal
    print(notaFiscal)
    

while True:
    
    print('''
    Bem vindo ao Mercadinho Jomart
    
    Menu:
    
    1. Ver Produtos
    2. Cadastrar Venda
    3. Ver Notas Fiscais
    0. Sair      
        ''')
    
    menu = input("Digite a opção desejada: ")
    
    if (menu == "1"):
        verProdutos()
    elif (menu == "2"):
        # Exibir a tabela de produtos 
       
        carrinhoDeCompras = {}
        # Escolher os ids dos produtos que serão comprados.
        while (True):
            verProdutos()
            while (True):
                idProduto = int(input("Digite o id do produto: "))
                #   - Validar se o produto existe no banco (Buscar produto)
                produto = buscarProdutoPorId(idProduto) 
                if (produto == None):
                    print("Escolha um produto válido!")
                else:
                    print(produto)
                    break
                
            # Pedir a quantidade de cada produto
            while (True):
                quantidadeProduto = int(input("Digite a quantidade do produto:"))
                #   - Validar se a quantidade é possível
                quantidadeDisponivel = produto[3]
                if (quantidadeDisponivel>=quantidadeProduto and quantidadeProduto>0):
                    print("Produto adicionado ao carrinho!")
                    break
                else:
                    print("Insira uma quantidade adequada.")
                    
            carrinhoDeCompras[idProduto] = [quantidadeProduto, produto]
            
            sair = input("Deseja continuar? S/N")
            if(sair == "S"):
                pass
            else:
                print("Carrinho finalizado!")
                print(carrinhoDeCompras)
                break
            
        # Criar a venda (Inserir uma venda)
        conexaoBD.manipular("INSERT INTO vendas VALUES (DEFAULT, DEFAULT, DEFAULT)")
        idVenda = conexaoBD._cursor.lastrowid
        
        # id = conexaoBD.manipular("INSERT INTO vendas VALUES (DEFAULT, DEFAULT, DEFAULT)")
        # Registrar os itens da venda (Descobrir o id da venda)
        valorVenda = 0
        
        for idProduto in carrinhoDeCompras:
            quantidadeComprada = carrinhoDeCompras[idProduto][0]
            informacoesProduto = carrinhoDeCompras[idProduto][1]
            
            conexaoBD.manipularComParametro("INSERT INTO itens VALUES(DEFAULT, %s, %s, %s, %s)", (idProduto, idVenda, quantidadeComprada, informacoesProduto[2]))
        
        # Atualizar o estoque dos produtos
            novaQuantidade = informacoesProduto[3] - quantidadeComprada
            
            conexaoBD.manipularComParametro('''
            UPDATE produtos
            SET
            estoque_produto = %s
            WHERE id_produto = %s''', (novaQuantidade,idProduto))
            
            valorVenda += quantidadeComprada * informacoesProduto[2]
        # Atualizar a venda com seu valor total
        
        conexaoBD.manipularComParametro('''
        UPDATE vendas
        SET
        valor_venda = %s
        WHERE
        id_venda = %s
        ''', (valorVenda, idVenda))
        
        # Imprimir na tela a "nota fiscal" com produtos, preços, quantidades e valor total
        # Buscar todos os itens da venda registrada(idVenda) e imprimir nas informações na tela
        
        gerarNotaFiscal(idVenda)
        
       
    elif (menu == "3"):
        # Imprime na tela as notas fiscais seguindo o padrão:
        # Número da Nota - Data da Nota - Total da Nota
        # Pede para o usuário escolher uma das notas pelo número
        # Usa o gerarNotaFiscal para exibir as informações daquela notinha na tela
        pass
    elif (menu == "0"):
        print("Saindo do programa...")
        break
    else:
        print("Você digitou uma opção inválida!")
    
    input("Tecle Enter para continuar!")
    
