# Realice un programa que permita leer la edad de una persona y el programa determine el costo
# de la entrada del cine, según la tabla:
# |  Edad      |  Precio en soles  |
# |------------|-------------------|
# |  0-17      |  15               |
# |  18- 30    |  25               |
# |  31 - 45   |  30               |
# |  46 a mas  |  10               |

age = int(input("Ingrese la edad: "))

if 0 <= age <= 17:
    print("El costo de la entrada es s/.15")
elif 18 <= age <= 30:
    print("El costo de la entrada es s/.25")
elif 31 <= age <= 45:
    print("El costo de la entrada es s/.30")
else:
    print("El costo de la entrada es s/.10")