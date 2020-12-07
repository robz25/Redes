#!usr/bin/python

import socket
import time 

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)      # para UDP

udp_host = 'localhost'
udp_port = 12345			        

msg = "hola mundo en minuscula"
msg = bytes(msg,'utf-8') 
print ("IP destino:", udp_host)
print ("Puerto:", udp_port)

sock.sendto(msg,(udp_host,udp_port))		# envio a server UDP
data,addr = sock.recvfrom(1024)	        #recepcion del servidor UDP
print("Mensaje del servidor: ",data," direccion: ",addr)

time.sleep(2) #esperamos dos segundos porque si para enviar mensaje de terminado
msg = ""
msg = bytes(msg,'utf-8') 
sock.sendto(msg,(udp_host,udp_port))		# Sending message to UDP server