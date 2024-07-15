# 1. **Cadastro de Nomes**:
#    - **Questão**: Crie um programa que permita ao usuário cadastrar 5 nomes de pessoas em uma lista. Após o cadastro, exiba a lista de nomes na tela.
#    - **Dica**: Utilize um loop para coletar os nomes e armazená-los na lista.

# print("-----Exercicio 1-----")

# nomes = []

# while True:
#     nome = input("Digite um nome:")
#     if(nome == "sair"):
#         break
#     nomes.append(nome)


# for i in range(len(nomes)):
#     print(f"{i+1}. {nomes[i]}")
    
# contador = 1
# for n in nomes:
#     print(f"{contador}. {n}")
#     contador += 1
    
# for i,n in enumerate(nomes,start=1):
#     print(f"{i}. {n}")
    
    
    
# 2. **Gerenciamento de Tarefas Simples**:
#    - **Questão**: Crie um programa que gerencie uma lista de tarefas. Permita ao usuário adicionar até 10 tarefas com uma descrição simples (apenas texto). Após adicionar as tarefas, exiba a lista completa.
#    - **Dica**: Utilize o método `append()` para adicionar tarefas à lista.

# 3. **Média de Idades**:
#    - **Questão**: Crie um programa que solicite ao usuário as idades de 5 pessoas e as armazene em uma lista. Calcule e exiba a média das idades.
#    - **Dica**: Utilize a função `sum()` e `len()` para calcular a média.

idades = []

# for i in range(5):
#     idade = input("Digite uma idade:")
#     if idade.isdigit():
#         idades.append(int(idade))
#     else:
#         print("Digite um número inteiro.")

for i in range(5):
    idade = int(input("Digite uma idade:"))
    idades.append(idade)
    
# soma = 0
# qtdIdades = 0

# for idade in idades:
#     soma += idade
#     qtdIdades += 1
    
soma = sum(idades)
qtdIdades = len(idades)
media = soma / qtdIdades
print("A média de idade é:", media)
    


# 4. **Lista de Compras Simples**:
#    - **Questão**: Crie um programa que permita ao usuário criar uma lista de compras contendo até 10 itens. Após a inserção dos itens, exiba a lista de compras.
#    - **Dica**: Utilize um loop para coletar os itens e armazená-los na lista.

# 5. **Registro de Temperaturas Diárias**:
#    - **Questão**: Crie um programa que solicite ao usuário as temperaturas médias registradas durante uma semana (7 dias) e as armazene em uma lista. Calcule e exiba a temperatura média da semana, a temperatura mais alta e a mais baixa.
#    - **Dica**: Utilize as funções `sum()`, `max()` e `min()`.

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