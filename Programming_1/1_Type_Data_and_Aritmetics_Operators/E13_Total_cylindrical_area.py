radio = float(input("Ingrese el radio: "))
height = float(input("Ingrese la altura: "))
pi = 3.14

area_base = 2 * pi * (radio ** 2)
area_lateral = 2 * pi * radio * height

area_total = area_base + area_lateral
volumen = pi * (radio ** 2) * height

print("El area total del cilindro es %.2f" % area_total, "y el volumen es %.2f" % volumen)