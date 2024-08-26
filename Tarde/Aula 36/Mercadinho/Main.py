from Conexao import Conexao

conexaoBD = Conexao("localhost", "root", "mysql", "mercadojoa")

def verProdutos():
    
    produtos = conexaoBD.consultar("SELECT * FROM produtos")
    
    print(f"ID |{' ' * (15-2)}Nome{' ' * (15-2)}| Preço (R$) | Estoque")
    for produto in produtos:
        espacoNome = ' ' * round(15-(len(produto[1])/2))
        print(f"{produto[0]} |{espacoNome}{produto[1]}{espacoNome}| {produto[2]} | {produto[3]}")
        
def buscarProdutoPorId(id):
    #Função que busca o banco por um produto específico usando o id e retorna a tupla do primeiro produto do resultado se não retorna None
    
    resultado = conexaoBD.consultarComParametros("SELECT * FROM produtos WHERE id_produto = %s", (id,)) 
    
    if (resultado == []):
        return None
    else:
        return resultado[0]
    
def gerarNotaFiscal(idVenda):
    # Consultar a tabela itens e encontrar todos os itens que fizeram parte da venda identificada por idVenda
    
    # itens = conexaoBD.consultarComParametros("SELECT * FROM itens WHERE id_venda = %s", (idVenda,))
    
    itens = conexaoBD.consultarComParametros('''
    SELECT produtos.nome_produto, itens.quantidade_item, itens.preco_unitario_item, vendas.data_venda, vendas.valor_total_venda FROM itens
    INNER JOIN produtos ON produtos.id_produto = itens.id_produto
    INNER JOIN vendas ON vendas.id_venda = itens.id_venda
    WHERE itens.id_venda = %s; ''', (idVenda,))
    
    # Ler as informações obtidas e gerar uma nota fiscal no seguinte formato:
    # Use uma variável do tipo texto e "incremente" ela
    '''
    ------- Nota Fiscal -------
    
    Nome - Quantidade - Preço - Total
    
    {nome} - {quantidade} - R${preco} - R$ {total}
    {nome} - {quantidade} - R${preco} - R$ {total}
    {nome} - {quantidade} - R${preco} - R$ {total}
    
    
    Total Bruto: R$ {totalBruto}
    Descontos: R$ 0.00
    Total Geral: R$ {totalBruto - desconto}
    Data da Venda: {data}
    '''
    
    notaFiscal = "----- Nota Fiscal ----- \n\n"
    notaFiscal += "Nome - Quantidade - Preço - Total \n\n"
    
    
    for item in itens:
        totalProduto = item[1] * item[2]
        # produto = buscarProdutoPorId(item[1])
        # notaFiscal += f"{produto[1]} - {item[3]} - R$ {item[4]:.2f} - R$ {totalProduto:.2f}\n"
         
        notaFiscal += f"{item[0]} - {item[1]} - R$ {item[2]:.2f} - R$ {totalProduto:.2f}\n"
    # Para conseguir o nome você deve usar o idProduto para buscar na tabela produtos
    
    # Para conseguir Total Bruto pode-se calcular ao imprimir cada item ou pode-se consultar a tabela vendas
    # Para conseguir a data da venda você pode usar o idVenda para encontrar a venda certa na tabela vendas
    # venda = conexaoBD.consultarComParametros("SELECT * FROM vendas WHERE id_venda= %s", (idVenda,))
    # totalBruto = venda[0][2]
    # data = venda[0][1]
    
    totalBruto = item[4]
    data = item[3].strftime("%d/%m/%Y %H:%M:%S")

    notaFiscal += f'''
Total Bruto = R$ {totalBruto}
Descontos = R$ 0.00
Total Final = R$ {totalBruto}
Data da Venda = {data}
    '''
    print(notaFiscal)
    

            
# Crie um programa que exibe um menu com as opções:
# 1. Ver Produtos
# 2. Cadastrar Venda
# 0. Sair

# Peça ao usuário qual opção deseja, e execute a funcionalidade escolhida

while True:
    
    print('''
    Bem Vindo ao Mercado Joa
    
    Menu:
    
    1. Ver Produtos
    2. Cadastrar Venda
    0. Sair     
        ''')
    
    op = input("Digite a opção desejada: ")
    
    if (op == "1"):
        verProdutos()
    elif (op == "2"):
        # Mostrar a tabela de produtos para o usuário
        verProdutos()
        
        while True:
            # Pedir o id dos produtos da compra
            idProduto = int(input("Digite o id do produto:"))
            
            #   - Verifica se o produto existe no banco de dados
            # Consulta o banco pra ver se o produto com id específico existe
            produto = buscarProdutoPorId(idProduto) #Retornar uma tupla
            
            if produto == None:
                print("Produto não encontrado! Digite um id válido!")
            else:
                print(f"Você escolheu {produto[1]}")
                break

        while (True):
            # Pedir a quantidade de unidades compradas daquele produto
            
            quantidadeComprada = int(input("Digite a quantidade que deseja comprar: "))
            
            #   - Verificar se o estoque é suficiente
            
            estoqueTotal = produto[3]
            
            if estoqueTotal >= quantidadeComprada and quantidadeComprada>0:
                print(f"Foram adicionados {quantidadeComprada} cópias do produto ao carrinho.")
                break
            else:
                print("Digite uma quantidade válida.")
            
        
        # Criar a venda (Inserir Venda)
        # idVenda = conexaoBD.manipular("INSERT INTO vendas VALUES (DEFAULT, DEFAULT, DEFAULT)")
        
        conexaoBD.manipular("INSERT INTO vendas VALUES (DEFAULT, DEFAULT, DEFAULT)")
        idVenda = conexaoBD._cursor.lastrowid
        
        # Criar os registros de venda dos produtos (Inserir na tabela itens)
        
        conexaoBD.manipularComParametros('''INSERT INTO itens VALUES (DEFAULT, %s, %s, %s, %s);''', (idProduto, idVenda, quantidadeComprada, produto[2]))
        
        # Atualizar a quantidade de produto na tabela produto
        novoEstoque = estoqueTotal - quantidadeComprada
        
        conexaoBD.manipularComParametros('''
        UPDATE produtos
        SET
        estoque_produto = %s
        WHERE
        id_produto = %s''', (novoEstoque, idProduto))
        
        # Atualiza a venda com o Valor Total dos produtos   
        valorTotal = float(produto[2]) * quantidadeComprada
        conexaoBD.manipularComParametros('''
        UPDATE vendas
        SET
        valor_total_venda = %s
        WHERE 
        id_venda = %s''',(valorTotal, idVenda))
        
        # Criar nota fiscal simples com produto, quantidade, preço e valor total    
        gerarNotaFiscal(idVenda)
        
    elif (op == "0"):
        print("Saindo do Programa...")
        break
    else:
        print("Você digitou uma operação inválida.")
        
    input("Tecle Enter para continuar!")
    


