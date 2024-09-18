import requests
from bs4 import BeautifulSoup

url = 'https://www.datachar.com'

response = requests.get(url) #Se hace una solicitud de request a la url, el codigo "200" es para dejarnos saber que la solicitud fue acceptada.

if response.status_code == 200: #Si el codigo es igual a 200 la solicitud fue acceptada y podemos comenza el codigo

    soup = BeautifulSoup(response.text, 'html.parser') #Esto nos permite analizar el contenido HTML de la paginas, asi buscamos la palabra que queremos encontrar. 
    word = input("Que palabra deseas buscar?: ") #Se le pide al usuario dar una palabra de solivitud 

    if word in soup.get_text().lower(): #Busca la palabra, y si la encuentra, la pasa de vuelva junto a la url. 
        print(f'Se encuentra la palabra {word} en la url {url}')

else:
    print("No se puede acceder a la pagina.")