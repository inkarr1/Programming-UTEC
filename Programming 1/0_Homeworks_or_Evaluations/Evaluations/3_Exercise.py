# Desarrolle un programa que permita hallar el factorial de un número entero positivo mayor
# que cero.
# El programa debe validar el ingreso del dato, de tal manera que solo acepte números mayores
# o iguales a 1.

number = 0
while number <= 0:
    number = int(input("Número [mayor o igual a 1]: "))

i = 0
fact = 1

while i < number:
    i += 1
    fact = fact * i
print("El factorial es: ", fact)