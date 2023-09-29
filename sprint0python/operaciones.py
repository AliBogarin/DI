def suma (num1, num2):
    print("La suma es: "+int(num1+num2))
    return num1+num2

def resta(num1, num2):
    if num1<num2:
        return print(" La resta es: ", num1-num2)
    else:
        return num2-num1

def multiplicacion(num1, num2):
    return print("La multiplicación es: ", num1*num2)

def division(num1,num2):
    if num1==0 | num2==0:
        return print("Operación inadecuada!")
    elif num1<num2:
        return print("La división es: ", num1-num2)
    else:
        return print("La división es: ", num1-num2)
    
respuesta= input("Qué operación desea realizar (suma 's'/resta 'r'/ multiplicación 'm'/ división 'd'): ")

if respuesta=="s":
    num1= input(" 1º número: ")
    num2= input(" 2º número: ")
    suma(num1,num2)
