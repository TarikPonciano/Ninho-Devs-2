from Conexao import Conexao
from Senha import Senha
import funcionalidade_empregador
import trabalhador

conexaoBd = Conexao("localhost", "root", "mysql", "portaldeempregos")

def gerenciar_aplicacoes():
    aplicacoes = conexaoBd.consultar("SELECT * FROM portaldeempregos.aplicacao")
    
    if aplicacoes:
        print("-- MOSTRANDO APLICAÇÕES --\n")
        for aplicacao in aplicacoes:
            vaga = conexaoBd.consultar(f"SELECT nome_vaga FROM portaldeempregos.vagas WHERE id_vaga = {aplicacao[2]};")
            candidato = conexaoBd.consultar(f"SELECT nome_candidato FROM portaldeempregos.candidato WHERE id_candidato = {aplicacao[1]}")
            if vaga and candidato:  # Verificar se os dados foram encontrados
                print(f"ID: {aplicacao[0]} | CANDIDATO: {candidato[0][0]}  | VAGA: {vaga[0][0]} | DATA CANDIDATURA: {aplicacao[3]} | STATUS: {aplicacao[4]}\n")
            else:
                print(f"Erro ao obter dados para a aplicação ID {aplicacao[0]}")
    else:
        print("Nenhuma aplicação para vaga foi encontrada.")

def cadastrar_aplicacao():
    print("--- CADASTRO DE APLICAÇÕES ---\n")
    gerenciar_aplicacoes()
    
    # Captura IDs do candidato e da vaga
    candidato_id = input("Digite o ID do Candidato: ").strip()
    vaga_id = input("Digite o ID da Vaga: ").strip()
    status = input("Digite o Status da aplicação: ").strip()

    # SQL para inserir a aplicação
    sql = '''
    INSERT INTO aplicacao (id_aplicacao, id_candidato, id_vaga, data_aplicacao, status_aplicacao)
    VALUES (DEFAULT, %s, %s, DEFAULT, %s)
    '''
    
    try:
        conexaoBd.manipularComParametro(sql, (candidato_id, vaga_id, status))
        print("Aplicação cadastrada com sucesso!")
    except Exception as e:
        print(f"Erro ao cadastrar aplicação: {e}")

def excluir_aplicacao():
    gerenciar_aplicacoes()

    try:
        idAplicacao = int(input("Digite o id da Aplicação que deseja remover: "))
    except ValueError:
        print("ID inválido. Operação Cancelada!")
        return

    if idAplicacao <= 0:
        print("Operação Cancelada!")
        return

    aplicacaoEscolhida = conexaoBd.consultarComParametro("SELECT * FROM aplicacao WHERE id_aplicacao = %s", (idAplicacao,))

    if not aplicacaoEscolhida:
        print("Aplicação não encontrada!")
        return

    aplicacao = aplicacaoEscolhida[0]
    print(f'''
    ID da Aplicação: {aplicacao[0]}
    ID do Candidato: {aplicacao[1]}
    ID da Vaga: {aplicacao[2]}
    Data da Aplicação: {aplicacao[3]}
    Status da Aplicação: {aplicacao[4]}''')

    confirmacao = input("Confirme se deseja remover a aplicação (sim/não): ").strip().lower()

    if confirmacao == "sim":
        try:
            conexaoBd.manipularComParametro("DELETE FROM aplicacao WHERE id_aplicacao = %s", (idAplicacao,))
            print("Aplicação removida com sucesso!")
        except Exception as e:
            print(f"Erro ao remover aplicação: {e}")
    else:
        print("Operação Cancelada")

def alterar_aplicacao():
    gerenciar_aplicacoes()

    try:
        idAplicacao = int(input("Digite o ID da Aplicação que deseja Alterar: "))
    except ValueError:
        print("ID inválido. Operação Cancelada!")
        return

    if idAplicacao <= 0:
        print("Operação Cancelada!")
        return

    aplicacaoEscolhida = conexaoBd.consultarComParametro(
        "SELECT * FROM aplicacao WHERE id_aplicacao = %s", 
        (idAplicacao,)
    )

    if not aplicacaoEscolhida:
        print("Aplicação não encontrada!")
        return

    aplicacao = aplicacaoEscolhida[0]
    print(f'''
    ID da Aplicação: {aplicacao[0]}
    ID do Candidato: {aplicacao[1]}
    ID da Vaga: {aplicacao[2]}
    Data da Aplicação: {aplicacao[3]}
    Status da Aplicação: {aplicacao[4]}
    ''')

    candidato_atual = aplicacao[1]
    vaga_atual = aplicacao[2]
    status_atual = aplicacao[4]

    novoCandidato_input = input("Digite o Novo ID do Candidato (deixe vazio para manter o atual): ").strip()
    if novoCandidato_input:
        try:
            novoCandidato = int(novoCandidato_input)
        except ValueError:
            print("ID do Candidato inválido. Operação Cancelada!")
            return
    else:
        novoCandidato = candidato_atual

    novaVaga_input = input("Digite o Novo ID da Vaga (deixe vazio para manter o atual): ").strip()
    if novaVaga_input:
        try:
            novaVaga = int(novaVaga_input)
        except ValueError:
            print("ID da Vaga inválido. Operação Cancelada!")
            return
    else:
        novaVaga = vaga_atual

    novoStatus = input("Digite o Novo Status da Aplicação (deixe vazio para manter o atual): ").strip()
    if not novoStatus:
        novoStatus = status_atual

    sql = '''
    UPDATE aplicacao
    SET
        id_candidato = %s,
        id_vaga = %s,
        data_aplicacao = DEFAULT,
        status_aplicacao = %s
    WHERE
        id_aplicacao = %s;
    '''
    
    try:
        conexaoBd.manipularComParametro(sql, (novoCandidato, novaVaga, novoStatus, idAplicacao))
        print("Aplicação atualizada com sucesso!")
    except Exception as e:
        print(f"Erro ao atualizar aplicação: {e}")




def ver_empresas():
    empresas = conexaoBd.consultar("SELECT * FROM portaldeempregos.empresa")
    
    if empresas != []:
        print("-- MOSTRANDO EMPRESAS CADASTRADAS --\n")
        for empresa in empresas:
            print(f"ID: {empresa[0]} | EMPRESA: {empresa[1]}  | CNPJ: {empresa[2]} | LOCALIZAÇÃO: {empresa[3]} | PORTE: {empresa[4]} | DESCRIÇÃO: {empresa[5]}\n")
    else:
        print("Nenhuma empresa cadastrada")
        
    return empresas



def pegar_id_empresa():
    lista_empresas = ver_empresas()
    if lista_empresas != []:
        
        lista_id = []
        for id in lista_empresas:
            lista_id.append(id[0])
        while True:
            try:
                
                id = int(input("Digite o ID da empresa: "))
            except Exception as erro:
                id = 0

            if id in lista_id:
                return id
            else:
                print("ID da empresa inválido!")


def cadastrar_empresa():
    print("--- CADASTRO DE EMPRESA --\n")
    nome = input("Digite o nome da empresa: ")
    while True:
        cnpj = input("Digite o CNPJ da empresa (Apenas números): ")
    
        if cnpj.isdigit() and len(cnpj) == 14:
            cnpj = int(cnpj)
            break 
        else:
            print("CNPJ inválido. Certifique-se de que o CNPJ contém exatamente 14 números.")
            

    localizacao = input("Digite a localização da empresa: ")
    porte = input("Qual o porte da empresa (Pequeno/Médio/Grande): ")
    descricao = input("Digite uma descrição da empresa: ")

    sql_empresa = '''
    INSERT INTO empresa (nome_empresa, cnpj_empresa, localizacao_empresa, porte_empresa, descricao_empresa)
    VALUES (%s, %s, %s, %s, %s);'''

    
    conexaoBd.manipularComParametro(sql_empresa, (nome, cnpj, localizacao, porte, descricao))
    id_empresa = conexaoBd._cursor.lastrowid

    print("Empresa cadastrada com sucesso!")
    input("Tecle enter para continuar!")



def ver_candidatos():
    candidatos = conexaoBd.consultar("SELECT * FROM portaldeempregos.candidato")
    
    if candidatos != []:
        print("-- MOSTRANDO CANDIDATOS CADASTRADOS --\n")
        for candidato in candidatos:
            print(f"ID: {candidato[0]} | CANDIDATO: {candidato[1]}  | CPF: {candidato[2]} | TELEFONE: {candidato[3]} | ENDEREÇO: {candidato[4]} | E-MAIL: {candidato[5]}\n")
    else:
        print("Nenhuma candidato cadastrado")

    input("Tecle enter para continuar!")
    return candidatos


def ver_vagas():
    vagas = conexaoBd.consultar("SELECT * FROM portaldeempregos.vagas")
    
    if vagas != []:
        print("-- MOSTRANDO VAGAS DISPONÍVEIS --\n")
        for vaga in vagas:
            empresa = conexaoBd.consultar(f"SELECT nome_empresa FROM portaldeempregos.empresa WHERE id_empresa = {vaga[1]};")
            print(f"ID: {vaga[0]} | EMPRESA: {empresa[0][0]}  | VAGA: {vaga[2]} | FUNÇÃO: {vaga[3]} | SALÁRIO: R$ {vaga[4]:.2F}\n")
    else:
        print("Nenhuma vaga encontrada.")
    
    input("Tecle enter para continuar!")

    return vagas


def excluir_vaga():
    vagas = ver_vagas()

    if vagas != []:
        id_vagas = []
        for id in vagas:
            id_vagas.append(id[0])
        
        while True:
            try:
                id = int(input("Digite o ID da vaga a ser excluída: "))
            except Exception as erro:
                id = 0

            if id in id_vagas:
                sql = "DELETE FROM vagas WHERE id_vaga = %s"
                conexaoBd.manipularComParametro(sql, (id,))
                print("Vaga excluída com sucesso!")
                break
            else:
                print("Digite um ID válido!")
        input("Tecle enter para continuar!")




def excluir_candidato():
    candidatos = ver_candidatos()

    if candidatos != []:
        id_candidato = []
        for id in candidatos:
            id_candidato.append(id[0])
        
        while True:
            try:
                id = int(input("Digite o ID da vaga a ser excluída: "))
            except Exception as erro:
                id = 0

            if id in id_candidato:
                sql_delete = "DELETE FROM aplicacao WHERE id_candidato = %s;"
                conexaoBd.manipularComParametro(sql_delete, (id,))
                sql = "DELETE FROM candidato WHERE id_candidato = %s;"
                conexaoBd.manipularComParametro(sql, (id,))
                print("Candidato excluído com sucesso!")
                break
            else:
                print("Digite um ID válido!")
        input("Tecle enter para continuar!")





def menu_administrador():
    
    autenticado = Senha.Autenticação()
    if(autenticado):
        while True:
            print("\n--- Menu do Administrador ---")
            print("1. Gerenciar Empresas")
            print("2. Gerenciar Candidatos")
            print("3. Gerenciar Aplicações")
            print("4. Voltar")

            escolha = input("Escolha uma opção: ").strip()

            if escolha == '1':
                while True:    
                    print("\n--- Menu de Empresas ---")
                    print("1. Ver Empresas")
                    print("2. Cadastrar Empresa")
                    print("3. Ver Vagas")
                    print("4. Cadastrar Vaga")
                    print("5. Ver Candidatos Inscritos")
                    print("6. Excluir Vaga")
                    print("0. Voltar")

                    escolha = input("Escolha uma opção: ").strip()
                    if escolha == '1':
                        ver_empresas()
                        
                    elif escolha == '2':
                        cadastrar_empresa()
                        
                    elif escolha == '3':
                        ver_vagas()
                        
                    elif escolha == '4':
                        print("Qual a empresa que esta divulgando a vaga?")
                        id = pegar_id_empresa()
                
                        funcionalidade_empregador.cadastrar_vaga(id)
                        
                    elif escolha == '5':
                        
                        id = pegar_id_empresa()
                
                        funcionalidade_empregador.ver_candidatos_inscritos(id)
                        
                    elif escolha == '6':
                        excluir_vaga()
                        
                    elif escolha == '0':
                        break
                    else:
                        print("Opção inválida, tente novamente.")

            elif escolha == '2':
                while True:    
                    print("\n--- Menu de Candidatos ---")
                    print("1. Ver Candidatos")
                    print("2. Cadastrar Candidato")
                    print("3. Excluir Candidato")
                    print("4. Editar Candidato")
                    print("0. Voltar")

                    escolha = input("Escolha uma opção: ").strip()
                    if escolha == '1':
                        ver_candidatos()
                        
                    elif escolha == '2':
                        print("-- Cadastro de Candidato --")
                        #Formulario:
                        nomeValor = input("Digite o nome(somente nome e sobrenome): ")
                        cpfValor = input("Digite o cpf(não use ponto, traços ou virgulas): ")
                        emailValor = input("Digite o email: ")
                        enderecoValor = input("Digite o endereço: ")
                        numeroValor = input("Digite o numero de telefone(Use somente numeros): ")
                        valor = [nomeValor, cpfValor, numeroValor, enderecoValor, emailValor]
                        
                        #para realizar o cadastro ainda não é necessario nenhuma verificação.
                        registro = trabalhador.Cadastro_candidato(valor)
                        registro.cadastrar()
                        
                        print("Inscrição realizada...")
                        
                    elif escolha == '3':
                        excluir_candidato()
                        
                    elif escolha == '4':
                        candidatos = ver_candidatos()
                        if candidatos != []:
                            id_candidato = []
                            for id in candidatos:
                                id_candidato.append(id[0])
                            
                            while True:
                                try:
                                    id = int(input("Digite o ID da candidato a ser editado: "))
                                except Exception as erro:
                                    id = 0

                                if id in id_candidato:
                                    candidatos = conexaoBd.consultarComParametro("SELECT * FROM portaldeempregos.candidato WHERE id_candidato = %s", (id,))
                                    print(f"ID: {candidatos[0][0]} | CANDIDATO: {candidatos[0][1]}  | CPF: {candidatos[0][2]} | TELEFONE: {candidatos[0][3]} | ENDEREÇO: {candidatos[0][4]} | E-MAIL: {candidatos[0][5]}\n")

                                    nomeValor = input("Digite seu nome(somente nome e sobrenome): ")
                                    cpfValor = input("Digite seu cpf(não use ponto, traços ou virgulas): ")
                                    emailValor = input("Digite seu email: ")
                                    enderecoValor = input("Digite o seu endereço: ")
                                    numeroValor = input("Digite o seu numero(Use somente numeros): ")

                                    sql = '''
                                        UPDATE candidato
                                        SET nome_candidato = %s,
                                        cpf_candidato = %s,
                                        telefone_candidato = %s,
                                        endereco_candidato = %s,
                                        email_candidato = %s
                                        WHERE id_candidato = %s;
                                        '''
                                    
                                    conexaoBd.manipularComParametro(sql, (nomeValor, cpfValor, numeroValor, enderecoValor, emailValor, id))
                                    print("Candidato editado com sucesso!")
                                    break
                                else:
                                    print("Digite um ID válido!")

                    elif escolha == "0":
                        return menu_administrador()
                    else:
                        print("Opção inválida, tente novamente.")

            elif escolha == '3':
                while True:
                    print("\n--- Menu de Aplicações ---")
                    print("1. Cadastrar Aplicações")
                    print("2. Excluir Aplicações")
                    print("3. Alterar Aplicações")
                    print("4. Ver Aplicações")
                    print("5. Voltar")
                    
                    escolha = input("Escolha uma opção: ").strip()
                    
                    if escolha == '1':
                        cadastrar_aplicacao()
                    elif escolha == '2':
                        excluir_aplicacao()
                    elif escolha == '3':
                        alterar_aplicacao()
                    elif escolha == '4':
                        gerenciar_aplicacoes()
                    elif escolha == "5":
                        break
                    else:
                        print("Opção inválida, tente novamente.")

            elif escolha == '4':
                break
            else:
                print("Opção inválida, tente novamente.")
    else:
        print("Não autenticado")

