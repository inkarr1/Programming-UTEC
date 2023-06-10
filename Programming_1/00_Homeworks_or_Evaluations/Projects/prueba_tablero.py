filas = 2
columnas = 3

# Crear una matriz de matrices vacía
matriz = []

# Llenar la matriz con matrices internas
for i in range(filas):
    fila = []
    for j in range(columnas):
        submatriz = [[i, j], [i+j, i-j]]
        fila.append(submatriz)
    matriz.append(fila)

# Imprimir la matriz de matrices
for fila in matriz:
    for submatriz in fila:
        print(submatriz)
    print()
