'''
Author: Oscar Gutierrez
Email: o.guty66@gmail.com
Date: 2021-04-28
'''
# __LIBRARIES__ #
import threading as th
import random as rd

# __MAIN CODE__ #


def factorial(n, res=1):
    while n != 1:
        res = multiply(n, res)
        n -= 1
        return factorial(n, res)
    return(res)


def multiply(n, m, res=0):
    while n != 0:
        res += m
        n -= 1
        return multiply(n, m, res)
    return res


def run(id):
    n = rd.randint(1, 20)
    print(f'Hilo {id}: {n}! = {factorial(n)}')
    return


def multitask():
    for i in range(rd.randint(1, 5)):
        t = th.Thread(target=run, args=[i])
        t.start()


if __name__ == '__main__':
    multitask()

# __NOTES__ #
'''
    En este caso se ha realizado una funcion recursiva factorial que ejecuta
    una segunda funcion recursiva multiply. Estas son llamadas de froma
    simultánea por un numero aleatorio entre 1 y 5 de hebras y nos muestra
    por pantalla a que hebra le corresponde el factorial de cada numero.
'''
# __BIBLIOGRAPHY__ #
'''
    Los apuntes proporcionados
'''
