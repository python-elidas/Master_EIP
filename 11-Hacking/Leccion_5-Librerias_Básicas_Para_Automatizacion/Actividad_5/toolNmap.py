# __BIBLIOTECAS__ #
import nmap, socket


# __ELEMENTOS AUXILIARES__ #
class NmapHost:  # Creamos un objeto Host con informacion relevante
    def __init__(self):
        self.host = None
        self.state = None
        self.reason = None
        self.openPorts = list()
        self.closedFilteredPorts = list()

    def selfPrint(self):
        print(f'.Host: {self.host}')
        print(f'.State: {self.state}')
        print('.Ports:')
        for port in self.openPorts:
            print(f'|___.Number: {port.port}')
            print(f'|   |___Name: {port.name}')
            print(f'|   |___State: {port.state}')
            print(f'|   |___Version: {port.version}')
            print(f'|   |___Script: {port.scriptOutput}')


class NmapPort:  # creamos un objeto Port con información relevante
    def __init__(self):
        self.id = None  # ID del puerto
        self.state = None
        self.reason = None
        self.port = None
        self.name = None
        self.version = None
        self.scriptOutput = None


# __SCRIPT PRINCIPAL__ #
class nmapTool:
    def __init__(self):
        self.nm = nmap.PortScanner()

    def parseNmapScan(self, scan):
        self.nmapHosts = list()  # Donde se almacenaran los objetos de tipo Host
        for host in scan.all_hosts():
            nmapHost = NmapHost()
            nmapHost.host = host  # Almacenamos el host en el objeto Host
            if 'status' in scan[host]:
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
                                nmapHost.openPorts.append(nmapPort)
                            else:
                                nmapHost.closedFilteredPorts.append(nmapPort)
                        self.nmapHosts.append(nmapHost)
            else:
                print(
                    f"[-] There is no match in the Nmap scan with the specified protocol {scan.all_hosts()}")
        return self.nmapHosts

    def getPorts(self, ip, to_txt=False):
        self.nm.scan(ip)
        ports = list()
        for host in self.nm.all_hosts():
            # print(host)
            for protocol in ['tcp', 'udp', 'icmp']:
                try:
                    ports.extend(list(self.nm[host][protocol].keys()))
                except KeyError:
                    continue
        
        if to_txt:
            with open('ports.txt', 'w') as fw:
                for host in list(ports.keys()):
                    for protocol in list(ports[host].keys()):
                        for port in ports[host][protocol]:
                            fw.write(f'{port}\n')
                fw.close()
        else:
            return ports        
    
    def nmapScan(self, ip, ports='', args='', parse=True):
        if not ports == '' and not args == '':
            self.nm.scan(ip, ports, arguments=args)
        elif not ports == '' and args == '':
            self.nm.scan(ip, ports)
        elif ports == '' and not args == '':
            self.nm.scan(ip, arguments=args)
        else:
            self.nm.scan(ip)
        if parse:
            return self.parseNmapScan(self.nm)

    def printNmap(self, results):
        for hosts in results:
            for host in hosts:
                host.selfPrint()
            print('\n')
            
    def getBanners(self, ip, ports=list(), t=10, to_screen=True, to_txt=False, to_var=False):
        banners = list()
        if len(ports) == 0:
            ports = self.getPorts(ip)
        for port in ports:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            try:
                if to_screen:
                    print(f'[-] Connecting to {ip} in port {port}')
                sock.connect((str(ip), int(port)))
                sock.settimeout(t)
                banner = sock.recv(1024)
                banners.append((port, banner.decode().strip()))
            except Exception as e:
                if to_screen:
                    print(e)
                continue
        if to_screen:
            try:
                from toolPrint import listPrint
                listPrint(banners)
            except ModuleNotFoundError:
                print(banners)
        if to_txt:
            with open(f'{ip}_banners.txt', 'w') as fw:
                for banner in banners:
                    fw.write(f'{banner}\n')
                fw.close()
        if to_var:
            return banners


#__TEST__ #
if __name__ == '__main__':
    import sys, argparse
    
    nmap = nmapTool()
    # nmap.printNmap(nmap.NmapScan())
    nmap.getBanners(sys.argv[1], to_var=False)
