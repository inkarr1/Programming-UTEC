# Multiplos de 3 ó 5
# Si escribimos los números enteros positivos menores a 10, podremos darnos cuenta que el
# 3, 5, 6 y 9 son múltiplos de 3 ó 5. La suma de estos números es igual a 23. Desarrolle
# un programa que permita leer un entero positivo n y calcule todos los números enteros positivos
# menores a n múltiplos de 3 ó 5.

number = 0
while number <= 0 or number > 10:
    number = int(input("Ingrese un entero positivo: "))

i = 0
while i < number:
    i += 1
    if i % 3 == 0 and i % 5 == 0:
        print(i, "H")
