from Conexao import Conexao

# conexaoBD = Conexao()

def verMenuUsuario():
    while True:
        print('''
              1. Ver Usuarios
              2. Alterar Usuarios
              ''')
        
        op = input()
        
        if op=="1":
            verUsuarios()
            
def verUsuarios():
    print("Vendo usuarios!")
    
