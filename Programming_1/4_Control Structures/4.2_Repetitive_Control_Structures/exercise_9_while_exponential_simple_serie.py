# SERIE SIMPLE
# Dada la serie 1, 4, 9, 16, 25, 36,...
# Diseñe e implemente un algoritmo que permita al usuario ingresar la cantidad de números a mostrar.
# El algoritmo debe imprimir la secuencia: 1, 4, 9, 16, 25, 36,..., hasta el cuadrado del número n.

number = int (input("Ingrese un número: "))
i = 0

while i < number:
    i += 1

    print(i ** 2)