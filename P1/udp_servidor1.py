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
    print("Mensaje recibido de {}: {}".format(addr, data.decode()))
