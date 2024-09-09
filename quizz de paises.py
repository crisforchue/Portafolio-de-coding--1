paises_capitales = {
    'Argentina': 'Buenos Aires',
    'Brasil': 'Brasilia',
    'Chile': 'Santiago',
    'Colombia': 'Bogota',
    'México': 'Ciudad de Mexico',
    'Perú': 'Lima',
    'Estados Unidos': 'Washington D.C.',
    'Francia': 'Paris',
    'España': 'Madrid',
    'Italia': 'Roma',
    'Alemania': 'Berlin',
    'Reino Unido': 'Londres',
    'Japón': 'Tokio',
    'China': 'Pekín',
    'India': 'Nueva Delhi',
    'Canadá': 'Ottawa',
    'Australia': 'Canberra',
    'Rusia': 'Moscu',
    'Sudáfrica': 'Pretoria',
    'Egipto': 'El Cairo'
}

def quizCapitales():

    print("Bienvenido a este quizz de capitales!")
    score = 0 #comenzamos con la puntuacion en 0

    for country, capital in paises_capitales.items(): #Aca nos dice que, por cada pais y capital dentro del diccionario de los paises.

        print(f'Pregunta: Cual es la capital de {country}')
        respuesta = input("Respuesta: ")
        if respuesta.lower() == capital.lower():
            print("Correcto! Ganaste 10 puntos.")
            score += 10
        else: 
            print(f"Respuesta incorrecta. La capital es {capital}")
    print(f'Tu puntuacion final es igual a: {score}/{len(paises_capitales)}') 


quizCapitales()