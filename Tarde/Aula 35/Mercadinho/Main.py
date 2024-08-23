from Conexao import Conexao

conexaoBD = Conexao("localhost", "root", "mysql", "mercadojoa")

def verProdutos():
    
    produtos = conexaoBD.consultar("SELECT * FROM produtos")
    
    print(f"ID |{' ' * (15-2)}Nome{' ' * (15-2)}| Preço (R$) | Estoque")
    for produto in produtos:
        espacoNome = ' ' * round(15-(len(produto[1])/2))
        print(f"{produto[0]} |{espacoNome}{produto[1]}{espacoNome}| {produto[2]} | {produto[3]}")
        
        
        
        
        

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
        
        # Pedir o id dos produtos da compra
        #   - Verifica se o produto existe
        
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
    


