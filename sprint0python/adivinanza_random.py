import random
#Defino las adivinanzas como funciones y luego creo una lista con ellos para iterarlos en Random
def adivinanza1():
    nota = 0
    print("¿Qué es algo que puedes atrapar, pero no lanzar?")
    print("a) Un resfriado")
    print("b) Un balón")
    print("c) Un libro")
    respuesta = input("Por favor, responde con a, b o c para indicar tu elección: ")
    if respuesta.lower() == 'a':
        print("¡Correcto! La respuesta es un resfriado.")
        nota =nota+ 10
    else:
        print("Lo siento, esa no es la respuesta correcta. La respuesta correcta es 'a', un resfriado.")
        nota =nota- 5
    return nota

def adivinanza2():
    nota = 0
    print("\n")
    print ("Soy pequeña y de cristal, méteme al hoyo y no pederás, qué soy?")
    print("a) Una ventana")
    print("b) Una canica")
    print("c)Una pelota de golf.")
    respuesta= input("Cuál es tu respuesta: a, b, o la c?: ")
    if respuesta.lower()=="b":
        print("Correcto!, muy bien hecho!")
        nota =nota + 10
    else:
        print("NO!, la respuesta correcta es la b")
        nota = nota - 5
    return nota

def adivinanza3():
    nota = 0
    print("\n")
    print("Se la doy a todo el mundo, pero me quedo con ella....qué soy?")
    print("a) El abrigo")
    print("b) Un libro")
    print("c) La mano")
    respuesta=input("Cuál es tu respuesta, a,b ó la c?: ")
    if respuesta.lower()=="c":
        print("Respuesta correcta!")
        nota = nota + 10
    else:
        print("Respuesta incorecta!, es la c")
        nota =  nota- 5
    return nota

adivinanzas = [adivinanza1, adivinanza2, adivinanza3]
aleatorio = random.sample(adivinanzas, 3)# Creo una variable donde guardar mi resultado ramdom

total_puntos = 0
for i in aleatorio:
    total_puntos = total_puntos + i() #Cuento los puntos de las adivinanzas

print("\n")
print("Un vez finalizado el juego, has sacado el punto máximo?")
if total_puntos == 30:
    print("Bien jugado, tienes 30 puntos!.")
else:
    print("Puedes intentar otra vez, tienes " +str( total_puntos) +  "puntos.")

    """" Random.sample(): devuelve una lista de elementos seleccionados aleatoriamente (secuencia, k) k, siedo esta la longitud
    """