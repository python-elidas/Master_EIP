'''
  Author: Python_Elidas
  Email: Pyro.elidas@gmail.com
  Python Version: 3.6.9
  Date: 2021-09-16T18:34:35.582Z
  Version: 0.0.1
'''

# __LIBRARIES__ #
import pymongo as pym
from datetime import datetime

# __MAIN CODE__ #


class Mongo:
    def __init__(self, host, port):
        # creamos la conexion con el cliente
        self.client = pym.MongoClient(host, port)
        # print(self.client)

    def conect_db(self, db):
        # establecemos la conexión a la base de datos establecida
        self.db = self.client[db]
        # print(self.db.user)

    def conect_coll(self, coll):
        # conectamos con la coleccion deseada
        self.coll = self.db[coll]

    def insert_info(self, info):  # info as variable & type(info) == list
        if type(info) is list:
            for elem in info:
                try:
                    self.coll.insert(elem)  # type(elem) = dict()
                except TypeError:
                    print(f'El tipo de dato de "{elem}" no es correcto.')
        else:
            print('TypeError: Introduced data must be a list.')

    def update_info(self, ref, info):  # info == {key: value}
        if type(ref) is dict:
            self.coll.update(ref, {'$set': info})
        # recorremos los datos para buscar la referencia
        else:
            for dato in self.coll.find({}):
                for key in list(dato.keys()):
                    if dato[key] == ref:
                        self.coll.update({key: ref}, {'$set': info})

    def print_collection(self):
        for dato in self.coll.find({}):
            print(dato)

    def find_group(self, ref, min, max):
        group = list()
        for dato in self.coll.find({}):
            if min <= dato[ref] and dato[ref] <= max:
                group.append(dato)
        return group

    def delete_info(self, info):
        if type(info) is dict:
            self.coll.delete_one(info)
        # recorremos los datos para buscar la referencia
        else:
            for dato in self.coll.find({}):
                for key in list(dato.keys()):
                    if dato[key] == info:
                        self.coll.delete_one({key: info})


if __name__ == '__main__':
    db = Mongo('localhost', 27017)
    db.conect_db('actividad')
    db.conect_coll('notas')
    info = [
        {'nombre': 'Pedro López', 'edad': 25, 'email': 'pedro@eip.com',
         'nota': 5.2, 'fecha': datetime.now()},
        {'nombre': 'Julia Garciía', 'edad': 22, 'email': 'julia@eip.com',
         'nota': 7.3, 'fecha': datetime.now()},
        {'nombre': 'Amparo Mayoral', 'edad': 28, 'email': 'amparo@eip.com',
         'nota': 8.4, 'fecha': datetime.now()},
        {'nombre': 'Juan Martínez', 'edad': 30, 'email': 'juan@eip.com',
         'nota': 6.8, 'fecha': datetime.now()}
    ]
    db.insert_info(info)
    update = [
        ({'nombre': 'Amparo Mayoral'}, {'nota': 9.3}),
        ('Juan Martínez', {'nota': 7.2})
    ]
    for elem in update:
        db.update_info(elem[0], elem[1])
    db.print_collection()
    for dato in db.find_group('nota', 7, 7.5):
        print(dato)
    db.delete_info('Pedro López')

# __NOTES__ #
'''
  >
'''


# __BIBLIOGRAPHY__
'''
  >
'''
