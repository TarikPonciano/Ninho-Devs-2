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
    


while True:
    
    print('''
    Bem vindo ao Mercadinho Jomart
    
    Menu:
    
    1. Ver Produtos
    2. Cadastrar Venda
    0. Sair      
          ''')
    
    menu = input("Digite a opção desejada: ")
    
    if (menu == "1"):
        verProdutos()
    elif (menu == "2"):
        # Exibir a tabela de produtos 
        verProdutos()
        # Escolher os ids dos produtos que serão comprados.
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
            
        # Criar a venda (Inserir uma venda)
        # Registrar os itens da venda
        # Atualizar o estoque dos produtos
        # Atualizar a venda com seu valor total
        # Imprimir na tela a "nota fiscal" com produtos, preços, quantidades e valor total
        pass
    elif (menu == "0"):
        print("Saindo do programa...")
        break
    else:
        print("Você digitou uma opção inválida!")
    
    input("Tecle Enter para continuar!")
    
