# __IMPORT__ #
import socket
import sys


ports = open('ports.txt', 'r')
vulnbanners = open('vulnbanners.txt', 'r')
for port in ports:
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	try:
		sock.connect(( str(sys.argv[1]), int(port) ))
		print('Connecting to '+str(sys.argv[1])+' in the port: '+str(port))
		sock.settimeout(1)
		banner = sock.recv(1024)
		for vulnbanner in vulnbanners:
			if banner.decode().strip() in vulnbanner.strip():
				print('Banner Found! '+banner)
				print('Host: '+str(sys.argv[1]))
				print('Port: '+str(port))		
	except Exception as e:
		print(e)
		continue
	finally:
		if sock is not None:
			sock.close()
