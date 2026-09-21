import random
import socket
from sys import argv 

if len(argv) < 2:
    print("Uso: python3 udp_servidor1.py port")
    exit(1)

port = int(argv[1])

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(("", port))

while True:
    data, addr = s.recvfrom(1024)
    num = random.randint(0,1)
    if num == 1:
        #simulamos que el mensaje se ha recibido correctamente
        print("Mensaje recibido de {}: {}".format(addr, data.decode()))
        #confirmamos recepción enviando un datagrama de vuelta al cliente
        s.sendto("OK".encode(), addr)
