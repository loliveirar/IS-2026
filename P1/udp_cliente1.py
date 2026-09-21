import socket
from sys import argv
if len(argv) < 3:
    print("Uso: python3 udp_cliente1.py host port")
    exit(1)

host = argv[1]
port = int(argv[2])

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(("", 8080))
while linea!="FIN":
    linea = input("Ingrese un mensaje (o 'FIN' para terminar): ")
    s.sendto(linea.encode(), (host, port))
    