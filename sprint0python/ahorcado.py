import random

def elegir_palabra(dificultad):
    palabras = {
        'facil': ['casa', 'agua', 'azul'],
        'normal': ['garaje', 'cabeza', 'guardia'],
        'dificil': ['curiosidad', 'paracaidas', 'coagulacion']
    }
    return random.choice(palabras[dificultad])

def jugar_ahorcado():
    dificultad = input("Elige la dificultad del juego (facil, normal, dificil): ")
    palabra = elegir_palabra(dificultad)
    palabra_guiones = "-" * len(palabra)
    intentos = 6
    letras_intentadas = []

    while intentos > 0 and "-" in palabra_guiones:
        print(f"\nPalabra: {palabra_guiones}")
        print(f"Intentos restantes: {intentos}")
        print(f"Letras intentadas: {letras_intentadas}")

        letra = input("\nAdivina una letra: ")

        if letra in letras_intentadas:
            print("Ya has intentado esa letra.")
        elif letra not in palabra:
            intentos -= 1
            print("Esa letra no está en la palabra.")
        else:
            for i in range(len(palabra)):
                if palabra[i] == letra:
                    palabra_guiones = palabra_guiones[:i] + letra + palabra_guiones[i+1:]
            print("¡Bien hecho!")

        letras_intentadas.append(letra)

    if "-" not in palabra_guiones:
        print(f"\n¡Felicidades! Has adivinado la palabra: {palabra}")
    else:
        print(f"\nLo siento, has perdido. La palabra era: {palabra}")

jugar_ahorcado()