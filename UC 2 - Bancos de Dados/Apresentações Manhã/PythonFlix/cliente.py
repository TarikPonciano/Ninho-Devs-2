from conexao import Conexao
from datetime import datetime

class Cliente:
    def __init__(self):
        self.conexaoBD = Conexao("localhost", "root", "mysql", "pythonflix")
        self.menu()
        
    
    
    def menu(self):
        while True:
            print('''
                1. Visualizar Catálogo de Filmes
                2. Alugar Filme
                3. Devolver Filme
                4. Ver Filmes Alugados
                5. Cadastrar Novo Usuário
                6. Sair
            ''')
            escolha = input("Digite sua opção: ")

            if escolha == "1":
                self.visualizar_catalogo()
            elif escolha == "2":
                self.alugar_filme()
            elif escolha == "3":
                self.devolver_filme()
            elif escolha == "4":
                self.ver_filmes_alugados()
            elif escolha == "5":
                self.cadastrar_novo_usuario()
            elif escolha == "6":
                print("Saindo...")
                self.conexaoBD.desconectar()
                break
            else:
                print("Opção inválida, tente novamente.")
                
            # input("Tecle Enter para Continuar")

    def visualizar_catalogo(self):
        filmes = self.conexaoBD.consultar("SELECT * FROM filmes WHERE disponibilidade = TRUE")
        print("ID / Nome / Gênero / Ano / Valor Locação")
        for filme in filmes:
            print(f"{filme[0]} / {filme[1]} / {filme[2]} / {filme[3]} / {filme[4]}")

    def alugar_filme(self):
        # Mostrar filmes disponíveis
        filmes = self.conexaoBD.consultar("SELECT * FROM filmes WHERE disponibilidade = TRUE")
        print("ID / Nome / Gênero / Ano / Valor Locação")
        for filme in filmes:
            print(f"{filme[0]} / {filme[1]} / {filme[2]} / {filme[3]} / {filme[4]}")

        id_filme = int(input("Digite o ID do filme que deseja alugar: "))
        id_cliente = int(input("Digite seu ID de cliente: "))
        data_aluguel = datetime.now().date()

        # Verificar se o filme está disponível
        filme = self.conexaoBD.consultar("SELECT * FROM filmes WHERE id_filme = %s AND disponibilidade = TRUE", (id_filme,))
        if not filme:
            print("Filme não disponível ou não encontrado!")
            return

        sql = '''
            INSERT INTO aluguel (id_filme, id_cliente, data_aluguel) 
            VALUES (%s, %s, %s)
        '''
        self.conexaoBD.executar_com_parametros(sql, (id_filme, id_cliente, data_aluguel))

        # Atualizar a disponibilidade do filme
        self.conexaoBD.executar_com_parametros("UPDATE filmes SET disponibilidade = FALSE WHERE id_filme = %s", (id_filme,))

        # Emitir nota fiscal
        self.emitir_nota_fiscal(id_filme, id_cliente, data_aluguel)

        print("Filme alugado com sucesso!")

    def emitir_nota_fiscal(self, id_filme, id_cliente, data_aluguel):
        # Consultar detalhes do aluguel
        aluguel = self.conexaoBD.consultar("SELECT f.nome, f.valor_locacao FROM aluguel a JOIN filmes f ON a.id_filme = f.id_filme WHERE a.id_filme = %s AND a.id_cliente = %s AND a.data_aluguel = %s", (id_filme, id_cliente, data_aluguel))
        if aluguel:
            nome_filme, valor_locacao = aluguel[0]
            nota_fiscal = f"Nota Fiscal\nFilme: {nome_filme}\nValor Locação: {valor_locacao}\nData de Aluguel: {data_aluguel}"
            print(nota_fiscal)
        else:
            print("Detalhes do aluguel não encontrados para emissão da nota fiscal.")

    def devolver_filme(self):
        id_cliente = int(input("Digite seu ID de cliente: "))
        alugueis = self.conexaoBD.consultar("SELECT * FROM aluguel WHERE data_devolucao IS NULL AND id_cliente = %s", (id_cliente,))
        print("ID / ID Filme / Data Aluguel")
        for aluguel in alugueis:
            print(f"{aluguel[0]} / {aluguel[1]} / {aluguel[3]}")

        id_aluguel = int(input("Digite o ID do aluguel que deseja devolver: "))
        data_devolucao = datetime.now().date()

        # Atualizar a devolução do filme
        self.conexaoBD.executar_com_parametros("UPDATE aluguel SET data_devolucao = %s WHERE id_aluguel = %s", (data_devolucao, id_aluguel))

        # Atualizar a disponibilidade do filme
        aluguel = self.conexaoBD.consultar("SELECT id_filme FROM aluguel WHERE id_aluguel = %s", (id_aluguel,))
        if aluguel:
            id_filme = aluguel[0][0]
            self.conexaoBD.executar_com_parametros("UPDATE filmes SET disponibilidade = TRUE WHERE id_filme = %s", (id_filme,))
            print("Filme devolvido com sucesso!")
        else:
            print("Aluguel não encontrado!")

    def ver_filmes_alugados(self):
        id_cliente = int(input("Digite seu ID de cliente: "))
        alugueis = self.conexaoBD.consultar("SELECT f.nome, a.data_aluguel FROM aluguel a JOIN filmes f ON a.id_filme = f.id_filme WHERE a.id_cliente = %s AND a.data_devolucao IS NULL", (id_cliente,))
        if alugueis:
            print("Filmes Alugados:")
            for aluguel in alugueis:
                print(f"Nome: {aluguel[0]}, Data de Aluguel: {aluguel[1]}")
        else:
            print("Você não tem filmes alugados no momento.")

    def cadastrar_novo_usuario(self):
        nickname = input("Digite o nickname do novo usuário: ")
        nome = input("Digite o nome do novo usuário: ")
        telefone = input("Digite o telefone do novo usuário: ")
        cpf = input("Digite o CPF do novo usuário: ")

        sql = '''
            INSERT INTO usuario (nickname, nome, telefone, cpf) 
            VALUES (%s, %s, %s, %s)
        '''
        try:
            self.conexaoBD.executar_com_parametros(sql, (nickname, nome, telefone, cpf))
            print("Novo usuário cadastrado com sucesso!")
        except Exception as e:
            print(f"Erro ao cadastrar novo usuário: {e}")

if __name__ == "__main__":
    cliente = Cliente()
    cliente.menu()
