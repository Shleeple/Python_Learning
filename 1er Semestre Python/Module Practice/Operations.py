def suma(a,b):
    try:
        c = a+b
    except TypeError:
        print("Error, tipo de dato no valido: ")
    return c

def resta(a,b):
    try:
        c = a-b
    except TypeError:
        print("Error, tipo de dato no valido: ")
    return c

def producto(a,b):
    try:
        c = a*b
    except TypeError:
        print("Error, tipo de dato no valido: ")
    return c

def division(a,b):
    try:
        c = round(a/b,2)
    except TypeError:
        print("Error, tipo de dato no valido: ")
    except ZeroDivisionError:
        print("Error, no se puede dividir entre 0")
    return c

def divEntera(a,b):
    try:
        c = a//b
    except TypeError:
        print("Error, tipo de dato no valido: ")
    except ZeroDivisionError:
        print("Error, no se puede dividir entre 0")
    return c

def mod(a,b):
    try:
        c = a%b
    except TypeError:
        print("Error, tipo de dato no valido: ")
    except ZeroDivisionError:
        print("Error, no se puede dividir entre 0")
    return c
