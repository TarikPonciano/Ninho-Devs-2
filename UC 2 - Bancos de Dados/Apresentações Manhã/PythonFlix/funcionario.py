from conexao import Conexao
from datetime import datetime

class Funcionario:
    def __init__(self):
        self.conexaoBD = Conexao("localhost", "root", "mysql", "pythonflix")
        usuario = input("Digite o seu nome de usuário: ")
        senha = input("Digite sua senha: ")

        if usuario == "funcionario1" and senha == "pythonflix":
            print("Login bem-sucedido!")
            self.menu()
        else:
            print("Usuário ou senha incorretos.")
            self.conexaoBD.desconectar()  # Assegure-se de desconectar se o login falhar.

    def menu(self):
        while True:
            print('''
                1. Adicionar Novo Filme
                2. Atualizar Filme
                3. Remover Filme
                4. Executar Consulta Personalizada
                5. Sair
            ''')
            escolha = input("Digite sua opção: ")

            if escolha == "1":
                self.adicionar_filme()
            elif escolha == "2":
                self.atualizar_filme()
            elif escolha == "3":
                self.remover_filme()
            elif escolha == "4":
                self.executar_consulta()
            elif escolha == "5":
                print("Saindo...")
                self.conexaoBD.desconectar()
                break
            else:
                print("Opção inválida, tente novamente.")

    def adicionar_filme(self):
        nome = input("Digite o nome do filme: ")
        genero = input("Digite o gênero do filme: ")
        ano = int(input("Digite o ano de lançamento: "))
        valor_locacao = float(input("Digite o valor de locação: "))
        disponibilidade = bool(int(input("Digite a disponibilidade (0/1): ")))

        sql = '''
            INSERT INTO filmes (nome, genero, ano, valor_locacao, disponibilidade) 
            VALUES (%s, %s, %s, %s, %s)
        '''
        dados = (nome, genero, ano, valor_locacao, disponibilidade)
        try:
            self.conexaoBD.executar_com_parametros(sql, dados)
            print("Filme inserido com sucesso!")
        except Exception as e:
            print(f"Erro ao adicionar filme: {e}")

    def atualizar_filme(self):
        self.listar_filmes()
        id_filme = int(input("Digite o ID do filme que deseja atualizar: "))
        campo = input("Digite o campo que deseja atualizar (nome, genero, ano, valor_locacao, disponibilidade): ")
        novo_valor = input(f"Digite o novo valor para {campo}: ")

        sql = f"UPDATE filmes SET {campo} = %s WHERE id_filme = %s"
        try:
            self.conexaoBD.executar_com_parametros(sql, (novo_valor, id_filme))
            print("Filme atualizado com sucesso!")
        except Exception as e:
            print(f"Erro ao atualizar filme: {e}")

    def remover_filme(self):
        self.listar_filmes()
        id_filme = int(input("Digite o ID do filme que deseja remover: "))

        sql = "DELETE FROM filmes WHERE id_filme = %s"
        try:
            self.conexaoBD.executar_com_parametros(sql, (id_filme,))
            print("Filme removido com sucesso!")
        except Exception as e:
            print(f"Erro ao remover filme: {e}")

    def executar_consulta(self):
        consulta = input("Digite a consulta SQL: ")
        try:
            resultados = self.conexaoBD.consultar(consulta)
            for resultado in resultados:
                print(resultado)
        except Exception as e:
            print(f"Erro ao executar consulta: {e}")

    def listar_filmes(self):
        try:
            filmes = self.conexaoBD.consultar("SELECT * FROM filmes")
            print("ID / Nome / Gênero / Ano / Valor Locação / Disponibilidade")
            for filme in filmes:
                print(f"{filme[0]} / {filme[1]} / {filme[2]} / {filme[3]} / {filme[4]} / {filme[5]}")
        except Exception as e:
            print(f"Erro ao listar filmes: {e}")

if __name__ == "__main__":
    funcionario = Funcionario()
