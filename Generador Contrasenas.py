## Programa que genera contrasenas, este programa sirve para generar contrasenas seguras a los usuarios

import string #Nos va a importar todos los strings posibles en python. 
import random

longitud = int(input("Ingrese el tamano de la contrasena: "))

caracteres = string.ascii_letters + string.digits + string.punctuation ## Nos trae las letras del ABC (upper and lowercase), numeros y puntuaciones respectivamente, en forma de string.

contrasena = "".join(random.choice(caracteres) for i in range(longitud)) #A un string vacio, se le agrega caracteres random. Sabe cuantos caracteres se le agrega gracias al "for" basado en la longitud que el usuario le pida.

print("Su nueva contrasena es: " + contrasena )