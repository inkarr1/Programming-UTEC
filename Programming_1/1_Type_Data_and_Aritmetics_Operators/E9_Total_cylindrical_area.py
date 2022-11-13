# Desarrolle un programa que permita hallar el área total de la superficie cilíndrica y el volumen de un cilindro circular recto,
# si se conocen las siguientes fórmulas:

# At = Ab + Al
# Ab = 2 * pi * (r ** 2)
# Al = 2 * pi * r * h
# V = (pi ** 2) * h

# Donde:
# At = Area totol de la superficie cilindrica
# Ab = Area de las bases
# Al = Area lateral
# V = volumen

radio = int(input("Ingrese el radio: "))
height = int(input("Ingrese la altura: "))
pi = 3.14

area_base = 2 * pi * (radio ** 2)
area_lateral = 2 * pi * radio * height

area_total = area_base + area_lateral
volumen = pi * (radio ** 2) * height

print("El area total del cilindro es", area_total, "y el volumen es", volumen)