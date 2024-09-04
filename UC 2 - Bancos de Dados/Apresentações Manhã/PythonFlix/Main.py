import mysql.connector
from conexao import Conexao
from funcionario import Funcionario
from cliente import Cliente

conexaoBD = Conexao("localhost", "root", "mysql", "pythonflix")

def MENU():
    print('''Seja bem-vindo à Locadora PythonFlix
          01. Tela Funcionário
          02. Tela Cliente''')

    while True:
        escolha = input("Escolha uma interface:") 

        if escolha == "1":
            print("Olá funcionário!")
            Funcionario()
            break
        elif escolha == "2":
            Cliente()
            break
        
        else:
            print("Opção inválida! Tente novamente.")
if __name__ == "__main__":
    MENU()