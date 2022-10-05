# TABLA DE MULTIPLICAR
# Desarrolle un programa que imprima la tabla de multiplicar de un número n ingresado por teclado.

number = int(input("Ingrese el número de la tabla: "))

i = 1

while i <= 12:
    print(str(number) + "x" + str(i) + "=", number*i)
    i += 1