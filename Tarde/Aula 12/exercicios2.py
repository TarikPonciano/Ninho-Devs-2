#Questão 1: Crie um programa que recebe 5 nomes. Imprima na tela, os nomes que começam com vogal e os nomes que começam com consoante. 
#Ex: Vogal - Ana Anabelle Arlete
#    Consoante - Marcos Mario Mauricio
def exercicio1():
    listaNomes = []
    vogais = ("A", "E", "I", "O", "U")

    for i in range(5):
        nome = input("Digite um nome:")
        listaNomes.append(nome)
        
    nomeComVogal = []
    nomeComConsoante = []
    for nome in listaNomes:
        if nome[0].upper() in vogais:
            nomeComVogal.append(nome)
        else:
            nomeComConsoante.append(nome)
            
    print("Começa com Vogal: ",nomeComVogal)
    
    print("Começa com Consoante: ", nomeComConsoante)



#Questão 2: Crie um programa que pede a temperatura de cada dia da semana (Domingo, Segunda... Sábado). Ao final, imprima na tela um relatório com a temperatura de cada dia e imprima que dia teve a maior temperatura e que dia teve a menor temperatura.

def exercicio2():
    diasDaSemanas = ("Domingo", "Segunda", "Terça", "Quarta")
    listaTemperaturas = []
    
    for dia in diasDaSemanas:
        temperatura = float(input(f"Digite a temperatura de {dia}: "))
        listaTemperaturas.append(temperatura)
        
    tempMaxima = listaTemperaturas[0]
    tempMinima = listaTemperaturas[0]
    
    diaMaxima = diasDaSemanas[0]
    diaMinima = diasDaSemanas[0]
    
    for i in range(len(diasDaSemanas)):
        print(f"{diasDaSemanas[i]} - {listaTemperaturas[i]}°C")
        
        if (listaTemperaturas[i] > tempMaxima):
            tempMaxima = listaTemperaturas[i]
            diaMaxima = diasDaSemanas[i]

        if (listaTemperaturas[i] < tempMinima):
            tempMinima = listaTemperaturas[i]
            diaMinima = diasDaSemanas[i]
            
    print(f'''
    Mínima - {diaMinima} - {tempMinima}°C
    Máxima - {diaMaxima} - {tempMaxima}°C      
          
          ''')
    
    # maxima = max(listaTemperaturas)
    # minima = min(listaTemperaturas)
    # diaMaxima = diasDaSemanas[listaTemperaturas.index(maxima)]
    # diaMinima = diasDaSemanas[listaTemperaturas.index(minima)]
        
    

#Questão 3: Crie um programa que utiliza o seguinte cardápio:
# | Código do Produto | Nome               | Preço (R$) |
# |-------------------|--------------------|------------|
# |     001           | Cheeseburger       | 12.50      |
# |     002           | Batata Frita       | 8.00       |
# |     003           | Milkshake de Morango | 15.00     |
# |     004           | Sanduíche de Frango   | 10.00     |
# |     005           | Refrigerante       | 5.00       |

# Permita que o usuário escreva o código do produto desejado. Você deve receber código até o usuário digitar 'Sair'. Ao terminar o processo de compra, exiba na tela os produtos comprados e o valor total da compra.

def exercicio3():
    
    listaCodigos = []
    
    print('''
Cardápio:
    
| Código do Produto | Nome               | Preço (R$) |
|-------------------|--------------------|------------|
|     001           | Cheeseburger       | 12.50      |
|     002           | Batata Frita       | 8.00       |
|     003           | Milkshake de Morango | 15.00     |
|     004           | Sanduíche de Frango   | 10.00     |
|     005           | Refrigerante       | 5.00       |
          ''')
    
    while (True):
        op = input("Escolha um produto do cardápio e digite seu código: ")
        
        if (op == "Sair"):
            break
        elif (op in ("001", "002", "003", "004", "005")):
            listaCodigos.append(op)
        else:
            print("Código inválido. Tente novamente.")
            
    print(listaCodigos)
    
    listaNomes = []
    listaPrecos = []
    
    for codigo in listaCodigos:
        
        if codigo == "001":
            listaNomes.append("Cheeseburguer")
            listaPrecos.append(12.5)
        elif codigo == "002":
            listaNomes.append("Batata Frita")
            listaPrecos.append(8.0)
        elif codigo == "003":
            listaNomes.append("MilkShake")
            listaPrecos.append(15.0)
        elif codigo == "004":
            listaNomes.append("Sanduiche de Frango")
            listaPrecos.append(10.0)
        elif codigo == "005":
            listaNomes.append("Refrigerante")
            listaPrecos.append(5.0)
        else:
            listaNomes.append("Produto Inexistente")
            listaPrecos.append(0)
    print("Carrinho de Compras: ")        
    
    
    verificado = []
    
    for i in range(len(listaNomes)):
        nome = listaNomes[i]
        quantidade = listaNomes.count(nome)
        
        if nome not in verificado:
            print(f"{nome} - {quantidade} - R$ {listaPrecos[i] * quantidade}")
        
            verificado.append(nome)
            
            
    for i in range(len(listaNomes)):
        
        print(listaNomes[i], listaPrecos[i])
        
        
    print("Total da sua compra é: R$", sum(listaPrecos))
    
            
#Questão 4: Receba o nome e nota de 10 alunos de uma turma. Imprima na tela, a média da turma, a maior nota e quem tirou a maior nota, a menor nota e quem tirou a menor nota e por fim os alunos aprovados e os alunos reprovados. Aprovado >= 5 e Reprovado <5