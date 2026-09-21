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

tiempo_maximo = 2.0
while linea!="FIN":
    contador += 1
    tiempo_espera = 0.1
    recibido = False
    linea = input("Ingrese un mensaje (o 'FIN' para terminar): ")
    s.sendto((str(contador) + ":" + linea).encode(), (host, port))
    #esperamos confirmación del servidor
    #si no llega en el tiempo establecido, duplicamos el tiempo de espera y reintentamos el envío
    while tiempo_espera <= tiempo_maximo and not recibido:
        s.settimeout(tiempo_espera)
        try:
            datagrama, origen = s.recvfrom(1024) # Tamaño máximo a recibir
            datagrama = datagrama.decode("utf8")
            if datagrama=="OK":
                print("Recibida confirmación")
                recibido = True
            else:
                print("Recibido datagrama no esperado")
        except socket.timeout:
            print("ERROR. El datagrama de confirmación no llega tras {} segundos. Reintentando...".format(tiempo_espera))
            tiempo_espera *= 2  # Duplicamos el tiempo de espera
        except:    # Otras posibles excepciones dejamos que las maneje el usuario
            raise
    