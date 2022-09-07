# Diseñe e implemente un algoritmo en Python que obtenga el promedio de un conjunto de números
# ingresados por el usuario. El usuario ingresará cero para indicar que ya no ingresará más
# números. El cero no se considera en el promedio.

n = 0
i = 0
suma = 0

while n >= 0:
    n = int(input(""))

    if n > 0:
        i += 1
        suma += n
    elif n == 0:
        break

print(suma / i)
