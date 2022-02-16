#__Librerias__#
import paramiko as pk
from paramiko import SSHClient
import getpass
from toolPing import ping
from toolNmap import nmapTool

#__AUXILIARS__#
def login_ssh(ip, user):
    try:
        pasw = getpass.getpass(f'[+] Introduzca la contraseña para la el usuario {user}:\n>>> ')
        return client.connect(ip, username=user, password=pasw)
    except:
        login_ssh(ip, user)
    

#__MAIN CODE__#
nm = nmapTool()
# Busquemos las IPs con servicios ssh levantados:
iprange = input('[+] Introduzca la IP de su maquina:\n>>> ')
r0 = 10
rf = 255#int(iprange.split('.')[-1]) + 30
print('[-] Searching for IPs ...')
ips = ping(iprange, r0=r0, rf=rf, screen=False, var=True)
ips.pop(ips.index(iprange))
ssh = list()
print('[-] Searching for SSH Banners ...')
for ip in ips:
    for banner in nm.getBanners(ip, ports=['22',],  to_screen=True, to_var=True):
        # print(banner)
        if 'SSH' in banner[1]:
            ssh.append(ip)
            
# Mostremos las IPs accesibles
print('[#] Se han hallado las siguientes IPs con servicios ssh:')
for ip in ssh:
    print(f'[{ssh.index(ip)}] {ip}')
sel = input('[+] Seleccione una o varias (separadas por ",") IPs:\n>>> ').split(',')

# conectemos con las IPs seleccionadas
clients = list()
for i in sel:
    ip = int(i)
    client = pk.SSHClient()
    client.set_missing_host_key_policy(pk.AutoAddPolicy())
    user = input(f'[+] Introduzca el usuario para la IP {ssh[ip]}:\n>>> ')
    login_ssh(ssh[ip], user)
    clients.append((ssh[ip], client))
    
# Interactuemos con las maquinas
command = 'cat /etc/issue'
while command != 'exit()':
    for client in clients:
        print(f'[-] Response from {client[0]}:')
        stdin, stdout, stderr = client[1].exec_command(command)
        print('[*] STDOUT')
        for line in stdout.readlines():
            print(f'[*] {line}')
    
        print('[-]====================[-]\n')
    command = str(input('[+] Command:\n>>> '))