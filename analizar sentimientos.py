from textblob import TextBlob

def analyze_sentiment(text): #se crea una funcion con el parametro de texto

    blob = TextBlob(text) #se crea el objeto con el texto que se va a recibir

    polarity = blob.sentiment.polarity #Funcion especial de la biblioteca. devuelve un valor que va desde -1 a 1, siendo estos muy negavito o muy positivo

    if polarity > 0: 
        sentiment = 'Positivo'
    elif polarity < 0:
        sentiment = 'Negativo'
    else:
        sentiment = 'Neutro'

    print(f'text {text}')
    print(f'Polaridad {polarity}')
    print(f'Sentimiento {sentiment}')

text_example = input("Write something: ") #el usuario entra el texto
analyze_sentiment(text_example) #se llama la funcion, utilizando el "text example"