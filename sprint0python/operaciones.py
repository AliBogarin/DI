def suma (num1, num2):
    return num1+num2

def resta(num1, num2):
    if num1<num2:
        return  num1-num2
    else:
        return num2-num1

def multiplicacion(num1, num2):
    return  num1*num2

def division(num1,num2):
    if num1==0 | num2==0:
        return print("Operación inadecuada!")
    elif num1<num2:
        return print("La división es: ", num1-num2)
    else:
        return print("La división es: ", num1-num2)
    
