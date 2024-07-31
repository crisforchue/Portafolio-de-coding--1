## IDENTIFICADOR DE PUERTOS. Este codigo sirve para buscar puertos abiertos o cerrados. 

import socket #Los sockets son combinarion de una dirrecion IP y numero de puerto. Identifica una aplicacion especifica en una computadora

ip = input("Ingrese la dirreccion IP que vamos a escanear ")

for puerto in range(1, 65535): #Numeros conocidos de puertos disponibles.
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #"Socket.AF_INET" se utilizan para las IPv4 (con la que estamos trabajando) y "SOCK_STREAM" se utiliza para TCP (transmision control protocol)
    sock.settimeout(5) 

    result = sock.connect_ex((ip, puerto)) #Aqui es donde se hacen las conexiones

    if result == 0: 
        print("Puerto abierto: " + str(puerto))
        sock.close()
        break
    else:
        print("Puerto cerrado: " + str(puerto))