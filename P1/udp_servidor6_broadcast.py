import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
s.bind(("", 12345))  # Escuchar en todas las interfaces

while True:
    datagrama, origen = s.recvfrom(1024)
    datagrama = datagrama.decode("utf8")
    if datagrama == "BUSCANDO HOLA":
        print("Recibido datagrama de {}: {}".format(origen, datagrama))
        s.sendto(("HOLA").encode(), origen)
        print("Enviado datagrama a {}: {}".format(origen, "HOLA"))
        datagrama, origen = s.recvfrom(1024)
        datagrama = datagrama.decode("utf8")
        print("Respuesta recibida de {}: {}".format(origen, datagrama))
        if datagrama == "HOLA":
            s.sendto(("OK").encode(), origen)
            print("Enviado datagrama a {}: {}".format(origen, "OK"))