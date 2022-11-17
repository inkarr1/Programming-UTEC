from math import pi, tan

s = int(input("Ingrese la longitud de los lados: "))
n = int(input("Ingrese el número de lados: "))

area = (n * (s**2)) / 4 * tan(pi/n)

print("Área del polígono regular es: ", area)