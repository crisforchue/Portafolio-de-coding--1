# Crear un bot para hacer chistes para un workspace utilizando API
# Arreglos hechos que no forman parte del video: Agregar temporizador entre solicitud, ahora da chistes diferentes.

import slack
import pyjokes #Importamos las librerias
import time

TOKEN = 'xoxb-7762157942919-7778040328850-jrocPJ7HuzZo40uYjsw8zxdE' #Aplicamos el token del API para poder utilizar el bot

client = slack.WebClient(TOKEN) #Creamos la instancia del cliente donde utilizamos el token, que es nuestro bot y es para darle acceso a la API.

#client.chat_postMessage(channel = 'chistes', text = 'Bienvenidos!') #Prueba de texto, en el canal "chistes" nos da el mesnaje de "Bienvenidos!"

while True: #creamos un blucle infinito 

    jokes = pyjokes.get_joke(language='es', category='all') #Nos busca los chistes que queremos 

    history = client.conversations_history(channel='C07NW1HA0BC') #Esta instancia nos dice, que el historial es la conversation que tiene el cliente (bot), en el canal de chistes (con el codigo hecho)
 
    if 'chiste' in history['messages'][0]['text'].lower(): #Si la palabra "chiste" se encuentra en el historial de mensajes,nos mandara un chiste. 
        client.chat_postMessage(channel='chistes', text = jokes) #El cliente (bot) nos da un mensaje. En el canal de chistes, nos da un chiste 

    time.sleep(5)