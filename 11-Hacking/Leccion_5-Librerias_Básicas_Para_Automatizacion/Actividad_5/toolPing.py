#__LIBRARIES__#
from email import message
from subprocess import Popen, PIPE
import os

#__AUXILIARS__#
def verify(ip):
    ip = ip.split('.')
    if len(ip) > 4:
        return False
    for sec in ip:
        if 0 > int(sec) or int(sec) > 255:
            return False
    return True

#__MAIN CODE__#
def ping(iprange, r0=1, rf=255, to_text=False, ver=False, screen=True, var=False):
    # Establecemos el programa a ejecutar
    program = '/bin/ping' 
    if os.name == 'nt':
        program = 'ping'
    # Adaptamos la IP recibida
    if len(iprange.split('.')) == 4:
        iprange = '.'.join(iprange.split('.')[:-1])
    elif iprange[-1] == '.':
        iprange = iprange[:-1]
    if verify(iprange):
        ips=list()
        for ip in range(r0,rf):
            ipAddress = f'{iprange}.{str(ip)}'
            if screen:
                print(f'[-] Scanning {ipAddress}')
            subprocess = Popen(
                [program, '-c 1', ipAddress], # lo que va a ejecutar (Nota1)
                stdin=PIPE, # Flujo de entrada
                stdout=PIPE, # Flujo de salida
                stderr=PIPE # El error entrada
            )
            stdout, stderr = subprocess.communicate(input=None) # Nota_2
            if 'bytes from' in stdout.decode():
                if screen:
                    print(f'[*] The Ip Address {stdout.decode().split()[1]} has responded with a ECHO_REPLY')
                if to_text:
                    with open('ips.txt', 'a') as fa:
                        fa.write(f'{stdout.decode().split()[1]}\n')
                if var:
                    print(f'[*] {ipAddress}')
                    ips.append(ipAddress)
                if ver: #solo pata una única IP
                    return True
        if not len(ips) == 0:
            return ips
    else:
        raise SyntaxError('Introduced IP is not valid.')


#__SELF RUN__#
if __name__ == '__main__':
    #! Incluir argumentos para las entradas de la funcion.add()
    import sys, argparse
    parser = argparse.ArgumentParser(description='Ping tool')
    parser.add_argument('-r', '--startRange', required=False, default=1, help='The first number of the IP segment to realize the ping')
    parser.add_argument('-R', '--endRange', required=False, default=255, help='The last number of the IP segment to realize the ping')
    parser.add_argument('-r', '--startRange', required=False, help='The first number of the IP segment to realize the ping')
    
    args = parser.parse_args()
    ping(
        sys.argv[1],
        r0=args.startRange,
        rf=args.endRange
    )

#__NOTAS__#
'''
Nota_1:
    Se le están diciendo 3 cosas al proceso:
        1.- El programa que debe ejecutar, el ping
        2.- La configuración del programa que va a ejecutar, -c 1
            -c 1 básicamente lo que indica es que va a enviar un único paquete
        3.- El objetivo, la ip que toque

Nota_2:
    El hecho de que el input sea none en el communicate le indica que es un
    comando no interactivo, que se ejecuta sin necesidad de interaccion del 
    usuario.
'''

#__BIBLIOGRAPHY__#
'''

'''