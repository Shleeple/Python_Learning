seguir = input("¿Quiere empezar? ¿Si o No? ")
while seguir == "Si":
    print("""\nTiene las siguientes opciones:  

    1) Factorial
    2) Calificaciones
    3) Promedio""")

    choice = int(input("\nElija una opcion del 1 al 3: "))

    if choice == 1:
        print("\nBienvenido/a al problema factorial")
        num = int(input("\nElija un numero, y sacaremos el factorial: "))
        fact = 1
        newFact = 0
        for i in range(0,num):
            newFact += 1
            fact *= newFact
        print("\nEl factorial de", num,"es", fact)

    elif choice == 2:
        print("\n Bienvenido/a al problema de calificaciones")
        cal=int(input("\nPonga una calificacion: "))
        n=0
        caln=0
        print()
        while caln >= 0:
            cal += caln
            n += 1
            caln = int(input("Ponga una calificacion: "))
        promedio = cal/n
        print("\nEl promedio de las calificaciones es:",round(promedio,2))

    elif choice == 3:
        print("\nBienvenido/a al problema de promedio")
        calSum = 0
        numCal = int(input("\n¿Cuantas calificaciones va a poner? "))
        print()
        for i in range(0,numCal):
            cal = int(input("Dame una calificación: "))
            calSum += cal
        promedio = calSum/numCal
        print("\nPromedio de califiaciones:", round(promedio,2))
    seguir = input("\n¿Quiere seguir? ¿Si o No? ")
