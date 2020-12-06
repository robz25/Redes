import socket

HOST = '127.0.0.1'  # direccion de loopback o localhost
PORT = 65432        # puerto de escucha, puertos sin privilegios arriba de 1023

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            if not data:
                break
#            data = str(data)
            data = data.upper()
#            data = bytes(data, 'utf-8')
            conn.send(data)