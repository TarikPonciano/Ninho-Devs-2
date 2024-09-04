import datetime

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


def normal_user(id_user):
    vezes_tocadas = 1

    while True:
        user_menu = """
[1] - listar musicas
[2] - tocar musica
[0] - sair
"""

        print(user_menu)

        usr_opt = input("digite uma opção: ")

        if usr_opt.isdigit():
            match int(usr_opt):
                case 1:
                    show_songs()

                case 2:
                    listen_song_id_user = input(
                        "digite o id da musica que deseja tocar: "
                    )

                    listen_id_user = id_user

                    query_see_vezes_tocadas = con_db.consultations(
                        """SELECT vezes_tocadas FROM escuta WHERE id_musica = %s AND id_usuario = %s""",
                        listen_song_id_user,
                        listen_id_user,
                    )

                    query_day_listen = con_db.consultations(
                        """SELECT EXTRACT(DAY FROM dia_reproducao_musica) FROM escuta WHERE id_musica = %s""",
                        listen_song_id_user,
                    )

                    if query_see_vezes_tocadas == [] or query_day_listen[-1][0] != datetime.date.today().day:
                        query_add_escuta1 = (
                            """INSERT INTO escuta VALUES (DEFAULT, %s, %s, %s, %s)"""
                        )

                        con_db.manipulations(
                            query_add_escuta1,
                            listen_id_user,
                            listen_song_id_user,
                            vezes_tocadas,
                            datetime.date.today(),
                        )

                    else:
                        if query_day_listen[-1][0] == datetime.date.today().day:
                            if query_see_vezes_tocadas[0][0] > 0:
                                query_update_escuta = """UPDATE escuta set vezes_tocadas = (vezes_tocadas + *) 
                                    WHERE (id_usuario = %s AND id_musica = %s) AND (dia_reproducao_musica = %s)""".replace(
                                    "*", str(vezes_tocadas)
                                )

                                con_db.manipulations(
                                    query_update_escuta, id_user, listen_song_id_user, datetime.date.today()
                                )
                            else:
                                query_add_escuta2 = """INSERT INTO escuta VALUES (DEFAULT, %s, %s, %s, %s)"""

                                con_db.manipulations(
                                    query_add_escuta2,
                                    listen_id_user,
                                    listen_song_id_user,
                                    vezes_tocadas,
                                    datetime.date.today(),
                                )

                    

                case 0:
                    break

                case _:
                    print("")

            input("precione [enter] para continuar: ")
        else:
            print("use apenas numeros para selecionar uma opção pfv!")
