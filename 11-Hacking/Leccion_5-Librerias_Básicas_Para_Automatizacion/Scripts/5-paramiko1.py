import paramiko
from paramiko import SSHClient
import getpass
paramiko.util.log_to_file('paramiko.log') 
host = input("Introduce el host: ")
user = input("Introduce el usuario: ")
passwd = getpass.getpass("Introduce la contraseña: ")
client = SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy()) 
client.connect(host,username=user,password=passwd)
stdin, stdout, stderr = client.exec_command('ls -a')
for line in stdout.readlines():
	print(line)
client.close()
