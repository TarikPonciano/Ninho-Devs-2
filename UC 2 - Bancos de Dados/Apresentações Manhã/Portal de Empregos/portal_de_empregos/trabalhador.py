from Conexao import Conexao
import candidato

#classe metodos necessarios para o cadastro.
class Cadastro_candidato():
    def __init__(self, parametros):
        self.parametros = parametros
        self._BD = Conexao("localhost", "root", "mysql", "portaldeempregos")
        
    def cadastrar(self):
        self._BD.manipularComParametro("INSERT INTO candidato VALUES (DEFAULT, %s, %s, %s, %s, %s)", parametros = self.parametros)

#classe e metodos necessarios para o login, verificação de usuario, verificaçao de vaga e aplicações,
#criação de aplicações e edição dos dados do usuario.
class Trabalhador():
    def __init__(self):
        
        #algumas variantes basicas.
        self._cpf = ""
        self._email = ""
        self._id = ""
        self._BD = Conexao("localhost", "root", "mysql", "portaldeempregos")
        
    def verificação(self, parametros):
        #Na verificação ela foi dividida em 3 etapas:
        #1º - verifica se não acontece nenhum erro critico ao sistema e tratalo com except.
        #2º - Verifica se o cpf e email existem não evitando retorna um valor vazio.
        #3º - verifica se o id dentro da tupla que a pesquisa do cpf e email retorna são iguais.
        try:
            self._email = self._BD.consultarComParametro(sql = ("SELECT * FROM candidato WHERE email_candidato = %s"), parametros=(parametros[0],))
            
            self._cpf = self._BD.consultarComParametro(sql = ("SELECT * FROM candidato WHERE cpf_candidato = %s"), parametros=(parametros[1],))
            
            if (self._cpf and self._email) != ("" and [] and None) and (self._id == ""):
                
                if self._email[0] == self._cpf[0]:
                    self._id = self._email[0]
                    return self._id
                
                else:
                    print("Email ou CPF incorreto.")
                    return False
                
            elif self._cpf in ["", [], None]:
                print("CPF invalido.")
                return False
            
            elif self._email in ["", [], None]:
                print("Email incorreto.")
                return False
                
        except Exception as erro:
            print("Erro de verificação, erro encontrado foi ", erro)
            return False
        
    def menu_trabalhador(self, acesso, id):
        #Só é possivel acessar esse menu caso seja retornado um True pela verificação.
        while acesso:
            print("\n--- Menu do Trabalhador ---")
            print("1. Buscar Vagas")
            print("2. Aplicar para Vaga")
            print("3. Visualizar Aplicações")
            print("4. Editar Cadastro")
            print("5. Voltar")

            escolhaT = input("Escolha uma opção: ")

            if escolhaT == '1':
                self.buscar_vagas()
            elif escolhaT == '2':
                self.aplicar_para_vaga(id)
            elif escolhaT == '3':
                self.visualizar_aplicacoes(id)
            elif escolhaT == '4':
                self.editar_cadastro_candidato(id)
            elif escolhaT == '5':
                print("Retornando ao Menu!")
                return candidato.trab()
            else:
                print("Opção inválida, tente novamente.")

    def buscar_vagas(self):
        #Pesquisa todas as vagas relacionada a pesquisa caso esteja escrito corretamente, não é necessario escrever a primeira letra em maisculo.
        dados = self._BD.consultar("SELECT nome_vaga FROM portaldeempregos.vagas")
        vagas = dados
        entrada = input("Escreva o nome da vaga dejesada: ")
        busca = entrada.lower()
        analise = busca.split()
        
        resultados = []
        for nome in vagas:
            palavra =  nome[0].lower()
            info = palavra.split()

            for vag in info:
                for x in analise:
                    if x in vag:
                        resultados.append(nome)
                    else:
                        pass
                    
        if resultados == []:
            print("Nenhuma vaga encontrada.")
            
        else:
            for tabs in resultados:
                saida = self._BD.consultarComParametro("SELECT * FROM vagas WHERE nome_vaga = %s", parametros=(tabs[0], ))
                
                print("\nID: ", saida[0][0], "| Vaga: ", saida[0][2], "| Função: ", saida[0][3], "| Salario: R$", saida[0][4])
            
            
    def visualizar_aplicacoes(self, id):
        #nesse metodo retorna todas as aplicações, é uma otima forma de verificar os status de cada aplicação.
        aplicacoes = self._BD.consultarComParametro("SELECT * FROM portaldeempregos.aplicacao WHERE id_candidato = %s",(id,))
            
        if aplicacoes != []:
            print("-- MOSTRANDO APLICAÇÕES --\n")
            for aplicacao in aplicacoes:
                vaga = self._BD.consultar(f"SELECT nome_vaga FROM portaldeempregos.vagas WHERE id_vaga = {aplicacao[2]};")
                candidato = self._BD.consultar(f"SELECT nome_candidato FROM portaldeempregos.candidato WHERE id_candidato = {aplicacao[1]}")
                print(f"ID: {aplicacao[0]} | CANDIDATO: {candidato[0][0]}  | VAGA: {vaga[0][0]} | DATA CANDIDATURA: {aplicacao[3]} | STATUS: {aplicacao[4]}\n")
        else:
            print("Nenhuma aplicação para vaga foi encontrado.")

    def editar_cadastro_candidato(self, id):
        #Aqui é realizado um processo rapido de edição de perfil.
        
        while True:
            print("[0]Alterar Nome;")
            print("[1]Alterar Cpf;")
            print("[2]Alterar Telefone;")
            print("[3]Alterar Endereço;")
            print("[4]Alterar Email;")
            print("[5]Voltar.")
            
            valor = input("Digite a opção escolhida: ")
            
            if valor == "0":
                novoNome = input("Digite o novo nome: ")
                self._BD.manipularComParametro("UPDATE candidato SET nome_candidato = %s WHERE id_candidato = %s", (novoNome, id))
                
            elif valor == "1":
                novoCpf = input("Digite o novo Cpf: ")
                self._BD.manipularComParametro("UPDATE candidato SET cpf_candidato = %s WHERE id_candidato = %s", (novoCpf, id))
                
            elif valor == "2":
                novoTelefone = input("Digite o novo telefone: ")
                self._BD.manipularComParametro("UPDATE candidato SET telefone_candidato = %s WHERE id_candidato = %s", (novoTelefone, id))
                
            elif valor == "3":
                novoEndereco = input("Digite o novo endereço: ")
                self._BD.manipularComParametro("UPDATE candidato SET endereco_candidato = %s WHERE id_candidato = %s", (novoEndereco, id))
                
            elif valor == "4":
                novoEmail = input("Digite o novo email: ")
                self._BD.manipularComParametro("UPDATE candidato SET email_candidato = %s WHERE id_candidato = %s", (novoEmail, id))
                
            elif valor == "5":
                break
            else:
                print("Valor invalido...")
    def aplicar_para_vaga(self, id):
        #nesse metodo ele foi dividido em duas etapas:
        #1º - Analisa se a pessoa já não tem uma vaga na aplicação dejesada.
        #2º - realiza a aplicação caso ja não exista uma.

        idVaga = input("Digite o ID da vaga dejesada: ")

        teste = self._BD.consultarComParametro("SELECT id_aplicacao FROM aplicacao WHERE id_vaga = %s and id_candidato=%s", (idVaga, id))

        if teste != []:
            print("Aplicação já existe...")
        elif teste == []:
            self._BD.manipularComParametro("INSERT INTO aplicacao VALUES (DEFAULT, %s, %s, DEFAULT, DEFAULT)", (id, idVaga))    
            print("Inscrição na vaga realizada.")    