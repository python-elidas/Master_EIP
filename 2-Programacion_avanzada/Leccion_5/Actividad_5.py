'''
Author: Oscar Gutierrez
Email: o.guty66@gmail.com
Date: 2021-04-19
'''
# __LIBRARIES__ #
import random as rd

# __MAIN CODE__ #


def lista():
    num = list()
    while len(num) < 10:
        num.append(len(num) + 1)
    return(num)


def create_dict():
    d = dict()
    while len(d.keys()) < 4:
        n = rd.randint(65, 90)
        d[chr(n)] = n
    return(d)


def mod_dict(d):
    mod = list(d.keys())[2]
    d[mod] = chr(rd.randint(33, 95))


def add_list(d):
    d['lista'] = lista()


print(f'Lista creada medinate bucle while: {lista()}')
d = create_dict()
print(f'Diccionario aleatorio de 4 elementos: {d}')
mod_dict(d)
print(f'3er elemeneto del diccionario modificado: {d}')
add_list(d)
print(f'Adición de lista al diccionario: {d}')


# __NOTES__ #
'''
    Para la creación de la lista se aprovecha la propia longitud de la lista
    para generar los valores de la misma.
    -
    El diccionario se genera de forma aleatoria tomando los valores ascii de
    letras mayúsculas.
    -
    La modificación del tercer elemento del diccionario se realiza tomando de
    forma aleatoria un valor entre el 33 y el 95 y obteniendo su carácter
    asociado de la tabla ascii.
    -
    Haciendo uso de la primera función definida, se añade una lista al
    al diccionario con lo números del 1 al 10.
    -
    Finalmente, se imprime por pantalla el resultado de los ejercicios.
'''

# __BIBLIOGRAPHY__ #
'''
W3Schools: https://www.w3schools.com/python/ref_dictionary_values.asp
GeeksForGeeks: https://www.geeksforgeeks.org/python-get-dictionary-keys-as-a-list/
'''
