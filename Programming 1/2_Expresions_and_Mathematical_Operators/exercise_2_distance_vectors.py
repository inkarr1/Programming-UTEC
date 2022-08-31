# Desarrolle un programa que permita hallar la distancia entre dos puntos.
# Puede utilizar la siguiente fórmula para calcular la distancia:

# Distancia = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 1/2

x1 = int(input("Ingrese x1: "))
y1 = int(input("Ingrese y1: "))
x2 = int(input("Ingrese x2: "))
y2 = int(input("Ingrese y2: "))

distance = ((x2 - x1) ** 2 + (y2-y1) ** 2) ** 0.5

print("La distancia es: ", distance)