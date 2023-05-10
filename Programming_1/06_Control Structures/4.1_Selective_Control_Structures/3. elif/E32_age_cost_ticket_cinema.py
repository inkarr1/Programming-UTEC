age = int(input("Ingrese la edad: "))

if 0 <= age <= 17:
    print("El costo de la entrada es s/.15")
elif 18 <= age <= 30:
    print("El costo de la entrada es s/.25")
elif 31 <= age <= 45:
    print("El costo de la entrada es s/.30")
else:
    print("El costo de la entrada es s/.10")