# Escribir  un programa que permita leer como dato un número entero y luego imprima si
# es positivo, negativo o es cero.

number = int(input("Ingrese número: "))

if number > 0:
    print("Positivo")
elif number < 0:
    print("Negativo")
else:
    print("Es cero")