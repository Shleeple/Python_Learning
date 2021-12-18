print("""Tiene las siguientes opciones:

1) Representar un menú con 4 opciones:
2) Solicitar edad y genero de una persona
3) Almacen
4) Salario de un obrero
5) 2 numeros
6) Area de un cuadrado
7) Sistema de ecuaciones\n""")
choice = int(input("Elija una opcion del 1 al 7: "))
if choice == 1:
    print("""\n\nQue quiere hacer?

1) Calcular el doble de un entero,
2) Calcular la mitad de un entero,
3) Calcular el cuadrado de un entero
4) Salir\n""")
    op = int(input("Elija una opcion del 1 al 4: "))
    if op == 1:
        doble = int(input("\nElija un numero: "))
        print("El doble de",doble,"es",(doble*2))
    elif op == 2:
        mitad = int(input("\nElija un numero: "))
        print("La mitad de",mitad,"es",(mitad/2))
    elif op == 3:
        cuad = int(input("\nElija un numero: "))
        print("El cuadrado de",cuad,"es",(cuad**2))
    elif op == 4:
        print("Hasta luego! Vuelva pronto")
    else:
        print("Ese no es un numero aceptable\n")

if choice == 2:
    gen = input("\n\nEs H o M? ")
    edad = int(input("Cual es su edad? "))
    if gen == "H":
        if edad >= 18:
            print("\nCumple las condiciones para realizar servicio militar.")
        else:
            print("\nSe revisa la informacion")
    elif gen == "M":
        print("\nSe revisa la informacion")
    else:
        print("\nEse no es un genero valido")

if choice == 3:
    print("\n\nSi compra mas de $1000, se le da un descuento del 20%")
    total = int(input("¿En cuanto sale su compra? $ "))
    if total >= 1000:
        print("Su total es de $", total*.80)
    elif total <= 0:
        print("Su compra no es valida")
    else:
        print("Su total es de $", total)

if choice == 4:
    hrs = int(input("\n\n¿Cuantas horas a la semana trabaja el obrero?"))
    if hrs > 40:
        sal = (40*100)+((hrs-40)*40)
    elif hrs <= 0:
        print("Las horas no son validas")
    else:
        sal = hrs*100

    print("El salario del obrero es de $", sal)

if choice == 5:
    num1 = int(input("\n\nElija num1: "))
    num2 = int(input("Elija num2: "))
    if num1 == num2:
        res = num1*num2
    elif num1 > num2:
        res = num1-num2
    else:
        res = num1+num2
    print("El resultado es:",res)

if choice == 6:
    print("""\n\nTiene las siguientes opciones:
\n1) Area de un cuadrado
2) Area de un circulo
3) Area de un triangulo equilatero""")
    fig = int(input("\nElija una opcion del 1 al 3: "))
    if fig == 1:
        lado = int(input("\nLongitud del lado: "))
        area = lado*lado
    elif fig == 2:
        radio = int(input("\nReadio del circulo: "))
        area = 3.14*radio**2
    elif fig == 3:
        lado = int(input("\nLongitud del lado: "))
        altura = int(input("Altura del triangulo: "))
        area = lado*altura/2
    print("\nEl area es",area,"m^2")

if choice == 7:
    print("""\n\nEn un sistema de ecuaciones

ax+by=c
dx+ey=f
""")
    a = int(input("Elija el valor de a: "))
    b = int(input("Elija el valor de b: "))
    c = int(input("Elija el valor de c: "))
    d = int(input("Elija el valor de d: "))
    e = int(input("Elija el valor de e: "))
    f = int(input("Elija el valor de f: "))

    if (a*e-b*d) == 0:
        print("El sistema no se puede resolver")
    else:
        x = (c*e-b*f)/(a*e-b*d)
        y = (a*f-c*d)/(a*e-b*d)
        print("\nx =",x,"\ny =",y)
















    
