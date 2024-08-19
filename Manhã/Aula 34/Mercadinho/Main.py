from Conexao import Conexao

# Criar um menu de aplicação com as opções:
# 1. Ver Produtos
# 2. Cadastrar Venda
# 0. Sair

conexaoBD = Conexao("localhost", "root", "mysql", "jomart")

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
        pass
    elif (menu == "0"):
        print("Saindo do programa...")
        break
    else:
        print("Você digitou uma opção inválida!")
    
    input("Tecle Enter para continuar!")
    
