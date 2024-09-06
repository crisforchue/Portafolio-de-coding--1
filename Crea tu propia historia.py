import random

vida = 100
puntuacion = 0
armadura = 50

def mostrarEstado():
 print(f'\n Vida: {vida}\n Puntuacion: {puntuacion} \n Armadura: {armadura}')

print("Iniciando juego...")

def reiniciarJuego():
    global vida, puntuacion, armadura
    vida = 100
    puntuacion = 0
    armadura = 50

def explorarHabitacion():

    global vida

    enemigo_presente = random.choice([True, False])

    if enemigo_presente:
        print("enemigo encontrado!")
        hablarMaestro()
    else: 
        print('La habitacion esta vacia, sigue explorando.')

def hablarMaestro():

    global vida, puntuacion

    print("Te encontraste con un maestro. te pregunta sobre las tablas de multiplicar.")

    respuesta_correcta = False

    while not respuesta_correcta and vida > 0:

        multiplicador = random.randint(1,10)
        multiplicando = random.randint(1,10)
        resultado_esperado = multiplicador * multiplicando

        respuesta = input(f"Cuanto es {multiplicador} x {multiplicando}?: ")

        if respuesta.isdigit() and int(respuesta) == resultado_esperado:
            print("Respuesta correcta! El profesor te da 20 puntos.")
            puntuacion += 20
            respuesta_correcta = True
        else:
            print("Respuesta incorrecta, el profesor te ataca con su regla y pierdes 10 de vida.")
            vida -= 10

def eventoAleatorio():

    global vida, puntuacion, armadura
    
    evento = random.choice(['Encontraste un cofre con tesoros', 'te caiste y pierde 10 de vida', 'Descubriste un atajo secreto'])

    if evento == 'Encontraste un cofre con tesoros':
        print("Encontraste un cofre con tesoros! Ganas 15 puntos.")
        puntuacion += 15
    elif evento == 'te caiste y pierde 10 de vida':
        print("Te caiste, pero tu armadura te salva. Pierdes 10 de vida, y 15 de armadura")
        armadura -= 15
        vida -= 10
    elif evento == 'Descubriste un atajo secreto':
        print("Encontraste un atajo secreto, y llegaste a donde el jefe final.")
        jefeFinal()

def jefeFinal():

    print("El jefe te desafia a un ultimo juego.")

    opciones = ['piedras', 'papel', 'tijeras']

    while True:

        eleccion_jugador = input("Elige tu arma. (Piedra/papel/tijera): ").lower()
        eleccion_jefe = random.choice(opciones)

        print(f"El jefe eligio {eleccion_jefe}")

        if eleccion_jefe == eleccion_jugador: 
            print("Es un empate, intenta de nuevo")

        elif (eleccion_jugador == 'piedra' and eleccion_jefe == 'tijera') or (eleccion_jugador == 'papel' and eleccion_jefe == 'piedra') or (eleccion_jugador == 'tijeras' and eleccion_jefe == 'papel'):
            print("Derrotaste al jefe, ganas 100 puntos!")
            puntuacion += 100
            print("Pasaste el juego!")
            break
        else:
            print("El jefe te derroto, perdiste :(. ")
            print("reiniciando juego...")
            reiniciarJuego()
            break

def jugar_juego():

    while vida > 0:
        print('\n Te encuentras en un pasillo del castillo!')
        mostrarEstado()
        opcion = input("Que deseas hacer? \n 1. Entrar en una habitacion\n2. Seguir explorando\n3.Consultar tu estado.\n4.Salir del juego")

        if opcion == '1':
            explorarHabitacion()
        elif opcion == '2':
            eventoAleatorio()
        elif opcion == '3': 
            mostrarEstado()
        else:
            print('opcion no valida, favor elegir entre las opciones.')
        
        if vida <= 0:
            print("\nPerdiste el juego! tu personaje no tiene vida.")
            mostrarEstado()
        elif puntuacion >= 100:
            print('\nGanaste el juego! Felicidades.')
            mostrarEstado()
            break
        elif armadura <= 0:
            print('\nTu armadura esta rota, perdiste')
            break

jugar_juego()