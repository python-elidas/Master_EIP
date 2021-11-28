'''
Author: Oscar Gutierrez
Email:  o.guty66@gmail.com
Date:   2021-06-23
Python Version: 3.6.9
code version: 0.0.1
'''
# __LIBRARIES__ #
import pdb

# __MAIN CODE__ #
ex = [[2, 4, 1], [1, 2, 3, 4, 5, 6, 7, 8], [100, 250, 43]]


def mayor(list):
    max = 0
    for elem in list:
        if elem > max:
            max = elem
    return max


pdb.set_trace()
maximos = list(map(mayor, ex))
print(maximos)


def primo(n):
    for i in range(1, n):
        if n % i == 0 and i != 1:
            return False
    return True


def verify_value():
    while True:
        try:
            n = int(input('Introduzca un valor (-1 para finalizar):\n>>> '))
            if n < 0 and n != -1:
                raise SyntaxError
            return n
        except NameError:
            print('Valor no reconocido.')
        except SyntaxError:
            print('Valor no reconocido.')


def find_primos():
    val = list()
    n = 0
    while n != -1:
        n = verify_value()
        val.append(n)
    primos = list(filter(primo, val[:-1]))
    print(primos)


find_primos()


# __NOTES__ #
'''

'''
# __BIBLIOGRAPHY__ #
'''

'''
