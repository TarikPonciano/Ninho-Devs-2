from Conexao import Conexao

# Criar um menu de aplicação com as opções:
# 1. Ver Produtos
# 2. Cadastrar Venda
# 0. Sair

conexaoBD = Conexao("localhost", "root", "mysql", "jomart")

def buscarProduto(id):
    pass

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
        idProduto = int(input("Digite o id do produto: "))
        #   - Validar se o produto existe no banco (Buscar produto)
        produto = buscarProduto(idProduto)
        # Pedir a quantidade de cada produto
        #   - Validar se a quantidade é possível
        # Criar a venda
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
    
