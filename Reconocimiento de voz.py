## RECONOCIMIENTO DE VOZ 

import speech_recognition as sr #Importamos la libreria. El sr "speech recongition" 

recognizer = sr.Recognizer() #Creamos una variable, "recognizer", para que pueda reconocer lo que hablamos 
mic = sr.Microphone() #Creamos una segunda variable para el microfono, para abrir nuestro microfono

with mic as source:
    audio = recognizer.listen(source) #El audio va a ser reconocido por el microfono, "source" es de donde proviene el audio, en este caso, es el microfono

text = recognizer.recognize_google(audio, language = 'ES') #El lenguahe que reconoce sera espanol

print(f"Dijiste: {text}")