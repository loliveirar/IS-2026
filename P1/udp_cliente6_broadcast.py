import socket
from sys import argv

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

broadcast_address = "172.20.255.255"
port = 12345


message = "BUSCANDO HOLA"
s.sendto(message.encode(), (broadcast_address, port))
print("Mensaje enviado: {}".format(message))
while True:
    data, addr = s.recvfrom(1024)
    print("Mensaje recibido de {}: {}".format(addr, data.decode()))
    if data.decode() == "HOLA":
        print("Respuesta recibida de {}: {}".format(addr, data.decode()))
        s.sendto(("HOLA").encode(), addr)
        print("Enviando HOLA a "+ str(addr))
        data, addr = s.recvfrom(1024)
        print("Respuesta final recibida de {}: {}".format(addr, data.decode()))