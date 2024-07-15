rep = int(input("Quantos nomes deseja digitar?"))

for i in range(rep):
    nome = input("Digite um nome:")
    if(nome[0] == "A" or nome[0] == "a"):
        print("Olá,", nome)