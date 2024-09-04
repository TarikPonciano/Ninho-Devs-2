from conexao import Conexao

# Função para visualizar produtos
def ver_produtos(conexao):
    produtos = conexao.consultar("SELECT * FROM depositobomjesus.produtos")
    print("ID | Nome                | Preço     | Estoque")
    print("-----------------------------------------------")
    for produto in produtos:
        print(f"{produto[0]:<3} | {produto[1]:<20} | {produto[2]:<9} | {produto[3]}")
    print()

# Função para inserir novos produtos
def inserir_produto(conexao):
    nome_produto = input("Digite o nome do produto: ")
    preco_produto = float(input("Digite o preço do produto: "))
    estoque_produto = int(input("Digite a quantidade em estoque: "))
    
    sql = "INSERT INTO depositobomjesus.produtos (nome_produto, preco_produto, estoque_produto) VALUES (%s, %s, %s)"
    parametros = (nome_produto, preco_produto, estoque_produto)
    
    conexao.manipularComParametros(sql, parametros)
    print(f"Produto '{nome_produto}' inserido com sucesso!\n")

# Função para registrar venda
def vender_produto(conexao):
    id_produto = int(input("Digite o ID do produto que deseja vender: "))
    quantidade = int(input("Digite a quantidade que deseja vender: "))
    
    # Buscar informações do produto
    produto = conexao.consultarComParametros("SELECT nome_produto, preco_produto, estoque_produto FROM depositobomjesus.produtos WHERE id_produto = %s", (id_produto,))
    
    if not produto:
        print("Produto não encontrado!\n")
        return
    
    nome_produto, preco_produto, estoque_produto = produto[0]
    
    if quantidade > estoque_produto:
        print(f"Quantidade em estoque insuficiente! Estoque atual: {estoque_produto}\n")
        return
    
    valor_total = preco_produto * quantidade
    novo_estoque = estoque_produto - quantidade
    
    # Atualizar estoque
    conexao.manipularComParametros("UPDATE depositobomjesus.produtos SET estoque_produto = %s WHERE id_produto = %s", (novo_estoque, id_produto))
    
    # Registrar venda
    conexao.manipularComParametros("INSERT INTO depositobomjesus.vendas (valor_total_venda) VALUES (%s)", (valor_total,))
    
    print(f"Venda registrada com sucesso! Produto: {nome_produto}, Quantidade: {quantidade}, Valor total: R${valor_total:.2f}\n")

# Função principal para o menu
def main():
    conexaoBD = Conexao("localhost", "root", "mysql", "depositobomjesus")
    
    while True:
        print("Menu:")
        print("1. Ver produtos")
        print("2. Inserir produto")
        print("3. Vender produto")
        print("4. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            ver_produtos(conexaoBD)
        elif opcao == "2":
            inserir_produto(conexaoBD)
        elif opcao == "3":
            vender_produto(conexaoBD)
        elif opcao == "4":
            print("Saindo...")
            break
        else:
            print("Opção inválida! Tente novamente.\n")

if __name__ == "__main__":
    main()
