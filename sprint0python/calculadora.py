from operaciones import suma, resta, multiplicacion, division #llamo a los métodos

def solicitar_numeros(): #creo otra función
    num1 = int(input("1º número: "))
    num2 = int(input("2º número: "))
    return num1, num2

def realizar_operacion(operacion, num1, num2): #utilizo los métodos dentro de una nueva función que llamaré más tarde
    if operacion == "suma":
        return suma(num1, num2)
    elif operacion == "resta":
        return resta(num1, num2)
    elif operacion == "multiplicacion":
        return multiplicacion(num1, num2)
    elif operacion == "division":
        if num2 == 0:
            return "Error: División por cero"
        else:
            return division(num1, num2)
    else:
        return "Operación no reconocida"

respuesta = 's'
while respuesta.lower() == 's':
    num1, num2 = solicitar_numeros()
    operacion = input("¿Qué operación desea realizar (suma/resta/multiplicacion/division)? ")
    resultado = realizar_operacion(operacion.lower(), num1, num2)
    print("El resultado es: " + str(resultado))
    respuesta = input("¿Desea realizar otra operación (s/n)? ")
