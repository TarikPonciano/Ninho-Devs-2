# 1. **Cadastro de Nomes**:
#    - **Questão**: Crie um programa que permita ao usuário cadastrar 5 nomes de pessoas em uma lista. Após o cadastro, exiba a lista de nomes na tela.
#    - **Dica**: Utilize um loop para coletar os nomes e armazená-los na lista.

# 2. **Gerenciamento de Tarefas Simples**:
#    - **Questão**: Crie um programa que gerencie uma lista de tarefas. Permita ao usuário adicionar até 10 tarefas com uma descrição simples (apenas texto). Após adicionar as tarefas, exiba a lista completa.
#    - **Dica**: Utilize o método `append()` para adicionar tarefas à lista.

# 3. **Média de Idades**:
#    - **Questão**: Crie um programa que solicite ao usuário as idades de 5 pessoas e as armazene em uma lista. Calcule e exiba a média das idades.
#    - **Dica**: Utilize a função `sum()` e `len()` para calcular a média.

# 4. **Lista de Compras Simples**:
#    - **Questão**: Crie um programa que permita ao usuário criar uma lista de compras contendo até 10 itens. Após a inserção dos itens, exiba a lista de compras.

# O programa deverá conter o seguinte cardápio:
# mensagem = """
# Olá!

# Bem-vindo à nossa lanchonete. Aqui está o nosso menu:

# | Código do Produto | Nome               | Preço (R$) |
# |-------------------|--------------------|------------|
# |     001           | Cheeseburger       | 12.50      |
# |     002           | Batata Frita       | 8.00       |
# |     003           | Milkshake de Morango | 15.00     |
# |     004           | Sanduíche de Frango   | 10.00     |
# |     005           | Refrigerante       | 5.00       |

# Obrigado por escolher a nossa lanchonete!
# """

#Ao final calcule o preço total do pedido do cliente.
#    - **Dica**: Utilize um loop para coletar os itens e armazená-los na lista.

def exercicio4():
    
    listaProdutos = []
    
    for i in range(5):
        produto = input("Digite o produto que deseja comprar:")
        listaProdutos.append(produto)
        
    # for numero,nome in enumerate(listaProdutos):
    #     print(f"{numero+1}. {nome}")
    
    for i in range(len(listaProdutos)):
        print(f"{i}. {listaProdutos[i]}")
        
    
def exercicio4Modificado():
    
    listaProduto = []
    
    for i in range(5):
        print('''
| Código do Produto | Nome               | Preço (R$) |
|-------------------|--------------------|------------|
|     001           | Cheeseburger       | 12.50      |
|     002           | Batata Frita       | 8.00       |
|     003           | Milkshake de Morango | 15.00     |
|     004           | Sanduíche de Frango   | 10.00     |
|     005           | Refrigerante       | 5.00       |
              ''')
        codigo = input("Digite o código do produto desejado: ")
        listaProduto.append(codigo)
        print(listaProduto)
    
    listaPrecos = []
    
    listaNomes = []
    
    for cod in listaProduto:
        if (cod == "001"):
            listaPrecos.append(12.5)
            listaNomes.append("Cheeseburger")
        elif(cod=="002"):
            listaPrecos.append(8)
            listaNomes.append("Batata Frita")
        elif(cod=="003"):
            listaPrecos.append(15)
            listaNomes.append("MilkShake")
        elif(cod=="004"):
            listaPrecos.append(10)
            listaNomes.append("Sanduíche de Frango")
        elif(cod=="005"):
            listaPrecos.append(5)
            listaNomes.append("Refrigerante")
        else:
            listaPrecos.append(0)
            listaNomes.append("Produto Inexistente")
    
    print("Nota Fiscal:")
    for i in range(len(listaNomes)):
        print(f"{listaNomes[i]} - R$ {listaPrecos[i]}")
        
    print("R$", sum(listaPrecos))

# 5. **Registro de Temperaturas Diárias**:
#    - **Questão**: Crie um programa que solicite ao usuário as temperaturas médias registradas durante uma semana (7 dias) e as armazene em uma lista. Calcule e exiba a temperatura média da semana, a temperatura mais alta e a mais baixa.
#    - **Dica**: Utilize as funções `sum()`, `max()` e `min()`.

def exercicio5():
    diasDaSemana = ("Domingo", "Segunda", "Terça","Quarta","Quinta","Sexta", "Sábado")
    temperaturas = []
    
    for dia in diasDaSemana:
        
        temperatura = float(input(f"Digite a temperatura de {dia}: "))
        
        temperaturas.append(temperatura)
    
    maior = temperaturas[0]
    menor = temperaturas[0]
    
    for i in range(len(diasDaSemana)):
        if (temperaturas[i] > maior):
            maior = temperaturas[i]
            maiorNome = diasDaSemana[i]
        
        if (temperaturas[i] < menor):
            menor = temperaturas[i]
            menorNome = diasDaSemana[i]
    
    media = sum(temperaturas)/len(temperaturas)
    
    print(f'''
    Máxima da Semana: {maiorNome} - {maior}°C 
    Mínima da Semana: {menorNome} - {menor}°C
    Média da Semana: {media}°C
          ''')
    
    # maior = max(temperaturas)
    # menor = min(temperaturas)
    
    # maiorNome = diasDaSemana[temperaturas.index(maior)]
    # menorNome = diasDaSemana[temperaturas.index(menor)]
    
    print("Histórico de Temperatura:")
    for i in range(len(diasDaSemana)):
        
        print(f"{diasDaSemana[i]}: {temperaturas[i]}")
        
        
    
    
        

# 6. **Pontuações de Jogadores**:
#    - **Questão**: Crie um programa que registre as pontuações de 5 jogadores em um jogo. Permita ao usuário adicionar as pontuações (números inteiros) a uma lista. Após a inserção, exiba a pontuação média, a maior e a menor pontuação.
#    - **Dica**: Utilize listas para armazenar as pontuações e as funções `sum()`, `max()` e `min()` para análise.

# 7. **Gerenciamento de Contatos Simples**:
#    - **Questão**: Crie um programa que permita ao usuário gerenciar uma lista de números de telefone. Permita ao usuário adicionar até 10 números de telefone à lista. Após a inserção, exiba todos os números de telefone cadastrados.
#    - **Dica**: Utilize um loop para coletar os números de telefone e armazená-los na lista.

# 8. **Controle de Inventário**:
#    - **Questão**: Crie um programa que permita ao usuário registrar a quantidade em estoque de 5 produtos diferentes. Armazene as quantidades em uma lista. Após a inserção, exiba o estoque total e a média de itens por produto.
#    - **Dica**: Utilize as funções `sum()` e `len()` para calcular o estoque total e a média.

# 9. **Análise de Vendas Diárias**:
#    - **Questão**: Crie um programa que solicite ao usuário a quantidade de produtos vendidos em cada um dos 7 dias da semana e armazene essas quantidades em uma lista. Calcule e exiba o total de vendas na semana, a média diária de vendas e o dia com mais vendas.
#    - **Dica**: Utilize listas e funções de agregação como `sum()`, `len()` e `max()`.

# 10. **Pesquisa de Satisfação**:
#     - **Questão**: Crie um programa que colete as notas de satisfação de 10 clientes, onde cada nota é um número de 1 a 5. Armazene essas notas em uma lista. Calcule e exiba a média das notas e a quantidade de cada nota recebida.
#     - **Dica**: Utilize a função `count()` para contar a ocorrência de cada nota e `sum()` para calcular a média.