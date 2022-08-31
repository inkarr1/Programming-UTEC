# Un poligono regular es aquel que tiene longitud de sus lados iguales y el angulo
# entre los lados adyacentes es igual. Desarrolle un programa que permita calcular
# el area de un pologino regular.

# Puede calcular el area de un poligono regular utilizando la siguiente formula:
# area = (n * (s**2)) / 4 * tan(pi/n)

# Donde
# s es la longitud de los lados
# n es el numero de lados

# NOTA: Para calculo se requiere de PI y llamar a la funcion tan en la biblioteca
# math:from math import pi, tan

from math import pi, tan

s = int(input("Ingrese la longitud de los lados: "))
n = int(input("Ingrese el número de lados: "))

area = (n * (s**2)) / 4 * tan(pi/n)

print("Área del polígono regular es: ", area)