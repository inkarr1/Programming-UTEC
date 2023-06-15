import random

# Función para generar una letra aleatoria
abecedario = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")


# Función para generar una matriz de letras aleatoria
def generar_matriz(filas, columnas):
    matriz = []
    for i in range(filas):
        fila = [random.choice(abecedario) for j in range(columnas)]
        matriz.append(fila)
    return matriz


# Función para mostrar la matriz
def mostrar_matriz(matriz):
    for fila in matriz:
        print(' '.join(fila))


# Función para obtener el string vertical
def obtener_string_vertical(matriz, fila_inicio, columna_inicio, tamano):
    filas = len(matriz)
    columnas = len(matriz[0])

    if (fila_inicio + tamano) > filas:
        return "No se puede generar el string"

    string_vertical = ""
    for i in range(fila_inicio, fila_inicio + tamano):
        if columna_inicio >= columnas:
            return "No se puede generar el string"
        string_vertical += matriz[i][columna_inicio]

    return string_vertical


# Solicitar dimensiones de la matriz al usuario
filas = int(input("Ingrese las filas: "))
columnas = int(input("Ingrese las columnas: "))

# Generar matriz aleatoria
matriz = generar_matriz(filas, columnas)

# Mostrar matriz generada
#print("Matriz generada:")
mostrar_matriz(matriz)
print()
# Solicitar posición de inicio, tamaño del string
fila_inicio = int(input("Ingrese la posición de inicio de fila: "))
columna_inicio = int(input("Ingrese la posición de inicio de columna: "))
tamano = int(input("Ingrese el tamaño del string: "))

# Obtener el string vertical
resultado = obtener_string_vertical(matriz, fila_inicio, columna_inicio, tamano)

# Mostrar el resultado
print("\nResultado:")
print(resultado)
