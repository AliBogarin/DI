
def adivinanza1():

    print("¿Qué es algo que puedes atrapar, pero no lanzar?")
    print("a) Un resfriado")
    print("b) Un balón")
    print("c) Un libro")

    respuesta = input("Por favor, responde con a, b o c para indicar tu elección: ")

    if respuesta.lower() == 'a':
        print("¡Correcto! La respuesta es un resfriado.")
    else:
        print("Lo siento, esa no es la respuesta correcta. La respuesta correcta es 'a', un resfriado.")

adivinanza1()



