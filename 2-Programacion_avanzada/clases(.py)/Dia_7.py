'''
    Author: Oscar Gutierrez
    Email: o.guty66@gmail.com
    Date: 2021-04-22
'''
# __LIBRARIES__ #
import sqlite3
from sqlite3 import Error

# __MAIN CODE__ #


def create_new_DB(route):
    conn = None  # creamos una variable para almacenar el estado de la conexion
    try:  # caso de omitir la ruta se crea en el directorio actual
        conn = sqlite3.connect(route)  # crea la BD en la ruta especificada
        print(f'SQLite verion: {sqlite3.version}\nConnection: {conn}')
        return (conn)
    except Error as e:
        print(e)
    '''finally:
        if conn:
            conn.close()  # termina la conexion'''


def create_table(conn):
    try:
        cursorObj = conn.cursor()  # objeto que permite interactuar con la tabla
        cursorObj.execute(
            'Create table Alumnos(DNI varchar primary key, Nombre varchar, Apellido varchar, nota float)')
        print('Tabla Alumnos creada.')
        conn.commit()  # finaliza las acciones pendientes con la BD
    except Error as e:
        print(e)


def run():
    db = create_new_DB(r'/home/elidas/Escritorio/Master/Programacion_avanzada/Leccion_7/My_db.db')
    create_table(db)


if __name__ == '__main__':
    run()

# __NOTES__ #
'''
    El objeto conn representa la puerta de enlace con la base de datos.
    El objeto cursorObj representa el actuador, nos permite interactuar con las
    tablas.
    cursorObj.execute('Create table <nombre>(<campo1> <varType>, <campo2>
    <varType>, ...)'

'''

# __BIBLIOGRAPHY__ #
