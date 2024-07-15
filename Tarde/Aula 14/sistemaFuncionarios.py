# funcionario = {
#     "Matricula": "001",
#     "Nome": "Josias",
#     "Cargo": "Gerente",
#     "Salário": 5000
# }

# listaFuncionarios = []
dicionarioFuncionarios = {
    "001": {"Matricula": "001", "Nome": "Jorge", "Cargo": "Vendedor", "Salário": 5000},
    "002": {"Matricula": "002", "Nome": "Maria", "Cargo": "Analista", "Salário": 6000},
    "003": {"Matricula": "003", "Nome": "Pedro", "Cargo": "Gerente", "Salário": 8000},
    "004": {"Matricula": "004", "Nome": "Ana", "Cargo": "Assistente", "Salário": 4500},
    "005": {"Matricula": "005", "Nome": "Lucas", "Cargo": "Programador", "Salário": 5500}
}

#{
# "001": {"Nome": "Cleiton", "Matricula": "001"},
# "002": {"Nome": "Jessica", "Matricula": "002"}
# }

while True:
    
    funcionario = {} 
    
    matricula = input("Digite a matrícula do funcionário ('sair' para encerrar): ")
    
    if (matricula == "sair"):
        break
    
    nome = input("Digite o nome do funcionário: ")
    cargo = input("Digite o cargo do funcionário: ")
    salario = float(input("Digite o salário do funcionário: R$"))
    
    # gerarMatricula = str(len(dicionarioFuncionarios)+1)
    # if len(gerarMatricula) == 1:
    #     realMatricula = "00"+gerarMatricula
    # elif(len(gerarMatricula) == 2):
    #     realMatricula = "0"+gerarMatricula
    # else:
    #     realMatricula = gerarMatricula
        
    # if len(gerarMatricula) <3:
    #     realMatricula = "0" *(3-len(gerarMatricula)) 
    #     realMatricula += gerarMatricula 
    # else:
    #     realMatricula = gerarMatricula
           
    # funcionario["Matricula"] = realMatricula
    funcionario["Matricula"] = matricula
    funcionario["Nome"] = nome
    funcionario["Cargo"] = cargo
    funcionario["Salário"] = salario
    
    # listaFuncionarios.append(funcionario)
    dicionarioFuncionarios[matricula] = funcionario

    # print(listaFuncionarios)
    # print(dicionarioFuncionarios)
    
for matricula in dicionarioFuncionarios:
    
    funcionarioDaVez = dicionarioFuncionarios[matricula]
    
    print(f"{funcionarioDaVez["Matricula"]} | {funcionarioDaVez["Nome"]} | {funcionarioDaVez["Cargo"]} | R$ {funcionarioDaVez["Salário"]}")
    

maiorFuncionario = None
menorFuncionario = None

for matricula in dicionarioFuncionarios:
    
    funcionarioDaVez = dicionarioFuncionarios[matricula]
    
    if maiorFuncionario == None:
        maiorFuncionario = funcionarioDaVez
    
    if menorFuncionario == None:
        menorFuncionario = funcionarioDaVez
        
    if funcionarioDaVez["Salário"] > maiorFuncionario["Salário"]:
        maiorFuncionario = funcionarioDaVez
        
    if funcionarioDaVez["Salário"] < menorFuncionario["Salário"]:
        menorFuncionario = funcionarioDaVez
        
        
print(f'''
Funcionário com Maior Salário:

Nome: {maiorFuncionario["Nome"]}
Cargo: {maiorFuncionario["Cargo"]}
Salário: R$ {maiorFuncionario["Salário"]:.2f}

Funcionário com Menor Salário:

Nome: {menorFuncionario["Nome"]}
Cargo: {menorFuncionario["Cargo"]}
Salário: R$ {menorFuncionario["Salário"]:.2f}
      
      ''')


while True:
    print("----- Remoção de Funcionários -----")
    for matricula in dicionarioFuncionarios:
        funcionarioDaVez = dicionarioFuncionarios[matricula]
        
        print(f"{funcionarioDaVez["Matricula"]} | {funcionarioDaVez["Nome"]} | {funcionarioDaVez["Cargo"]} | R$ {funcionarioDaVez["Salário"]}")
    
    
    matricula = input("Digite uma matricula para remover um funcionário (0 para sair): ")
    
    if (matricula == "0"):
        break
    
    if matricula in dicionarioFuncionarios:
    
        del dicionarioFuncionarios[matricula]
    else:
        print("Matrícula inválida!")
        input("Enter para continuar")








