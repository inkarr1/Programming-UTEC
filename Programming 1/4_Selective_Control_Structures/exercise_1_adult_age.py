# Elaborar un algoritmo y un programa que solicite el nombre y la edad de una persona.
# Deberá imprimir un saludo: "Hola <nombre>". Además, otro mensaje si la persona tiene
# 18 años : "Usted debe tramitar ante RENIEC su DNI de mayor de edad".

name = input("Ingrese su nombre: ")
age = int(input("Ingrese su edad: "))

print("Hola " + name)

if age == 18:
    print("Usted debe tramitar ante RENIEC su DNI de mayor de edad")