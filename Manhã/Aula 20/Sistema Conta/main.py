#Utilizando a class Conta dos slides, crie os atributos dessa class como privado e os métodos get e set para cada atributo. Instancie 3 objetos da classe conta e faça as operações:
# 1. Criar os objetos
# 2. Depositar quantias aleatorias em cada conta
# 3. Sacar quantias aleatorias em cada conta
# 4. Modifique o titular de cada conta
# 5. Imprimir na tela o titular e saldo final da conta

from classConta import ContaSimples
import random

conta1 = ContaSimples("Joaquim", 5000)
conta2 = ContaSimples("Manoel", 6000)
conta3 = ContaSimples("Vanessa", 8000)

listaContas = [conta1,conta2,conta3]


for conta in listaContas:
    
    deposito = random.randint(0, 5000)
    
    conta.set_saldo(conta.get_saldo() + deposito)

    print(f"A conta do titular {conta.get_titular()} recebeu um depósito de R$ {deposito:.2f}. Novo saldo é de: R$ {conta.get_saldo():.2f}")
    
for conta in listaContas:
    
    saque = random.randint(0, conta.get_saldo())
    
    conta.set_saldo(conta.get_saldo() - saque)

    print(f"A conta do titular {conta.get_titular()} teve um saque de R$ {saque:.2f}. Novo saldo é de: R$ {conta.get_saldo():.2f}")


maior = listaContas[0]
conta1.set_titular("Marquinhos")  
for conta in listaContas:
    
    print(f'''
    Titular: {conta.get_titular()}
    Saldo: R$ {conta.get_saldo():.2f}      
          ''')
    
    if conta.get_saldo() > maior.get_saldo():
        maior = conta    


print(f"Maior saldo pertece ao {maior.get_titular()} e tem o valor de R${maior.get_saldo():.2f}")


