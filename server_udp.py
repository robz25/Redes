#!usr/bin/python

import socket

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)      # UDP

HOST = 'localhost'		        #IP del host
PORT = 12345			                #puerto

sock.bind((HOST,PORT))

data = "1"

while data:
    print("Eserando cliente...")
    data,addr = sock.recvfrom(1024)	        #receive data from client
    if(not data):
        break           #salir del loop
    else:
        print("Mensaje recibido: ",data)
        data = data.upper() #convertimos letras a muysculas
        sock.sendto(data,addr)      #send message to UDP server 

sock.close()    #terminar conexion
    