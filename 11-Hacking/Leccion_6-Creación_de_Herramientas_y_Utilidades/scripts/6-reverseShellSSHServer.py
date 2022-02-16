import socket 
import paramiko 
import threading 
import sys 

if len(sys.argv) != 3: 
    print("usage SSHServer.py <interface> <port>") 
    exit() 
 
server_key = paramiko.RSAKey(filename='/home/adastra/.ssh/id_rsa',password='password') 
 
class Server (paramiko.ServerInterface): 
   def check_channel_request(self, kind, chanid): 
       if kind == 'session': 
           return paramiko.OPEN_SUCCEEDED 
       return paramiko.OPEN_FAILED_ADMINISTRATIVELY_PROHIBITED 
   def check_auth_password(self, username, password): 
       if (username == 'adastra') and (password == 'adastra'): 
           return paramiko.AUTH_SUCCESSFUL 
       return paramiko.AUTH_FAILED 
 
try: 
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
    sock.bind((sys.argv[1], int(sys.argv[2]))) 
    sock.listen(100) 
    print('[+] Listening ...') 
    client, addr = sock.accept() 
except Exception as e: 
    print(('[-] Exception: ' + str(e))) 
    sys.exit(1) 
print('[+] New Client!') 
 
try: 
    t = paramiko.Transport(client) 
    try: 
            t.load_server_moduli() 
    except: 
        raise 
    t.add_server_key(server_key) 
    server = Server() 
    try: 
        t.start_server(server=server) 
    except paramiko.SSHException as x: 
        raise 
 
    chan = t.accept(20) 
    print((chan.recv(1024))) 
    chan.send('SSH Connection Established!') 
    while True: 
        command= input(">: ").strip('n') 
        if command.lower() == 'exit': 
            print("Exiting...") 
            chan.send('exit') 
            break 
        chan.send(command) 
        print((chan.recv(1024))) 
 
except Exception as e: 
    print(('[-] Caught exception: ' + str(e))) 
    try: 
        t.close() 
    except: 
        pass 
    sys.exit(1)
