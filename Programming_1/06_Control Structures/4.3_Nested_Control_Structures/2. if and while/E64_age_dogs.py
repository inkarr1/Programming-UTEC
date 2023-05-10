num = int(input("Numero de perritos: "))
i = 0

while i < num:
    nombre = input("Nombre del perro: ")
    edad = 0

    while edad < 1:
        edad = int(input("Edad canina: "))

    edadCann = 0

    if edad <= 2:
        edadCann = 10.5 * edad
    else:
        edadCann = (10.5) * 2 + 4 * (edad - 2)

    print("La edad de", nombre, "es", edadCann)
    i = i + 1