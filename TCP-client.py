import socket

HOST = '127.0.0.1'  # direccion de loopback o localhost
PORT = 3333        # Puerto empleado en el servidor
enviar = 'acbdeertykilo'

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    enviar = bytes(enviar, 'utf-8') #convertir string a byte
    s.send(enviar)
    data = s.recv(1024)

print('Received', repr(data))   #mostrar informacion recibida

