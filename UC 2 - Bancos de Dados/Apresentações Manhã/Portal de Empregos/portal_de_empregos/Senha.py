import getpass
import hashlib

class Senha:
    def __init__(self, credentials_file='credentials.txt'):
        self.credentials_file = credentials_file

    def hash_senha(self, senha):
        return hashlib.sha256(senha.encode()).hexdigest()
    
    def verificar_senha(self, armazenar_senha_hash, senha_oferecida):
        return armazenar_senha_hash == self.hash_senha(senha_oferecida)
    
    def registrar_usuario(self, nome, senha):
        with open(self.credentials_file, 'a') as f:
            senha_hash = self.hash_senha(senha)
            f.write(f'{nome},{senha_hash}\n')

    def autenticar_usuario(self, nome, senha):
        try:
            with open(self.credentials_file, 'r') as f:
                for line in f:
                    nome_armazenado, senha_armazenada_hash = line.strip().split(',')
                    if nome_armazenado == nome:
                        return self.verificar_senha(senha_armazenada_hash, senha)
        except FileNotFoundError:
            print("Arquivo de credenciais não encontrado.")
        return False
    
    def Autenticação():
        usuario_manager = Senha()

        while True:
            print("--- menu admistrador ---")
            print("1- registrar Usuario e senha")
            print("2. Autenticar Usuario e senha")
            print("3. Sair.")

            
            escolha = input("Escolha uma opção: ").strip()

            if escolha == '1':
                nome = input("Digite um nome de usuário: ")
                senha = getpass.getpass("Digite uma senha: ")
                usuario_manager.registrar_usuario(nome, senha)
                print("Usuário registrado com sucesso!")

            elif escolha == '2':
                nome = input("Digite um nome de usuário: ")
                senha = getpass.getpass("Digite a senha: ")
                if usuario_manager.autenticar_usuario(nome, senha):
                    print("Autenticação bem-sucedida!")
                    return True  # Encerra o loop após autenticação bem-sucedida
                else:
                    print("Falha na autenticação. Tente novamente.")

            elif escolha == '3':
                print("Saindo...")
                return False
  
            else:
                print("Opção inválida. Tente novamente.")

