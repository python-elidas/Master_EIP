# __LIBRERIAS__#
import socket
import sys
import threading


#__MAIN CODE__#
class Server():
    def __init__(self, ip='0.0.0.0', port=8080, cli=5):
        serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #? Nota1
        try:
            #serversocket.bind((socket.gethostname(), 80))
            serversocket.bind((ip, port)) # reservamos un puerto
        except socket.error as msg:
            print('Bind failed. Error Code : %s Message %s ' %(str(msg[0]), str(msg[1])))
            sys.exit()
        try:
            serversocket.listen(cli) # establecemos el numero de clientes concurrentes
            while True:
                # wait to accept a connection - blocking call
                conn, addr = serversocket.accept() #? Nota 2
                print('Connection with %s : %s ' %(addr[0], str(addr[1])))
                # Levantamos un hilo port cliente
                hilo = threading.Thread(target=self.clientthread, args=(conn,))
                hilo.start()
        finally:
            serversocket.close()

    def clientthread(self, conn):
        conn.send('Welcome to the server. Type something! \n'.encode()) #send only takes string
        while True:
            data = conn.recv(1024)
            reply = 'OK...' + str(data)
            if not data:
                break
            conn.sendall(reply.encode())
        conn.close()

class Client():
    def __init__(self, ip='0.0.0.0', port=8080):
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((ip, port))
        client.send("Hello".encode())
        print(client.recv(1024))
        try:
            while True:
                message = input(">> ")
                client.send(message.encode())
                print("<< "+str(client.recv(1024)))
                if message == "close":
                    break
        finally:
            client.close()

#__MAIN RUN__#
if __name__ == "__main__":
    #server = Server()
    client= Client()


#__NOTAS__#
'''
    Nota 1:
        Con shocket.AF_INET le estamos diciendo al shocket que la conexión es del tipo tcp
        
    Nota2:
        La instrucción .accept() es una instrucción bloqueante, es decir, se queda en estado
        de espera hasta que se realiza una conexión.
        
    IMPORTANTE:
        Los puertos entre el 1 y el 1024 están reservados a permisos de root, del 1023 en
        adelante están disponibles. Esta restricción solo se aplica a los shocket de tipo
        server, los clientes se pueden conectar a cualquier puerto.
'''