# funcionario = {
#     "Nome": "José",
#     "Salário": 3000
# }

# print(funcionario)
# print("Nome:", funcionario["Nome"])
# print("Salário: R$", funcionario["Salário"])


# funcionario["Nome"] = "Maria"
# funcionario["Cargo"] = "Gerente"

# print(funcionario)

# del funcionario["Salário"]

funcionario = {}

funcionario["Nome"] = input("Digite o nome do funcionário:")

funcionario["Salário"] = float(input("Digite o salário do funcionário:"))

funcionario["Cargo"] = input("Digite o cargo do funcionário:")

print(funcionario)