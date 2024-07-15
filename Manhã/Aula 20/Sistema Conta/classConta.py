class Conta:
    def __init__(self, numero, titular, saldo = 0, limite = 1000):
        self.numero = numero
        self.titular = titular
        self.__senha = "Abacate"
        if saldo == None:
            self._saldo = 0
        else:
            self._saldo = saldo
        
        if limite == None:
            self.limite = 1000
        else:
            self.limite = limite
    
    def __mostrar_informacoes(self):
        for key in self.__dict__:
            print(f"{key.capitalize()} - {self.__dict__[key]}")
            
    def sacar(self, saque):
        
        if saque > self._saldo:
            print("Saque negado! Saldo insuficiente!")
        else:
            self._saldo -= saque
    def depositar(self,deposito):
        self._saldo += deposito
        
    def verSaldo(self):
        return self._saldo
    
    def acessar_conta(self,senha):
        
        if senha == self.__senha:
            self.__mostrar_informacoes()
        else:
            print("ACESSO NEGADO!")
    
# conta1 = Conta(120, "Josias", 3000, 2000)

# conta1.acessar_conta("Abacate")

# print(f'''
      
#       Menu:
      
#       1. Verificar Saldo
#       2. Depositar
#       3. Sacar
#       0. Sair
      
#       ''')

# op = input("Digite uma opção: ")

# if op == "1":
#     print(f"Saldo: R$ {conta1.verSaldo():.2f}")
# elif op == "2":
#     deposito = float(input("Digite a quantidade do depósito: "))
    
#     conta1.depositar(deposito)
#     print(f"Novo Saldo: R$ {conta1.verSaldo():.2f}")
# elif op =="3":
#     saque = float(input("Digite a quantidade do saque:"))
#     conta1.sacar(saque)
    
#     print(f"Novo Saldo: R$ {conta1.verSaldo():.2f}")

class ContaSimples:
    def __init__(self, titular, saldo):
        self._titular = titular
        self._saldo = saldo
    
    def get_saldo(self):
        return self._saldo
    def set_saldo(self, saldo):
        self._saldo = saldo
    
    def get_titular(self):
        return self._titular
    def set_titular(self, titular):
        self._titular = titular
    
        