#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 21:15:37 2021

@author: elidas
"""

#__LIBRARIES__#

#__MAIN CODE__#

def primos(n):
    p = list()#listra contenedora de los numeros primos en el rango dado
    for i in range(2, n+1):
        ctrl = 1
        for j in range(2, i):
            ctrl *= i % j
            #print(f'i={i}, j={j}, mod={i%j}')
        if ctrl != 0:
            p.append(i)
    print(p)
            
