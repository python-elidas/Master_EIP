'''
Author: Oscar Gutierrez
Email: o.guty66@gmail.com
Date: 2021-04-19
'''
# __LIBRARIES__ #


# __MAIN CODE__ #
class Calculadora:
    def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2

    def sumar(self):
        print(f'{self.n1} + {self.n2} = {self.n1+self.n2}')

    def multiplicar(self):
        print(f'{self.n1} x {self.n2} = {self.n1*self.n2}')

    def restar(self):
        print(f'{self.n1} - {self.n2} = {self.n1-self.n2}')

    def dividir(self):
        if self.n2 == 0:
            print(f'{self.n1} / {self.n2} = Infinito')
        else:
            print(f'{self.n1} / {self.n2} = {self.n1/self.n2}')


calc = Calculadora(15, 5)
calc.sumar()
calc.multiplicar()
calc.restar()
calc.dividir()

# __NOTES__ #


# __BIBLIOGRAPHY__ #
