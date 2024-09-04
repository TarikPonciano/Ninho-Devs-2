from Conexao import Conexao
from setup import Usuario
from luistools import tabber, centerprint, filler, cls, pause
from CypherFinal import CifraVigenere

def trimmer(s):
    if len(s) <= 1:
        return ""
    return s[1:-1]

def submit():
    #Envio
    cls()
    filler("*")
    centerprint("INTEL Feed V1.0")
    tabber("Teste - Insert a message for the main feed:")

    msg = input("Message: ")
    key = input("Solver Key: ")
    #Encriptação abaixo
    crpt = cifra.cifrar(msg, key)
    print("Cifrada:", crpt)
    decf = cifra.decifrar(crpt, key)
    print("Decifrada:", decf)
    database.manipularComParametro('''INSERT INTO SIS.FEED(id_client, CONTENT) VALUES('1', "%s")''', (crpt,))
    response = database.consultar("SELECT * FROM FEED ")
    for item in response:
        print(item[3])
        saida = trimmer(item[3])
        out = cifra.decifrar(saida,key)
        print(out)

def request():
    response = database.consultar("SELECT * FROM FEED ")
    for item in response:
        
        filler('=')
        print('')
        print(' ',"ID|     Entry Time      | Sender's ID")
        print(' ' ,item[0],'|',item[1],'|', item[2])
        print("")
    choice = input("Insert message's ID > ")
    show = database.consultarComParametros("SELECT * FROM SIS.FEED WHERE ID_ENTRY = %s", (choice,))
    print("")
    tabber("-Requested Message-")
    print("")
    print(' ',"ID|     Entry Time      | Sender's ID")
    print(' ' ,show[0][0],'|',show[0][1],'|', show[0][2])
    passe = input("Insert Message's Solving Key > ")
    mess = trimmer(show[0][3]) #aparo nas arestas
    mout = cifra.decifrar(mess, passe) #texto de saida decifrado
    print("Output:", mout)
    print("")
    txtout = input("Export to text file? : Y/N")
    while True:
        if txtout == 'Y' or txtout == 'y':
            #escrita de arquivo de texto aqui
            with open("output.txt",'w') as file:
                file.write(mout)
                tabber("Output written on file successfully.")
                pause()
                break
        elif txtout == 'N' or txtout == 'n':
            break
        else:
            print("Invalid Command, try again.")
            pause()
        
def menu():
    #Menu
    cls()
    filler("*")
    centerprint("S.I.S Feed\n")
    tabber("1. Upload to feed")
    tabber("2. Request from feed")
    tabber("3. Exit")
    entry = input("> ")
    return entry

def registrar(database):
    cls()
    filler("*")
    centerprint("Registro de Usuário")
    print("Insira os dados para criar um novo usuário.")
    username = input("Nome de usuário: ")
    password = input("Senha: ")

    novo_usuario = Usuario(username, password)
    if novo_usuario.salvar_no_banco(database):
        centerprint("Usuário registrado com sucesso!")
    else:
        centerprint("Usuário já existe.")
    pause()
        
def login(database):
    cls()
    filler("*")
    centerprint("Login de Usuário")
    print("Insira os dados para fazer login.")
    username = input("Nome de usuário: ")
    password = input("Senha: ")

    usuario = Usuario.buscar_no_banco(username, database)
    if usuario and usuario.verificar_senha(password):
        centerprint("Login bem-sucedido!")
        pause()
        return usuario
    else:
        centerprint("Nome de usuário ou senha incorretos.")
        pause()
        return None

def auth(database):
    while True:
        cls()
        filler("*")
        centerprint("S.I.S Feed")
        print("")
        print("")
        centerprint("1 - Login")
        centerprint("2 - Registrar")
        centerprint("3 - Sair")
        opt = input("   > ")
        if opt == '3':
            centerprint("Encerrando o Programa")
            pause()
            exit()
        elif opt == '1':
            usuario = login(database)
            if usuario:
                return usuario
        elif opt == '2':
            registrar(database)
        else:
            centerprint("Opção inválida. Tente novamente.")
            pause()


database = Conexao("localhost", "root", 'mysql', 'SIS')
cifra = CifraVigenere()
admin = Usuario('admin','admin')
#Fazer o client aqui com interface, logins, uploads e submissoes
#NOta - escrever o menu principal e separar as funções de envio e requisição

usuario_logado = auth(database)  # Autentica o usuário

while True:
    entry = menu()
    if entry == '1':
        submit()
        pause()
    elif entry == '2':
        request()
        pause()
    elif entry == '3':
        centerprint("Closing Programme")
        pause()
        break
    else:
        centerprint("Entrada INvalida")
        pause()