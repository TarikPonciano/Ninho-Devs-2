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
    [()]
    
    if (resultado == []):
        return None
    else:
        return resultado[0]
    
    

            
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

        # Pedir a quantidade de unidades compradas daquele produto
        #   - Verificar se o estoque é suficiente
        
        # Criar a venda (Inserir Venda)
        # Criar os registros de venda dos produtos (Inserir na tabela itens)
        # Atualizar a quantidade de produto na tabela produto
        # Atualiza a compra com o Valor Total da compra    
        # Criar nota fiscal simples com produto, quantidade, preço e valor total    
        pass
    elif (op == "0"):
        print("Saindo do Programa...")
        break
    else:
        print("Você digitou uma operação inválida.")
        
    input("Tecle Enter para continuar!")
    


