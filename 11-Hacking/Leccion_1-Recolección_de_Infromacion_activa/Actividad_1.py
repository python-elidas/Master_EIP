# __IMPORT__ #
import shodan
import nmap

# __Auxiliars__ #
'''
Definamos primero ciertos elementos auxilaires que ayudarán con la resolución de la actividad
'''
class NmapHost: # Creamos un objeto Host con informacion relevante
	def __init__(self):
		self.host = None # IP del servidor
		self.state = None # Estado del servidor
		self.reason = None # respuesta recibida desde el host
		self.openPorts = list() # lista de puertos abiertos en el host
		self.closedFilteredPorts = list() # lista de servidores cerrados en el host
	
	def selfPrint(self): # definimos una funcion print que ayudará a visualizar los resultados
		print(f'.Host: {self.host}')
		print(f'.State: {self.state}')
		print('.Ports:')
		for port in self.openPorts:
			print(f'|___.Number: {port.port}')
			print(f'|   |___Name: {port.name}')
			print(f'|   |___State: {port.state}')
			print(f'|   |___Version: {port.version}')
			print(f'|   |___Script: {port.scriptOutput}')
		
class NmapPort: # creamos un objeto Port con información relevante
	def __init__(self):
		self.id = None # iddel puerto dado por nmap
		self.state = None # estado del puerto
		self.reason = None # respuesta del puerto
		self.port = None # numero del puerto
		self.name = None # tipo de puerto
		self.version = None # version del puerto
		self.scriptOutput = None # script empleado para analizar el puerto
		
# __SHODAN__ #
'''
Definamos la utilidad que emplearemos para buscar las IP que coincidan con los criterios de busqueda en shodan.
'''
class shodanTool:
	def __init__(self, API):
		self.API = shodan.Shodan(API) # creamos el objeto Shodan con nuestra API
		self.infoAPI = self.keyInfo() # almacenamos la información de la Key
	
	def keyInfo(self):
		try:
			return self.API.info() # Devuelve la infromacion de la Key
		except shodan.APIError as e:
			print(f'Error: {e}')
			
	def shodanIP(self, query, n_result=10): # el script devolverá los primeros 10 resultados
		IPs = list() # creamo la lista en la que se almacenarán los resultados
		try:
			results = self.API.search(query) # realizamos la búsqueda
			for item in list(results['matches'])[:n_result]: # en los matches iteramos los n primeros
				IPs.append(item['ip_str']) #nos interesa la IP
		except shodan.APIError as e:
			print(f'Error: {e}') # en caso de error
		return IPs # Devuelve las ip halladas.
		
# __NMAP__ #
'''
· Definamos la funcionalidad que analizará las IP obtenidas mediente shodan.
· La funcion definida a continuacion se ha sacado de las lecciones del modulo 1
'''
class nmapTool:
	def __init__(self, ip, ports='', args=''):
		self.nm = nmap.PortScanner()
		self.ip = list(ip)
		self.ports = ports
		self.args = args
		
	def aux(self, scan): # Funcion de parseo
		self.nmapHosts = list()  # Donde se almacenaran los objetos de tipo Host
		for host in scan.all_hosts(): # analizaremos cada host en la lista
			nmapHost = NmapHost() # creamos un objeto host
			nmapHost.host = host  # Almacenamos el host en el objeto Host
			if 'status' in scan[host]: # si ha sido posible analizar la IP, almacenamos la informacion
				nmapHost.state = scan[host]['status']['state'] 
				nmapHost.reason = scan[host]['status']['reason']			
				for protocol in ['tcp', 'udp', 'icmp']:
					if protocol in scan[host]:
						ports = list(scan[host][protocol].keys())
						for port in ports:
							nmapPort = NmapPort()
							nmapPort.port = port
							check = scan[host][protocol][port]
							if 'script' in check:
								nmapPort.scriptOutput = check['script']
							if 'reason' in check:
								nmapPort.reason = check['reason']
							if 'name' in check:
								nmapPort.name = check['name']
							if 'version' in check:
								nmapPort.version = check['version']
							if 'open' in (check['state']):
								nmapHost.openPorts.append(nmapPort) # si el puerto está abierto
							else:
								nmapHost.closedFilteredPorts.append(nmapPort) # sie el puerto no esta abierto
						self.nmapHosts.append(nmapHost)
			else:
				print(f"[-] There is no match in the Nmap scan with the specified protocol {scan.all_hosts()}")
		return self.nmapHosts
	
	def parseNmapScan(self):
		results = list()
		for i in self.ip:
			if not self.ports == '' and not self.args == '': # si se especifican puertos y argumentos
				self.nm.scan(i, self.ports, arguments=self.args)
			elif not self.ports == '' and self.args == '': # si solo se especifican argumentos 
				self.nm.scan(i, self.ports)
			elif self.ports == '' and not self.args == '': # si solo se especifian puertos
				self.nm.scan(i, arguments=self.args)
			else: # si no se especifica ninguno
				self.nm.scan(i)
			results.append(self.aux(self.nm))
		return results
	
	def printNmap(self, results): # imprimamos los resultados:
		for hosts in results: 
			for host in hosts:
				host.selfPrint()
			print('\n')

# __MAIN RUN__ #
def run():
	key = str(input('Introduce la API Key para shodan:\n>>> '))
	shodan = shodanTool(key)
	query = str(input('Introduce los términos de búsqueda\n>>> '))
	IPs = shodan.shodanIP(query, n_result=5)
	if not len(IPs) == 0:
		print('Resultados hallados.\nEmpezando análisis...')
		nm = nmapTool(IPs, args='-A')
		res = nm.parseNmapScan()
		nm.printNmap(res)
	else:
		print('No se han podido hallar resultados.')
		
# __EJECUCUIÓN__ #
if __name__ == '__main__':
	run()
		
			