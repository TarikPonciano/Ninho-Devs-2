#Crie uma classe conta que possui os atributos numero, titular, saldo e limite.
class Conta:
    def __init__(self, numero, titular, saldo=0, limite=1000):
        self.numero = numero
        self.titular = titular
        self.__senha = "Abacate"
        if saldo == None:
            self.saldo = 0
        else:
            self.saldo = saldo
        if limite == None:
            self.limite = 1000
        else:
            self.limite = limite
    def mostrar_informacoes(self):
        senha = input("Digite a senha de acesso: ")
        if senha == self.__senha:
            print("---------------------")
            for key in self.__dict__:
                print(f"{key.capitalize()} - {self.__dict__[key]}")
        else:
            print("Acesso Negado!")        
    def depositar(self, deposito):
        if deposito.isdecimal():
            deposito = float(deposito)
        else:
            print("Não foi possível compreender o valor informado.")
            return "ERRO" 
            
        if deposito <= 0:
            print("Valor de depósito inválido! Insira um número válido!")
            return "ERRO"
        else:
            self.saldo += deposito
            return "DEU CERTO"
            
    def sacar(self, saque):
        if saque <= 0:
            print("Valor de saque inválido! Insira um número válido!")
        else:
            if saque > self.saldo:
                print("Valor de saque inválido! Saldo insuficiente!")
            else:
                self.saldo -= saque
                
    def get_saldo(self):
        return self.saldo
    def set_saldo(self,novoSaldo):
        self.saldo = novoSaldo
        
    def get_senha(self):
        return self.__senha
#Faça um programa que instancia uma conta e faz as operações saque, depósito e ver informações da conta

# conta1 = Conta(123, "Marquinhos", 5000, 3000)


# while(True):
    
#     print(f'''
#           Menu:
          
#           1. Ver Informações
#           2. Depositar
#           3. Sacar
#           0. Sair
#           ''')
    
#     op = input("Escolha uma das opções: ")
    
#     match op:
#         case "1":
#             conta1.mostrar_informacoes()
#         case "2":
#             resposta = ""
#             while resposta != "DEU CERTO":
#                 deposito = input("Digite quanto de seja depositar: ")
                
#                 resposta = conta1.depositar(deposito)
                
#                 print(f"O novo saldo da conta é: R${conta1.saldo:.2f}")
            
#         case "3":
#             saque = float(input("Digite quanto de seja sacar: "))
            
#             conta1.sacar(saque)
            
#             print(f"O novo saldo da conta é: R${conta1.saldo:.2f}")
#         case "0":
#             print("Saindo do programa...")
#             break
#         case default:
#             print("Opção inválida!")
            
#     input("Digite Enter para continuar!")

class ContaSimples:
    def __init__ (self, titular, saldo):
        self.__titular = titular
        self.__saldo = saldo
        
    def get_saldo(self):
        return self.__saldo 
    def set_saldo(self, novoSaldo):
        self.__saldo = novoSaldo
        
    def get_titular(self):
        return self.__titular
    def set_titular(self, novoTitular):
        self.__titular = novoTitular
    
    def mostrar_informacoes(self):
        print("////////////////////////////")
        print("Titular:", self.__titular)
        print(f"Saldo: R${self.__saldo:.2f}")      
