
DIVISIONES = 5
TRIMESTRES = 3

divisiones = ["Línea Blanca", "Electrodomésticos", "Juguetería",
              "Perecibles", "Limpieza"]

datos = [[450, 650, 342], [340, 487, 767], [134, 212, 354],
         [180, 464, 565], [647, 324, 232]]

"""
suma = 0
i = 2   # fila i
for j in range(TRIMESTRES):  
    suma = suma + datos[i][j]
print("\nEl total de ventas de la División Juguetería es: ", suma)

"""
suma = 0
j = 1
for i in range(DIVISIONES) :  
    suma = suma + datos[i][j]
print("\nEl total de ventas del segundo Trimestre es: ", suma)
