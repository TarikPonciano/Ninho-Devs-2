import mysql.connector

class Connection:
    def __init__(self, user, host, password, database) -> None:
        self._user = user
        self._host = host
        self._password = password
        self._database = database

        self._con = None
        self._cursor = None
    

    def start_connection(self):
        try:
            self._con = mysql.connector.connect(user = self._user, host = self._host, password = self._password, database = self._database)
        except mysql.connector.Error as err:
            print(err)
        except Exception as gerr:
            print(gerr)
        try:
            self._cursor = self._con.cursor()
        except mysql.connector.Error as err:
            print(err)
        except Exception as gerr:
            print(gerr)

    def close_connection(self):
        try:
            self._cursor.close()
        except mysql.connector.Error as err:
            print(err)
        except Exception as gerr:
            print(gerr)

        try:
            self._con.close()
        except mysql.connector.Error as err:
            print(err)
        except Exception as gerr:
            print(gerr)

    def setup_db(self, query_db, query_add_values = None, *args):
        try:
            self.start_connection()
            db_name = query_db.split(" ")

            self._cursor.execute(f"DROP DATABASE IF EXISTS {db_name[-1]}")
            self._cursor.execute(query_db)

            self._cursor.execute(f"USE {db_name[-1]}")
            for q in args:
                self._cursor.execute(q)
                self._con.commit()
    
            self._cursor.execute(f"USE {db_name[-1]}")
            self._cursor.execute(query_add_values)
            self._con.commit()

        except mysql.connector.Error as err:
            print(err)
        except Exception as gerr:
            print(gerr)

        self.close_connection()

    def consultations(self, query, *args):
        try:
            result = []
            self.start_connection()

            self._cursor.execute(query, (*args,))

            result = self._cursor.fetchall()

        except mysql.connector.Error as err:
            print(err)
        except Exception as gerr:
            print(gerr)

        self.close_connection()

        return result

    def manipulations(self, query, *args):
        try:
            self.start_connection()

            self._cursor.execute(query, (*args,))

            self._con.commit()
        except mysql.connector.Error as err:
            print(err)
        except Exception as gerr:
            print(gerr)

        self.close_connection()

    