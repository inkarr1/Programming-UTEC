# PROMEDIO DE UN CONJUNTO DE NÚMEROS
# Diseñe e implemente un algoritmo en Python que obtenga el promedio de un conjunto
# de números ingresados por el usurio. El usuario ingresará cero para indicar que ya
# no ingresará más números. EL cero no se considera en el promedio.

number = int(input("Ingrese un número: "))

suma = number
i = 1

while number != 0:
    number = int(input("Ingrese un número: "))

    if number == 0: continue
    suma += number
    i += 1
print(suma/i)