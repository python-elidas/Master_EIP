'''
Author: Oscar Gutierrez
Email: o.guty66@gmail.com
Date: 2021-04-22
'''
# __LIBRARIES__ #
import time
import sqlite3
from sqlite3 import Error

# __MAIN CODE__ #


class SQL:
    def __init__(self):
        self.db_name = str(input('Indica el nombre de la base de datos: ')) + '.db'
        self.create_connexion()
        print('Conexion establecida con exito.')
        print('Creando tablas...')
        self.cursorObj = self.conn.cursor()
        self.create_tables()

    def create_connexion(self):
        self.conn = None  # creamos el objeto conect
        try:  # caso de omitir la ruta se crea en el directorio actual
            self.conn = sqlite3.connect(self.db_name)  # crea la BD en la ruta especificada
        except Error as e:
            print(e)

    def create_tables(self):
        try:
            self.cursorObj.execute(
                'Create table Alumnos(DNI varchar primary key, Nombre varchar, Apellido varchar, Nota float)')
            self.cursorObj.execute(
                'Create table Profesores(Correo varchar primary key, Nombre varchar)')
            time.sleep(3)
            print('Tablas creadas con exito.')
        except:
            pass

    def insert_Alumnos(self):
        dni = input('Introduce el dni: ')
        nombre = input('Introduce el Nombre: ')
        apellido = input('Introduce el Apellido: ')
        nota = input('Introduce el Nota: ')
        val = (dni, nombre, apellido, nota)
        self.cursorObj.execute(
            'insert into Alumnos(DNI, Nombre, Apellido, Nota) values(?, ?, ?, ?)', val)
        self.conn.commit()

    def insert_Profesores(self):
        correo = input('Introduce el correo: ')
        nombre = input('Introduce el Nombre: ')
        val = (correo, nombre)
        self.cursorObj.execute(
            'insert into Profesores(Correo, Nombre) values(?, ?)', val)
        self.conn.commit()

    def update(self):
        tab = input('Introduce la Tabla (Alumnos, Profesores): ')
        if tab == 'Alumnos':
            key = 'DNI'
            col = input('Introduce la Columna (Nombre, Apellido, Nota): ')

        elif tab == 'Profesores':
            key = 'correo'
            col = 'Nombre'
        var1 = input('Introduce el nuevo valor para %s: ' % col)
        var2 = input('Introduce la referencia %s: ' % key)
        val = (var1, var2)
        self.cursorObj.execute('update %s set %s = ? where %s = ?' % (tab, col, key), val)
        self.conn.commit()

    def list(self):
        tab = input('Introduce la Tabla (Alumnos, Profesores): ')
        self.cursorObj.execute('select * from %s' % tab)
        filas = self.cursorObj.fetchall()
        for fila in filas:
            print(fila)

    def delete(self):
        tab = input('Introduce la Tabla (Alumnos, Profesores): ')
        if tab == 'Alumnos':
            key = 'DNI'
        elif tab == 'Profesores':
            key = 'correo'
        var2 = input('Introduce la referencia %s: ' % key)
        val = (var2)
        self.cursorObj.execute('delete from %s where %s = ?' % (tab, key), val)


def run():
    db = SQL()
    db.insert_Alumnos()
    db.insert_Profesores()
    db.update()
    db.list()
    db.delete()


if __name__ == '__main__':
    run()

# __NOTES__ #


# __BIBLIOGRAPHY__ #
