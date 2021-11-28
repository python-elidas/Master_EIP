'''
  Author: Python_Elidas
  Email: Pyro.elidas@gmail.com
  Python Version: 3.6.9
  Date: 2021-09-15T20:11:57.450Z
  Version: 0.0.1
'''

# __LIBRARIES__ #
import psycopg2 as psy  # por hacerlo mas comodo
from psycopg2 import sql
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


# __MAIN CODE__ #
class Postgres:
    def __init__(self, name):
        self.name = name
        self.conect()
        self.edic = ['Uno', 'Dos', 'Tres']
        self.notas = [
            ('Isabel Maniega', 30, 5.6, 1), ('José Manuel Peña', 30, 7.8, 1),
            ('Pedro López', 25, 5.2, 2), ('Julia García', 22, 7.3, 1),
            ('Amparo Mayora', 28, 8.4, 3), ('Juan Martínez', 30, 6.8, 3),
            ('Fernando López', 35, 6.1, 2), ('María Castro', 41, 5.9, 3)
        ]

    def conect(self):
        try:
            # conectemonos a la base de datos:
            self.conn = psy.connect(
                database=self.name,
                user='Elidas', password='EIPpython',
                host='localhost', port=5432
            )
            # creamos el cursor
            self.cur = self.conn.cursor()
            return True

        except psy.Error:
            # Creamos la conexión
            conn = psy.connect(
                user='Elidas', password='EIPpython',
                host='localhost', port=5432
            )

            conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

            # creamos el cursor
            cur = conn.cursor()

            # creamos la base de datos:
            cur.execute(
                sql.SQL('CREATE DATABASE {};').format(
                    sql.Identifier(self.name)
                )
            )  # Nota 1.0 & 1.1

            return self.conect()

    def create_table(self):  # creamos las dos tablas
        try:
            self.cur.execute(
                "CREATE TABLE edicion( \
                    IDedic serial, numero varchar);"
            )
            self.cur.execute(
                "CREATE TABLE notas( \
                    IDnotas serial, name varchar(120),\
                    edad int, notas real, IDedic int);"
            )

        except psy.Error as e:
            print('Error Crear tabla: %s', str(e))

        self.conn.commit()

    def fill_edic(self, cnt=0):
        while cnt != len(self.edic):
            try:
                self.cur.execute("INSERT INTO edicion VALUES\
                    (nextval('edicion_idedic_seq'), %s)",
                                 (self.edic[cnt],))

            except psy.Error as e:
                print('Error Insertar dato: %s', str(e))
            cnt += 1
            self.conn.commit()
            return self.fill_edic(cnt)
        return True

    def fill_notas(self, cnt=0):
        while cnt != len(self.notas):
            try:
                self.cur.execute("INSERT INTO notas VALUES\
                    (nextval('notas_idnotas_seq'), %s, %s, %s, %s)",
                                 self.notas[cnt])  # ('Oscar', 25, 5.0))

            except psy.Error as e:
                print('Error Insertar dato: %s', str(e))
            cnt += 1
            self.conn.commit()
            return self.fill_notas(cnt)
        return True

    def update(self):
        try:
            self.cur.execute("UPDATE notas SET notas=6.4 WHERE\
            idnotas=3")
            self.cur.execute("UPDATE notas SET notas=5.2 WHERE\
            idnotas=8")

        except psy.Error as e:
            print('Error Actualizar dato: %s', str(e))

        self.conn.commit()

    def print_table(self, table):
        try:
            self.cur.execute(f"SELECT * FROM {table};")
            rows = self.cur.fetchall()
            print(f'**{table}**')
            for row in rows:
                print(f'\t{row}')

        except psy.Error as e:
            print('Error Actualizar dato: %s', str(e))

    def find_range(self, min, max, column, table):
        self.cur.execute(f"SELECT * FROM {table} WHERE\
         {column} >= {min} AND {column} <= {max}")
        print(
            f"Los registros de la tabla {table} cuyos valores en la columna {column} estan entre {min} y {max} son: ")
        rows = self.cur.fetchall()
        for row in rows:
            print(f'\t{row}')

    def delete(self):
        try:
            self.cur.execute("DELETE FROM notas WHERE\
            name='Pedro López';")
        except psy.Error as e:
            print('Error eliminar dato: %s', str(e))

        self.conn.commit()

    def close_conection(self):
        self.cur.close()
        self.conn.close()


if __name__ == '__main__':
    db = Postgres('actividad_v2')
    # db.create_table()
    # db.fill_edic()
    # db.fill_notas()
    # db.update()
    # db.print_table('edicion')
    # db.print_table('notas')
    # db.find_range(5, 6.5, 'notas', 'notas')
    # db.find_range(2, 2, 'idedic', 'notas')
    db.delete()

# __NOTES__ #
'''
    nota 1.0: sql.SQL y sql.Identifier se emplean para evitar ataques de tipo
        SQL inyection
    Nota 1.1: ya que el nombre actividad lo hemos empleado para crear la base
        de datos mediante adminer, a esta le pondremos el apellido v2 de
        version 2
'''


# __BIBLIOGRAPHY__
'''
  >
'''
