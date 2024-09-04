from Conexao import Conexao

import main

conexaoBd = Conexao("localhost", "root", "mysql", "portaldeempregos")



def verificar_cnpj(cnpj):
    sql = "SELECT id_empresa FROM empresa WHERE cnpj_empresa = %s"
    resultado = conexaoBd.consultarComParametro(sql, (cnpj,))
    if resultado:
        return resultado[0][0]
    else:
        return None


def acessar_como_empregador():
    print("-- Acessando como Empregador --\n")

    while True:
        cnpj = input("Digite o CNPJ da empresa (Apenas números): ")
    
        if cnpj.isdigit() and len(cnpj) == 14:
            cnpj = int(cnpj)
            break 
        else:
            print("CNPJ inválido. Certifique-se de que o CNPJ contém exatamente 14 números.")

    id_empresa = verificar_cnpj(cnpj)

    if id_empresa:
        print("Acesso permitido.")
        menu_empregador(id_empresa)
    else:
        
        while True:
            print('''
    -- Não Consegui identificar sua Empresa 🙁 --
    1 - Cadastrar Empresa
    2 - Tentar Novamente
    3 - Sair
''')

            op = input("Escolha uma opção: ")
            if op == "1":
                id_empresa = cadastrar_empresa()
                menu_empregador(id_empresa)
                break
            elif op == "2":
                return acessar_como_empregador()
            elif op == "3":
                print("Voltando ao Menu Principal")
                return main.menu()
            else:
                print("Digite uma opção válida:")


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
    input("tecle enter para continuar!")

    return id_empresa


def editar_cadastro_empresa(id_empresa):
    empresa = conexaoBd.consultar(f"SELECT nome_empresa, localizacao_empresa, porte_empresa, descricao_empresa FROM portaldeempregos.empresa WHERE id_empresa = {id_empresa};")
    for dados in empresa:
        print(f"Empresa: {dados[0]} | Localização: {dados[1]} | Porte: {dados[2]} | Descrição: {dados[3]}")
    print("--- EDITAR EMPRESA ---\n")

    nome_empresa = input("Digite o novo nome da empresa: ")
    localizacao_empresa = input("Digite a nova localização: ")
    porte_empresa = input("Qual o novo porte da empresa (Pequeno/Médio/Grande):")
    descricao_empresa = input("Digite a nova descrição da empresa: ")

    sql = '''
    UPDATE empresa
    SET nome_empresa = %s,
    localizacao_empresa = %s,
    descricao_empresa = %s,
    porte_empresa = %s
    WHERE id_empresa = %s;
    '''

    conexaoBd.manipularComParametro(sql, (nome_empresa, localizacao_empresa, descricao_empresa, porte_empresa, id_empresa))
    print("Empresa editada com sucesso!")
    input("tecle enter para continuar!")



def cadastrar_vaga(id_empresa):
    print("--- CADASTRO DE VAGA --\n")
    nome_vaga = input("Digite o nome da vaga: ")
    funcao_vaga = input("Digite a função: ")
    salario_vaga = float(input("Digite o salário: R$ "))
    
    sql_vaga = '''
    INSERT INTO vagas (id_empresa, nome_vaga, funcao_vaga, salario_vaga)
    VALUES (%s, %s, %s, %s);'''

    conexaoBd.manipularComParametro(sql_vaga, (id_empresa, nome_vaga, funcao_vaga, salario_vaga))

    print("Vaga cadastrada com sucesso!")
    input("tecle enter para continuar!")


def ver_vagas_publicadas(id_empresa):
    sql = "SELECT * FROM portaldeempregos.vagas WHERE id_empresa = %s"
    vagas = conexaoBd.consultarComParametro(sql, (id_empresa,))
    
    if vagas != []:
        print("-- MOSTRANDO VAGAS PUBLICADAS --\n")
        for vaga in vagas:
            empresa = conexaoBd.consultar(f"SELECT nome_empresa FROM portaldeempregos.empresa WHERE id_empresa = {vaga[1]};")
            print(f"ID: {vaga[0]} | EMPRESA: {empresa[0][0]}  | VAGA: {vaga[2]} | FUNÇÃO: {vaga[3]} | SALÁRIO: R$ {vaga[4]:.2F}\n")

    
    else:
        print("Nenhuma vaga encontrada 🙁.")
        

    input("tecle enter para continuar!")
    




def editar_vaga_publicada(id_empresa):

    sql = "SELECT id_vaga FROM portaldeempregos.vagas WHERE id_empresa = %s"
    vagas = conexaoBd.consultarComParametro(sql, (id_empresa,))
    lista_id_vagas = []
    for i in vagas:
        lista_id_vagas.append(i[0])

    if lista_id_vagas != []:
        ver_vagas_publicadas(id_empresa)

        print("--- EDITAR VAGA PUBLICADA---\n")
        
        while True:
            id_vaga = int(input("Digite o ID da vaga a ser editada: "))

            if id_vaga in lista_id_vagas:
                nome_vaga = input("Digite o novo nome da vaga: ")
                funcao_vaga = input("Digite a nova função: ")
                salario_vaga = float(input("Digite o novo salário: R$ "))

                sql = '''
                UPDATE vagas
                SET nome_vaga = %s,
                funcao_vaga = %s,
                salario_vaga = %s
                WHERE id_vaga = %s AND id_empresa = %s;
                '''

                conexaoBd.manipularComParametro(sql, (nome_vaga, funcao_vaga, salario_vaga, id_vaga, id_empresa))
                print("Vaga editada com sucesso!")
                break
            else:
                print("Digite um ID válido:")
    else:
        print("Nenhuma vaga encontrada 🙁.")
        
    input("tecle enter para continuar!")



def excluir_vaga(id_empresa):
    sql = "SELECT id_vaga FROM portaldeempregos.vagas WHERE id_empresa = %s"
    vagas = conexaoBd.consultarComParametro(sql, (id_empresa,))
    lista_id_vagas = []
    for i in vagas:
        lista_id_vagas.append(i[0])

    if lista_id_vagas != []:
        
        while True:
            ver_vagas_publicadas(id_empresa)
            print("-- EXCLUSÃO DE VAGA --\n")
            id_vaga = int(input("Digite o id da vaga publicada a ser excluida: "))

            if id_vaga in lista_id_vagas:
                sql = "DELETE FROM vagas WHERE id_vaga = %s and id_empresa = %s"
                conexaoBd.manipularComParametro(sql, (id_vaga, id_empresa))
                print("Vaga excluída com sucesso!")
                break
            else:
                print("Digite um ID válido!")
                input("Tecle enter para continuar!")
    else:
        print("Nenhuma vaga encontrada 🙁.")
    
    input("tecle enter para continuar!")



def ver_candidatos_inscritos(id_empresa):
    vagas = conexaoBd.consultarComParametro("SELECT * FROM portaldeempregos.vagas WHERE id_empresa = %s", (id_empresa,))
    
    if vagas != []:

        aplicacoes = conexaoBd.consultarComParametro("SELECT * FROM portaldeempregos.aplicacao WHERE id_vaga = %s", (vagas[0][1],))


        if aplicacoes != []:
            print("-- MOSTRANDO APLICAÇÕES FEITAS PARA A VAGA NA EMPRESA --\n")
            for aplicacao in aplicacoes:

                empresa = conexaoBd.consultarComParametro("SELECT nome_empresa FROM portaldeempregos.empresa WHERE id_empresa = %s",(id_empresa,))
                vaga = conexaoBd.consultar(f"SELECT nome_vaga FROM portaldeempregos.vagas WHERE id_vaga = {aplicacao[2]};")
                candidato = conexaoBd.consultar(f"SELECT nome_candidato FROM portaldeempregos.candidato WHERE id_candidato = {aplicacao[1]}")
                print(f"ID: {aplicacao[0]} | CANDIDATO: {candidato[0][0]}  | VAGA: {vaga[0][0]} | EMPRESA: {empresa[0][0]} | DATA CANDIDATURA: {aplicacao[3]} | STATUS: {aplicacao[4]}\n")
        else:
            print("Nenhuma aplicação para vaga de sua empresa foi encontrado 🙁.")
    else:
            print("Nenhuma aplicação para vaga de sua empresa foi encontrado.")
            
    input("Tecle enter para continuar!")



def menu_empregador(id_empresa):
    empresa = conexaoBd.consultar(f"SELECT nome_empresa FROM portaldeempregos.empresa WHERE id_empresa = {id_empresa};")
    while True:
        print(f'''
    Olá {empresa[0][0]}!\n
    --- Menu do Empregador ---
    1. Editar Cadastro da Empresa
    2. Cadastrar Vaga
    3. Editar Vaga
    4. Ver Vagas Publicadas
    5. Ver Candidatos Inscritos
    6. Excluir Vaga
    7. Voltar
''')
        

        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            editar_cadastro_empresa(id_empresa)
        
        elif escolha == '2':
            cadastrar_vaga(id_empresa)

        elif escolha == '3':
            editar_vaga_publicada(id_empresa)

        elif escolha == '4':
            ver_vagas_publicadas(id_empresa)

        elif escolha == '5':
            ver_candidatos_inscritos(id_empresa)

        elif escolha == '6':
            excluir_vaga(id_empresa)

        elif escolha == '7':
            print("Fechando o sistema do Empregador.")
            break
        else:
            print("Opção inválida, tente novamente.")


