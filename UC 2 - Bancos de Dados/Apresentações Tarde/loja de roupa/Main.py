from Conexao import Conexao

# Configurar credenciais de conexão do banco
conexaoBD = Conexao("localhost", "root", "mysql", "SilvaStyle")

def menu():
    print("\nMenu:")
    print("0. Sair")
    print("1. Ver Clientes")
    print("2. Criar Cliente")
    print("3. Atualizar Cliente")
    print("4. Remover Cliente")
    print("5. Ver Produtos")
    print("6. Criar Produto")
    print("7. Atualizar Produto")
    print("8. Remover Produto")
    print("9. Cadastrar Venda")
    print("10. Ver Vendas")
    escolha = input("Escolha uma opção: ")
    return escolha

def ver_clientes():
    resultado = conexaoBD.consultar("SELECT * FROM cliente")
    if resultado:
        print("\nClientes:")
        for row in resultado:
            print(f"ID:{row[0]} | Nome:{row[1]} | Telefone:{row[2]} | CPF:{row[3]}")
    else:
        print("Nenhum cliente encontrado.")

def criar_cliente():
    nome = input("Nome do cliente: ")
    telefone = input("Telefone do cliente: ")
    cpf = input("CPF do cliente: ")
    sql = "INSERT INTO cliente (nome, telefone, cpf) VALUES (%s, %s, %s)"
    parametros = (nome, telefone, cpf)
    conexaoBD.manipularComParametros(sql, parametros)
    print("Cliente criado com sucesso.")

def atualizar_cliente():
    id_cliente = input("ID do cliente para atualizar: ")
    nome = input("Novo nome do cliente: ")
    telefone = input("Novo telefone do cliente: ")
    cpf = input("Novo CPF do cliente: ")
    sql = "UPDATE cliente SET nome = %s, telefone = %s, cpf = %s WHERE id_cliente = %s"
    parametros = (nome, telefone, cpf, id_cliente)
    conexaoBD.manipularComParametros(sql, parametros)
    print("Cliente atualizado com sucesso.")

def remover_cliente():
    id_cliente = input("ID do cliente para remover: ")
    sql = "DELETE FROM cliente WHERE id_cliente = %s"
    conexaoBD.manipularComParametros(sql, (id_cliente,))
    print("Cliente removido com sucesso.")

def ver_produtos():
    resultado = conexaoBD.consultar("SELECT * FROM produtos")
    if resultado:
        print("\nProdutos:")
        for row in resultado:
            print(f"ID:{row[0]} | Nome:{row[1]} | Estoque:{row[2]} | Preço:R${row[3]}")
    else:
        print("Nenhum produto encontrado.")

def criar_produto():
    nome = input("Nome do produto: ")
    estoque = input("Estoque do produto: ")
    preco = input("Preço do produto: ")
    sql = "INSERT INTO produtos (nome, estoque, preco) VALUES (%s, %s, %s)"
    parametros = (nome, estoque, preco)
    conexaoBD.manipularComParametros(sql, parametros)
    print("Produto criado com sucesso.")

def atualizar_produto():
    id_produto = input("ID do produto para atualizar: ")
    nome = input("Novo nome do produto: ")
    estoque = input("Novo estoque do produto: ")
    preco = input("Novo preço do produto: ")
    sql = "UPDATE produtos SET nome = %s, estoque = %s, preco = %s WHERE id_produto = %s"
    parametros = (nome, estoque, preco, id_produto)
    conexaoBD.manipularComParametros(sql, parametros)
    print("Produto atualizado com sucesso.")

def remover_produto():
    id_produto = input("ID do produto para remover: ")
    sql = "DELETE FROM produtos WHERE id_produto = %s"
    conexaoBD.manipularComParametros(sql, (id_produto,))
    print("Produto removido com sucesso.")

def cadastrar_venda():
    ver_produtos()
    id_produto = input("ID do produto: ")
    ver_clientes()
    id_cliente = input("ID do cliente: ")
    qntd = input("Quantidade: ")
    # Obter o preço do produto
    resultado = conexaoBD.consultarComParametros("SELECT preco FROM produtos WHERE id_produto = %s", (id_produto,))
    if resultado:
        preco = resultado[0][0]
        total = float(preco) * int(qntd)
        sql = "INSERT INTO compras (qntd, total, id_produto, id_cliente) VALUES (%s, %s, %s, %s)"
        parametros = (qntd, total, id_produto, id_cliente)
        conexaoBD.manipularComParametros(sql, parametros)
        print("Venda registrada com sucesso.")
    else:
        print("Produto não encontrado.")

def ver_vendas():
    resultado = conexaoBD.consultar("SELECT compras.id_compra, compras.qntd, compras.total, cliente.nome, produtos.nome FROM compras INNER JOIN cliente ON compras.id_cliente = cliente.id_cliente INNER JOIN produtos ON compras.id_produto = produtos.id_produto ")
    if resultado:
        print("\nVendas:")
        for row in resultado:
            print(f"Nome do Cliente:{row[3]} | ID da Compra:{row[0]} | Nome do Produto:{row[4]} | Quantidade de Compras:{row[1]} | Total:R${row[2]}")
    else:
        print("Nenhuma venda encontrada.")

def main():
    while True:
        escolha = menu()
        if escolha == "0":
            print("Saindo...")
            break
        elif escolha == "1":
            ver_clientes()
        elif escolha == "2":
            criar_cliente()
        elif escolha == "3":
            atualizar_cliente()
        elif escolha == "4":
            remover_cliente()
        elif escolha == "5":
            ver_produtos()
        elif escolha == "6":
            criar_produto()
        elif escolha == "7":
            atualizar_produto()
        elif escolha == "8":
            remover_produto()
        elif escolha == "9":
            cadastrar_venda()
        elif escolha == "10":
            ver_vendas()
        else:
            print("Escolha inválida.")
        input("Tecle Enter para continuar")

if __name__ == "__main__":
    main()
