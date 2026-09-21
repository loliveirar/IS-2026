import socket
from sys import argv
if len(argv) < 3:
    print("Uso: python3 udp_cliente1.py host port")
    exit(1)

host = argv[1]
port = int(argv[2])

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
linea=""
contador = 0
while linea!="FIN":
    contador += 1
    linea = input("Ingrese un mensaje (o 'FIN' para terminar): ")
    s.sendto((str(contador) + ":" + linea).encode(), (host, port))

    
    