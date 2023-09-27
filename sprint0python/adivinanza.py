nota =10
def adivinanza1():

    print("¿Qué es algo que puedes atrapar, pero no lanzar?")
    print("a) Un resfriado")
    print("b) Un balón")
    print("c) Un libro")

    respuesta = input("Por favor, responde con a, b o c para indicar tu elección: ")

    if respuesta.lower() == 'a':
        print("¡Correcto! La respuesta es un resfriado.")
        nota+=10
    else:
        print("Lo siento, esa no es la respuesta correcta. La respuesta correcta es 'a', un resfriado.")

adivinanza1()

def adivinanza2():
    print ("Si le doy a todo el  mundo y me quedo con ella, que es?")
    print("a) La mano")
    print("b) Dinero")
    print("c) Una vaca")

respuesta = input("Cuál es la respuesta correcta la a, b, c, dime, cuál eliges?: ")

if respuesta.lower()== 'a':
    print("Perfecto!, respuesta correcta")
    nota+=10
else:
    print ("Incorrecto!, la respuesta correcta es la a.")
adivinanza2()

def adivinanza3():
    print("Cae de un tajo y no se mata, cae al rio y se desbarata")
    print("a) Un borracho")
    print("b) Un papel")
    print("c) La hoja de un árbol")

respuesta= input("Cuál es la correcta, la a, b, c?")

if respuesta.lower()=='b':
    print("Correcto!")
    nota+=10
else:
    print("La respuesta correcta es la b")
adivinanza3()


