'''
Author: Oscar Gutierrez
Email: o.guty66@gmail.com
Date: @timestamp@
'''
#__LIBRARIES__#


#__MAIN CODE__#
def print_N():
    n = int(input('Introduce un numemro: '))
    for i in range(n+1):
        print(i)

def gen_dict():
    letters = dict()
    ind = 65
    for i in range(26):
        letters[chr(ind+i)] = ind + i
    return letters

def print_touple():
    ascii = gen_dict()
    for elem in ascii.items():
        print(elem)

def print_dict():
    ascii = gen_dict()
    for key in ascii.keys():
        print(f'{key} : {ascii.get(key)}')

print_N()
print_dict()

#__NOTES__#
'''
    gen_dict(): genera un dicionario con las letras mayusculas a partir del
    codigo ascii de cada una.

    print_touple(): imprme los valores del diccionario en forma de tupla,
    (key, value)

    print_dict(): imprime los valores del diccionario de la forma 'key : value'
'''
#__BIBLIOGRAPHY__#
