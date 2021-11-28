'''
Author: Oscar Gutierrez
Email: o.guty66@gmail.com
Date: 2021-04-08
'''
#__LIBRARIES__#


#__MAIN CODE__#
def op():
    try:
        n1 = int(input('Introduce el Primer numero: '))
        n2 = int(input('Introduce el Segundo numero: '))
    except:
        print('Uno de los valores no es valido.')
        return op()
    return [n1+n2, n1-n2]

def suma(n=10, cnt = 0):
    while n != 0:
        cnt += n
        return suma(n-1, cnt)
    print(f'La suma de los valores entre 0 y 10 es de {cnt}')

suma()

lst = op()
print(lst)

#__NOTES__#
'''
    op(): al recibir valores genera una excepción si alguno de los dos
    no es del tipo int() en la que se llama a si misma de nuevo para solicitar
    nuevos valores al usuario y devuelve una lista en la que incluye la suma
    y la resta de ambos valores

    suma(): genera la suma de los diez primeros entros de forma recursiva.
'''
#__BIBLIOGRAPHY__#
