
from gtts import gTTS #Libreria que permite convertir el texto al habla.

file = open('libro.txt', 'r', encoding="utf-8") #"R" lo usa como el modo de lectura, mientras que "enconding" utiliza una codificacion especial para que el texto reconozca cierto caracteres.
textBook = file.read()
file.close() 

audio = gTTS(text=textBook, lang='es')
audio.save('Audiolibro.mp3') #crea el audi mp3 junto al archivo de text.