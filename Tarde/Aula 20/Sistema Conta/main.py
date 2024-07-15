#Crie uma classe ContaSimples com os atributos titular e saldo. Ao criar os atributos crie da seguinte maneira:
#self.__titular
#self.__saldo

#Faça as seguintes operações:
#1. Instancie 3 objetos dessa classe ContaSimples
#2. Faça depositos aleatórios nas 3 contas
#3. Faça saques aleatórios nas 3 contas
#4. Faça uma alteração de titular em cada conta
#5. Exiba as informações de todas contas na tela

from classConta import ContaSimples
import random

conta1 = ContaSimples("Jonas", 4000)
conta2 = ContaSimples("Maria", 6000)
conta3 = ContaSimples("Zeca", 8000)

listaContas = [conta1, conta2, conta3]

for conta in listaContas:
    deposito = random.randint(0,5000)
    
    conta.set_saldo(conta.get_saldo() + deposito)
    print("------------------")
    print(f"A conta do titular {conta.get_titular()} recebeu um depósito de R$ {deposito:.2f}. Novo saldo: R$ {conta.get_saldo():.2f}")
    
for conta in listaContas:
    saque = random.randint(0,conta.get_saldo())
    
    conta.set_saldo(conta.get_saldo() - saque)
    
    print("------------------")
    print(f"A conta do titular {conta.get_titular()} efetuou um saque de R$ {saque:.2f}. Novo saldo: R$ {conta.get_saldo():.2f}")
    
sobrenomes = ["Lopes", "Dias", "Oliveira", "Arruda", "Maia", "Duboar", "Sampaio", "Sousa", "Sartre", "Vargas", "Barros", "Muller", "Marques", "Saldanha", "Sales", "João", "Holanda", "Nogueira"]

for conta in listaContas:
    conta.set_titular(conta.get_titular() + " " + random.choice(sobrenomes))
    print("Novo titular:", conta.get_titular())

maior = listaContas[0]
for conta in listaContas:
    conta.mostrar_informacoes()
    
    if conta.get_saldo() > maior.get_saldo():
        maior = conta
        
        
print("Conta com maior saldo:")
maior.mostrar_informacoes()
    