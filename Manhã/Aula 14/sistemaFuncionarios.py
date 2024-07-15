# funcionario = {
#     "Matrícula": 20,
#     "Nome": "Maicão",
#     "Cargo": "Assistente de Vendas",
#     "Salário": 3000
# }

dicionarioFuncionarios = {
    "001": {"Matricula": "001", "Nome": "Jessica", "Cargo": "Vendedor", "Salário": 5000},
    "002": {"Matricula": "002", "Nome": "João", "Cargo": "Gerente", "Salário": 8000},
    "003": {"Matricula": "003", "Nome": "Maria", "Cargo": "Analista", "Salário": 6000},
    "004": {"Matricula": "004", "Nome": "Pedro", "Cargo": "Assistente", "Salário": 4000},
    "005": {"Matricula": "005", "Nome": "Ana", "Cargo": "Estagiário", "Salário": 2000}
    
}

while True:
    funcionario = {}
    
    matricula = input("Digite a matricula do funcionário (para sair digite 'sair'): ")
    
    if (matricula == "sair"):
        break
    
    nome = input("Digite o nome do funcionário: ")
    cargo = input("Digite o cargo do funcionário: ")
    salario = float(input("Digite o salário: R$"))
    
    
    
    funcionario["Matricula"] = matricula
    funcionario["Nome"] = nome
    funcionario["Cargo"] = cargo
    funcionario["Salário"] = salario
    
    dicionarioFuncionarios[matricula] = funcionario

print("Matrícula | Nome | Cargo | Salário")


for matricula in dicionarioFuncionarios:
    funcionarioDaVez = dicionarioFuncionarios[matricula] # {"Nome": "Marcos", "Salário": 3000}
    
    print(f"{funcionarioDaVez['Matricula']} | {funcionarioDaVez['Nome']} | {funcionarioDaVez['Cargo']} | R$ {funcionarioDaVez['Salário']:.2f}")
    
maiorFuncionario = None
menorFuncionario = None   

for matricula in dicionarioFuncionarios:
    funcionarioDaVez = dicionarioFuncionarios[matricula] 
    
    if (maiorFuncionario == None):
        maiorFuncionario = funcionarioDaVez
    
    if (menorFuncionario == None):
        menorFuncionario = funcionarioDaVez
    
    if funcionarioDaVez["Salário"] > maiorFuncionario["Salário"]:
        maiorFuncionario = funcionarioDaVez
    
    if funcionarioDaVez["Salário"] < menorFuncionario["Salário"]:
        menorFuncionario = funcionarioDaVez
        
    

print(f'''
      
Funcionário com Maior Salário:

{maiorFuncionario["Matricula"]} | {maiorFuncionario["Nome"]} | {maiorFuncionario["Cargo"]} | {maiorFuncionario["Salário"]}

Funcionário com Menor Salário:

{menorFuncionario["Matricula"]} | {menorFuncionario["Nome"]} | {menorFuncionario["Cargo"]} | {menorFuncionario["Salário"]}
''')

while True:
    print("----- Remoção de Funcionários -----")
    
    for matricula in dicionarioFuncionarios:
        funcionarioDaVez = dicionarioFuncionarios[matricula]
        
        print(f"{funcionarioDaVez['Matricula']} | {funcionarioDaVez['Nome']}")
    
    matricula = input("Digite a matricula do funcionário a ser removido: ")
    
    if (matricula == "0"):
        break
    
    if matricula in dicionarioFuncionarios:
    
        del dicionarioFuncionarios[matricula]
    else:
        print("Digite uma matrícula válida!")




