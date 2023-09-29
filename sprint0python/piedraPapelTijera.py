import random

opciones = ['piedra', 'papel', 'tijera']
contador_jugadas = 0
victorias_jugador = 0
victorias_aleatorio = 0

while contador_jugadas < 5:
    jugador = input("Elige una jugada (piedra, papel, tijera): ")
    if jugador not in opciones:
        print("Jugada no válida. Inténtalo de nuevo.")
        continue
    aleatorio = random.choice(opciones)
    print("El programa ha elegido: " + aleatorio)
    if jugador == aleatorio:
        print("Habéis empatado.")
        continue
    elif (jugador == 'piedra' and  aleatorio == 'tijera') or \
        (jugador == 'papel' and aleatorio == 'piedra') or \
        (jugador == 'tijera' and aleatorio == 'papel'):
        victorias_jugador += 1
        print("Has ganado, " + jugador + " gana a " + aleatorio)
    else:
        victorias_aleatorio += 1
        print("Has perdido, " + aleatorio + " gana a " + jugador)
    contador_jugadas += 1
if victorias_jugador > victorias_aleatorio:
    print("Has ganado el juego!")
elif victorias_jugador < victorias_aleatorio:
    print("Has perdido el juego.")
else:
    print("El juego ha terminado en empate.")