from trabalhador import Cadastro_candidato
from trabalhador import Trabalhador
import main

def trab():
    while True:
        #Menu de acesso:
        print("[0]login;")
        print("[1]Realizar cadastro;")
        print("[2]Voltar;")
        acesso = input("Escolha uma opção: ")
        
        if acesso == "0":
            while True:
                print(*"----- LOGIN -----") 
                login = Trabalhador()
                
                try:
                    
                    #O cpf e o email são necessarios para identificar o usuario que esta acessando, 
                    # #tambem para que se tenha um controle de segurança maior
                    email = input("Digite seu email: ")
                    
                    cpf = input("Digite seu cpf sem traços e pontos: ")
                    
                    verificacao = login.verificação(parametros = (email, cpf))
                    #Na verificação compara se as informaçoes dentro do email e do cpf batem, 
                    #em seguida retornando valores necessario para o acesso.                    


                    if verificacao !=([] and None):
                        #Mais uma etapa de verificação para entrar no menu de acesso do funcionario.
                        login.menu_trabalhador(acesso = True, id = verificacao[0])
                  
                  
                    elif verificacao == False:
                            
                            #Um menu pratico para ajudar o ususario a tentar a entrar novamente pelo o login.
                        pergunta = input('''
                            [1] Tentar fazer login novamente.
                            [0] Sair.

                        Escolha aqui:                      ''')
                        
                        if pergunta == "1":
                            continue

                        elif pergunta == "0":
                            break
                        else:
                            print("Valor invalido.")
                except Exception as erro:#Caso o erro seja critico o codigo fecha a pagina do login e informa qual foi o erro.
                    print(erro)
                    print('fechando login...')
                    break
                
            #Realiza o cadastro caso o usuario ainda não tenha um.        
        elif acesso == "1":
            #Formulario:
            nomeValor = input("Digite seu nome(somente nome e sobrenome): ")
            cpfValor = input("Digite seu cpf(não use ponto, traços ou virgulas): ")
            emailValor = input("Digite seu email: ")
            enderecoValor = input("Digite o seu endereço: ")
            numeroValor = input("Digite o seu numero(Use somente numeros): ")
            valor = [nomeValor, cpfValor, numeroValor, enderecoValor, emailValor]
            
            #para realizar o cadastro ainda não é necessario nenhuma verificação.
            registro = Cadastro_candidato(valor)
            registro.cadastrar()
            
            print("Inscrição realizada...")
        elif acesso == "2":
            print("Fechando o sistema do Trabalhador.")
            return main.menu()
        else:
            print("Valor não reconhecido.")