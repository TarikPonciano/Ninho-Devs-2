import MenuUsuario

while True:
    print('''
          
          1. Gerenciar Usuarios
          2. Gerenciar Funcionarios''')
    
    op = input("Digite")
    
    if op == "1":
        MenuUsuario.verMenuUsuario()           
            
    elif op == "2":
        pass
    else:
        break