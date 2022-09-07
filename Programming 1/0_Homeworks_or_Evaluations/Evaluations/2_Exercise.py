# Desarrolle un programa que permita hallar la sumatoria de la siguiente serie:

# La serie corresponde a los número naturales, en donde cada número es elevado a la quinta. Se pide que realice
# un programa que lea como datos el número del término y halle la suma de los términos de sereie desde 1 hasta
# el número que se ingresó como dato.

n = int(input("Valor de N :"))
i = 0
suma = 0

while i < n:
    i += i
    suma = suma + i ** 5
print("La suma es:", suma)