# Escribir un programa que permita ingresar un número del 1-7 y muestre su equivalente en letras.
# Ejemplo: 1 = Lunes, 2 = Martes, 3 = Miércoles, 4 = Jueves, etc. Si esta fuera el rango mostrar el mensaje error.

number_day = int(input("Ingresa el número del día de la semana: "))

if number_day == 1:
    print("Lunes")
elif number_day == 2:
    print("Martes")
elif number_day == 3:
    print("Miércoles")
elif number_day == 4:
    print("Jueves")
elif number_day == 5:
    print("Viernes")
elif number_day == 6:
    print("Sábado")
elif number_day == 7:
    print("Domingo")
else:
    print("No existe ese número de la semana")