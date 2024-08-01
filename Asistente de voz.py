## "Copycat Alexa" en python. se le dice a la maquina que queremos hacer, y lo hara. (como alexa)
## falta explicacion

import speech_recognition as sr
import webbrowser
import pyttsx3

recognizer = sr.Recognizer()
engine = pyttsx3.init()

print("iniciando programa")

def talk():
    
    mic = sr.Microphone()
    with mic as source:
        audio = recognizer.listen(source)

    text = recognizer.recognize_google(audio, language='es-ES') 
    print(f"Dijiste: {text}")   
    return text.lower()

if "amazon" in talk():
    engine.say("Que quieres comprar en Amazon?")
    engine.runAndWait()
    text = talk()
    webbrowser.open(f"https://www.amazon.es/s?k={text}")