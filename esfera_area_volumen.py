#Escribe un programa en Python que permita hallar el area y el volumen de una esfera.

radio = float(input("Ingrese el radio de la esfera: "))
pi = 3.14

area = 2 * pi * (radio) ** 2
volumen = 4 / 3 * pi * (radio) ** 3

print(f"Area es igual a {area} y el volumen {volumen}")