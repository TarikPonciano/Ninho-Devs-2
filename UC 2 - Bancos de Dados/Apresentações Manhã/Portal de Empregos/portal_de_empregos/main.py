from Conexao import Conexao
import funcionalidade_empregador
import candidato
import Admistrador_funcionalidade

conexaoBd = Conexao("localhost", "root", "mysql", "portaldeempregos")

def menu():
    while True:
        print("\n--- Portal de Empregos ---")
        print("1. Acessar como Empregador")
        print("2. Acessar como Trabalhador")
        print("3. Acessar como Administrador")
        print("4. Sair")
        
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            funcionalidade_empregador.acessar_como_empregador()
        elif escolha == '2':
            candidato.trab()
        elif escolha == '3':
            Admistrador_funcionalidade.menu_administrador()
        elif escolha == '4':
            print("Saindo do programa...")
            return
        else:
            print("Opção inválida, tente novamente.")



if __name__ == "__main__":
    menu()