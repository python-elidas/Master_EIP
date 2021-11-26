# -*- coding: utf-8 -*-

#__LIBRARIES__#
from rpy2.robjects import r as ro

#__MAIN CODE__#
class Primos():
    def __init__(self, num):
        self.num = num
        self.r_prime()
        
    def r_prime(self):
        #ro.assign('n', self.num)
        r_code = '''
        prime <- function(n) {
                if (n >= 2) {
                        x = seq(2, n)
                        prime_nums = c()
                        for (i in seq(2, n)) {
                                if (any(x == i)) {
                                        prime_nums = c(prime_nums, i)
                                        x = c(x[(x %% i) != 0], i)
                                }
                        }
                                return(prime_nums)
                }
                                else {
                                        stop("Input number should be at least 2.")
                                }
        }
        '''
        ro(r_code)
        prime_py = ro.globalenv['prime']    
        prime_py(self.num)
       
            
n = int(input('Introduzca un numero: '))
prime = Primos(n)
        

#__NOTES__#
            
#__BIBLIOGRA__#