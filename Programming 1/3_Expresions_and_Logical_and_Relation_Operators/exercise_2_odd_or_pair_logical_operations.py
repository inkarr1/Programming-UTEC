# Desarrolle un programa que permita leer un numero entero y el programa indique si el
# numero es par o impar.
# Realice el programa sin utilizar estructuras de control.

number = int(input("Number: "))

# numero = int(input("Ingrese un numero entero: ")
# par = (numero%2==0)
# impar = (numero%2!==0)
# print("El numero es: " + ((par)*"par") + ((impar)*"impar")

result = "Es" + " " + ("im" * (number % 2 == 1)) + "par"

print(result)