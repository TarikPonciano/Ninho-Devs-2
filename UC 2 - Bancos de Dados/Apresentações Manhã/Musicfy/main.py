import admin_user_i
import normal_user_i
from conec_musicfy import Connection

config = {
    "user": "root",
    "host": "127.0.0.1",
    "password": "mysql",
    "database": "musicfy",
}

con_db = Connection(**config)


def show_songs():
    query_show_songs = """SELECT * FROM musica"""

    result = con_db.consultations(query_show_songs)

    for songs in result:
        print(*songs)


menu = """
[1] - cadastrar
[2] - logar
[0] - Sair
"""

while True:
    print(menu)

    usr_opt = input("digite uma opção: ")

    if usr_opt.isdigit():
        match int(usr_opt):
            case 1:
                reg_usr_name = input("digite seu nome: ")
                reg_usr_login = input("digite o nome do seu login: ")
                reg_usr_born = input(
                    "digite sua data de nascimento nesse formato 00/00/0000 : "
                )
                reg_usr_password = input("digite uma senha: ")
                age_usr_born = reg_usr_born.split("/")
                usr_age = 2024 - int(age_usr_born[-1])

                result_logins = con_db.consultations(
                    """SELECT login_usuario FROM usuario WHERE login_usuario = %s """,
                    reg_usr_login,
                )

                if result_logins != []:
                    print("login ja está sendo usado")
                elif usr_age < 9:
                    print("voce precisa ser maior de 9 anos para poder se cadastrar!")
                else:
                    query_add_user = """
                                INSERT INTO usuario (id_usuario, nome_usuario, login_usuario, senha_usuario, role_usuario,idade_usuario) VALUES(DEFAULT, %s, %s, SHA(%s), 'user', %s);"""

                    con_db.manipulations(
                        query_add_user,
                        reg_usr_name,
                        reg_usr_login,
                        reg_usr_password,
                        usr_age,
                    )
                    print("usuario cadastrado com sucesso!")

            case 2:
                log_usr_name = input("digite seu login: ")
                log_usr_password = input("digite sua senha: ")

                result = con_db.consultations(
                    "SELECT role_usuario, id_usuario FROM usuario WHERE login_usuario = %s AND senha_usuario = SHA(senha_usuario) = %s",
                    log_usr_name,
                    log_usr_password,
                )

                if result[0][0] == "admin":
                    admin_user_i.admin_user()

                elif result[0][0] == "user":
                    normal_user_i.normal_user(result[0][1])

                else:
                    print("usuario nao cadastrado")

            case 0:
                break

            case _:
                print("")

        input("precione [enter] para continuar: ")
    else:
        print("use apenas numeros para selecionar uma opção pfv!")
