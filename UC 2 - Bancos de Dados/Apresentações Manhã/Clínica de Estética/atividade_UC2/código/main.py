import mysql.connector

from Conexao import Conexao
from datetime import datetime

import menuCliente
import menuServico
import menuAtendimento


conexaoBD = Conexao("localhost", "root", "mysql", "estetica")

while True:
    print('''
    Bem-vindo(a) à CLÍNICA DE ESTÉTICA
    
    Menu Principal:

    1. CLIENTES
    2. SERVIÇOS
    3. ATENDIMENTOS
    0. SAIR
    ''')

    op = input("Digite a opção do menu desejada: ")

    if op == "1":
        
        menuCliente.menuCliente()

    elif op == "2":
        
        menuServico.menuServico()

    elif op == "3":

        menuAtendimento.menuAtendimento()
        
    elif op == "0":
        print("Encerrando programa...")
        break
    else:
        print("Você digitou uma opção inválida!")
    
    input("Tecle ENTER para continuar")
