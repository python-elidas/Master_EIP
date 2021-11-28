'''
Author: Oscar Gutierrez
Email: o.guty66@gmail.com
Date: 2021-04-27
'''
# __LIBRARIES__ #
import pandas as pd
import random
import numpy as np

# __MAIN CODE__ #


def create_text():
    fw = open('file.txt', 'w')  # apertura y/o creacion del archivo
    for i in range(random.randint(1, 20)):
        line = 'Esta es la linea numero %i del archivo.\n' % i
        fw.write(line)  # escritura de la linea f¡generada
    fw.close()  # cierre del archivo


def print_text():
    create_text()  # creacion del archivo
    fr = open('file.txt', 'r')  # apertura para lectura
    for line in fr.readlines():
        print(line)  # impresion por pantalla
    fr.close()  # cierre


class CSV:
    def __init__(self):
        self.df = pd.read_csv('cotizacion.csv', delimiter=';')
        for col in self.df.columns[1:]:
            try:
                self.df[col] = self.df[col].str.replace(',', '.').astype(np.float64)
            except:
                pass
        # print(self.df)

    def get_min(self):
        print('Minimos de las columnas:')
        for col in self.df.columns[1:]:
            print(f'{col} : {self.df.min()[col]}')

    def get_max(self):
        print('Maximos de las columnas:')
        for col in self.df.columns[1:]:
            print(f'{col} : {self.df.max()[col]}')

    def get_avg(self):
        print('Media de las columnas:')
        for col in self.df.columns[1:]:
            print(f'{col} : {self.df[col].mean()}')


if __name__ == '__main__':
    print('Manipulacion del .txt')
    print_text()
    print('Empeo de Pandas')
    csv = CSV()
    csv.get_min()
    print(' ')
    csv.get_max()
    print(' ')
    csv.get_avg()

# __NOTES__ #
'''
    Por costumbre he cogido al trabajar con ficheros usar la siguiente notacion:
        fr = archivo de lectura
        fa = archivo de adición
        fw = archivo de escritura

    A la hora de manejar el .csv con pandas, se ha creado una clase CSV con
    las funciones get_min, get_max y get_avg
'''

# __BIBLIOGRAPHY__ #
'''
    Material del master
    Geeks for Geeks :   https://www.geeksforgeeks.org/
    This Pointer    :   https://thispointer.com/
'''
