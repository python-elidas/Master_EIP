# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 18:20:30 2021

@author: elidas

Tema: Estructuras de control
"""

#__IF__#
name = input('Cual es tu nombre? ')

if name == 'Oscar':
    print('Welcome, Master')
else:
    print('Welcome, extrainger')
    
numero = int(input('Introduce un numero: '))

if numero < 10:
    print('Es menor de 10')
    if numero < 5:
        print('Es menor de 5')
    else:
        print('Esta entre 5 y 10')
else:
    print('Es mayor de 10')

#__FOR__#
for i in range(10):
    print(i)
    
#val = int(input('Introduce un numero: '))
for i in range(1,11): 
    for j in range(1,11):
        print(f'{i} x {j} = {i * j}')
    print('\n')


#__OTROS__#
'''range(x,y,z)
        x = numero de inicio
        y = numero de parada 
        z = paso entre valores
        range(10, 1, -1) seria un range decreciente
   '''



