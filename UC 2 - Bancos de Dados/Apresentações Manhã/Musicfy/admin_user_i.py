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


def admin_user():
    while True:
        admin_menu = """
[1] - adicionar musica
[2] - listar musicas
[3] - listar usuarios
[4] - ver tempo total tocado de musica pelo usuario 
[5] - ver tempo total tocado de musica pelo usuario por musica especifica
[6] - ver tempo total tocado de musica pelo usuario por usuario especifico
[0] - sair
"""

        print(admin_menu)

        usr_opt = input("digite uma opção: ")

        if usr_opt.isdigit():
            match int(usr_opt):
                case 1:
                    song_name = input("digite o nome da musica: ")
                    type_song = input("digite o tipo de musica: ")
                    duration_song = input(
                        "digite a duração da musica nesse formato 0.00 :"
                    )

                    query_add_song = (
                        """INSERT INTO musica VALUES (DEFAULT, %s, %s, %s)"""
                    )

                    con_db.manipulations(
                        query_add_song, song_name, type_song, duration_song
                    )

                case 2:
                    show_songs()

                case 3:
                    query_list_users = """SELECT id_usuario, login_usuario, idade_usuario FROM usuario"""

                    result_users = con_db.consultations(query_list_users)

                    print("id_usuario | login_usuario | idade_usuario")
                    for results in result_users:
                        print(results)

                case 4:
                    query_see_all_time_songs = """SELECT usuario.id_usuario, musica.nome_musica, (duracao_musica * vezes_tocadas) as tempo_total_reproduzido
                    FROM escuta
                    LEFT JOIN musica ON musica.id_musica = escuta.id_musica
                    INNER JOIN usuario ON usuario.id_usuario = escuta.id_usuario"""

                    result_total = con_db.consultations(query_see_all_time_songs)

                    print("id_usuario | nome_musica | tempo_total_reproduzido_musica")
                    for results in result_total:
                        print(results)

                case 5:
                    id_espec_song = input("digite o id da musica: ")
                    query_see_espe_time_song = """SELECT musica.id_musica, musica.nome_musica, vezes_tocadas, duracao_musica, (duracao_musica * vezes_tocadas) as tempo_total_reproduzido
                    FROM escuta
                    LEFT JOIN musica ON musica.id_musica = escuta.id_musica
                    WHERE musica.id_musica = %s"""

                    result_espec = con_db.consultations(
                        query_see_espe_time_song, id_espec_song
                    )

                    print(
                        "id_musica | nome_musica | vezes_tocadas | duração_musica | tempo_total_reproduzido_musica"
                    )
                    for results in result_espec:
                        print(results)

                case 6:
                    id_espec_usr_song = input("digite o id do usuario: ")
                    query_see_espe_time_song = """SELECT musica.id_musica, musica.nome_musica, vezes_tocadas, duracao_musica, (duracao_musica * vezes_tocadas) as tempo_total_reproduzido
                    FROM escuta
                    LEFT JOIN musica ON musica.id_musica = escuta.id_musica
                    INNER JOIN usuario ON usuario.id_usuario = escuta.id_usuario
                    WHERE usuario.id_usuario = %s"""

                    result_espec_usr = con_db.consultations(
                        query_see_espe_time_song, id_espec_usr_song
                    )
                    print(
                        "id_musica | nome_musica | vezes_tocadas | duração_musica | tempo_total_reproduzido_musica"
                    )
                    for results in result_espec_usr:
                        print(results)

                case 0:
                    break
                case _:
                    print("")

            input("precione [enter] para continuar: ")
        else:
            print("use apenas numeros para selecionar uma opção pfv!")
