from translate import Translator #importamos la libreria 

translator = Translator(from_lang='spanish', to_lang='english') #Llamamos a la case de esa libreria y agregamos lo parametros. Respectivamente, traduce de espanol a ingles

txt = input("Que quieres traducir?: ")
respuesta = translator.translate(txt) #Llamamos a nuestro metodo

print(respuesta) #Imprime la respuesta