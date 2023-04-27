num = int(input("Número de perritos: "))
i = 0
while i <num:
    nombre = input("Nombre del perro: ")
    edad = 0

    while edad < 1:
        edad = int(input("Edad canina: "))

    edadCanina = 0
    if edad <= 2:
        edadCanina = 10.5 * edad
    else:
        edadCanina = (10.5) * 2 + 4 * (edad - 2)

    print("La edad de", nombre, "es", edadCanina)
    i += 1