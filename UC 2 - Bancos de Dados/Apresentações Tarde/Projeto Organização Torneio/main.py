from Conexao import Conexao


def cadastrar_time(conexaoBD):
    nome = input("Digite o nome da equipe: ")
    pais = input("Digite o país da equipe: ")

    sql = """
    INSERT INTO Equipes (Nome, Pais)
    VALUES (%s, %s);
    """
    valores = (nome, pais)
    conexaoBD.manipular(sql, valores)
    print("Equipe cadastrada com sucesso!")

def listar_times(conexaoBD):
    sql = "SELECT * FROM Equipes;"
    resultados = conexaoBD.consultar(sql)

    if resultados:
        print("\nTimes cadastrados:")
        for row in resultados:
            print(f"ID: {row[0]}, Nome: {row[1]}, País: {row[2]}")
    else:
        print("Nenhum time encontrado.")

def cadastrar_jogador(conexaoBD):
    nome = input("Digite o nome do jogador: ")
    nickname = input("Digite o nickname do jogador: ")
    idade = input("Digite a idade do jogador: ")
    nacionalidade = input("Digite a nacionalidade do jogador: ")

    sql = """
    INSERT INTO Jogadores (Nome, Nickname, Idade, Nacionalidade)
    VALUES (%s, %s, %s, %s);
    """
    valores = (nome, nickname, idade, nacionalidade)
    conexaoBD.manipular(sql, valores)
    print("Jogador cadastrado com sucesso!")

def listar_jogadores(conexaoBD):
    sql = "SELECT * FROM Jogadores;"
    resultados = conexaoBD.consultar(sql)

    if resultados:
        print("\nJogadores cadastrados:")
        for row in resultados:
            print(f"ID: {row[0]}, Nome: {row[1]}, Nickname: {row[2]}, Idade: {row[3]}, Nacionalidade: {row[4]}")
    else:
        print("Nenhum jogador encontrado.")

def cadastrar_torneio(conexaoBD):
    nome = input("Digite o nome do torneio: ")
    data_inicio = input("Digite a data de início (YYYY-MM-DD): ")
    data_fim = input("Digite a data de fim (YYYY-MM-DD): ")
    premiacao = input("Digite a premiação: ")

    sql = """
    INSERT INTO Torneios (Nome, Data_Inicio, Data_Fim, Premiacao)
    VALUES (%s, %s, %s, %s);
    """
    valores = (nome, data_inicio, data_fim, premiacao)
    conexaoBD.manipular(sql, valores)
    print("Torneio cadastrado com sucesso!")

def listar_torneios(conexaoBD):
    sql = "SELECT * FROM Torneios;"
    resultados = conexaoBD.consultar(sql)

    if resultados:
        print("\nTorneios cadastrados:")
        for row in resultados:
            print(f"ID: {row[0]}, Nome: {row[1]}, Data Início: {row[2]}, Data Fim: {row[3]}, Premiação: {row[4]}")
    else:
        print("Nenhum torneio encontrado.")

def associar_jogador_a_time(conexaoBD):
    id_jogador = input("Digite o ID do jogador: ")
    id_time = input("Digite o ID do time: ")
    posicao = input("Digite a posição do jogador (Titular/Reserva): ")

    sql = """
    INSERT INTO Jogadores_Equipes (ID_Jogador, ID_Equipe, Posicao)
    VALUES (%s, %s, %s);
    """
    valores = (id_jogador, id_time, posicao)
    conexaoBD.manipular(sql, valores)
    print("Jogador associado ao time com sucesso!")

def associar_time_a_torneio(conexaoBD):
    id_time = input("Digite o ID do time: ")
    id_torneio = input("Digite o ID do torneio: ")

    sql_verificar_time = "SELECT COUNT(*) FROM Equipes WHERE ID = %s;"
    if conexaoBD.consultar(sql_verificar_time, (id_time,))[0][0] == 0:
        print("O ID do time fornecido não existe.")
        return

    # Verificar se o torneio existe
    sql_verificar_torneio = "SELECT COUNT(*) FROM Torneios WHERE ID = %s;"
    if conexaoBD.consultar(sql_verificar_torneio, (id_torneio,))[0][0] == 0:
        print("O ID do torneio fornecido não existe.")
        return


    sql_associar = """
    INSERT INTO Equipes_Torneios (ID_Equipe, ID_Torneio)
    VALUES (%s, %s);
    """
    valores = (id_time, id_torneio)
    conexaoBD.manipular(sql_associar, valores)
    print("Time associado ao torneio com sucesso!")


def main():
    try:
        conexaoBD = Conexao("localhost", "root", "mysql", "Esports")

        while True:
            print("\nMenu:")
            print("1. Cadastrar time")
            print("2. Listar times")
            print("3. Cadastrar jogador")
            print("4. Listar jogadores")
            print("5. Cadastrar torneio")
            print("6. Listar torneios")
            print("7. Associar jogador a time")
            print("8. Associar time a torneio")
            print("9. Sair")

            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                cadastrar_time(conexaoBD)
            elif opcao == "2":
                listar_times(conexaoBD)
            elif opcao == "3":
                cadastrar_jogador(conexaoBD)
            elif opcao == "4":
                listar_jogadores(conexaoBD)
            elif opcao == "5":
                cadastrar_torneio(conexaoBD)
            elif opcao == "6":
                listar_torneios(conexaoBD)
            elif opcao == "7":
                associar_jogador_a_time(conexaoBD)
            elif opcao == "8":
                associar_time_a_torneio(conexaoBD)
            elif opcao == "9":
                print("Saindo...")
                break
            else:
                print("Opção inválida, tente novamente.")

    except Exception as e:
        print(f"Ocorreu um erro: {e}")

if __name__ == "__main__":
    main()
