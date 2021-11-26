#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 21:15:37 2021

@author: elidas
"""

#__LIBRARIES__#

#__MAIN CODE__#
class Primos():
    def __init__(self, num):
        self.num = num
        self.p = list()#almacena la lista bde primos entre 1 y n
        self.primos()
        
    def primos(self):
        for i in range(2, self.num+1):
            ctrl = 1
            for j in range(2, i):
                ctrl *= i % j
                #print(f'i={i}, j={j}, mod={i%j}')
            if ctrl != 0:
                self.p.append(i)
        print(self.p)
            
n = int(input('Introduce un numero: '))
p = Primos(n)