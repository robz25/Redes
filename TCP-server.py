import socket

HOST = '127.0.0.1'  # direccion de loopback o localhost
PORT = 3333        # puerto de escucha, puertos sin privilegios arriba de 1023

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
            data = data.upper() #convertimos letras a muysculas
            conn.send(data)