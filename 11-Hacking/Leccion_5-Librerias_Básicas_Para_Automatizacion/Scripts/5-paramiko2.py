'''
public key authentication:
keys:
				ssh-keygen -t rsa
copiar claves al servidor:
				ssh-copy-id user@host
'''


import paramiko
from paramiko import SSHClient
from paramiko import RSAKey
import getpass

paramiko.util.log_to_file('paramiko.log') 
host = input("Introduce el host: ")
user = input("Introduce el usuario: ")
passwd = getpass.getpass("Introduce la contraseña de la clave privada: ")

paramiko.util.log_to_file('paramiko.log')
#Se debe cambiar esta línea e incluir la ruta donde se encuentra la clave id_rsa
private_key = '/home/adastra/.ssh/id_rsa'
rsa_key = RSAKey.from_private_key_file(private_key,password=passwd)

client = SSHClient()
#client.load_system_host_keys()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy()) 
client.connect(host, username=user, pkey=rsa_key,password=passwd)
stdin, stdout, stderr = client.exec_command('ls -a')
for line in stdout.readlines():
	print(line)
