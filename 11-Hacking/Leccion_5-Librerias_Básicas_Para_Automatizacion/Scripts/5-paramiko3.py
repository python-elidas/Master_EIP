'''
public key authentication:
keys:
				ssh-keygen -t rsa
copiar claves al servidor:
				ssh-copy-id user@host
'''


import paramiko
from paramiko import RSAKey
import getpass 

host = input("Introduce el host: ")
user = input("Introduce el usuario: ")
passwd = getpass.getpass("Introduce la contraseña de la clave privada: ")

client = paramiko.SSHClient()
try:
	paramiko.util.log_to_file('paramiko.log')
	#Se debe cambiar esta línea e incluir la ruta donde se encuentra la clave id_rsa
	rsa_key = paramiko.RSAKey.from_private_key_file('/home/adastra/.ssh/id_rsa',password='password')
	client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	client.connect(host,pkey=rsa_key,username=user,password=passwd)
	sftp = client.open_sftp()
	dirlist = sftp.listdir('.')
	print(dirlist)
	try:
		sftp.mkdir("demo")
	except IOError:
		print('IOError, the file already exists!')
	client.close()
except Exception as e:
	print('Exception %s' % str(e))
	try:
		client.close()
	except:
		pass
