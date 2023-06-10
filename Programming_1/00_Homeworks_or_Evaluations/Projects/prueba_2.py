# Crear el tablero vacío
tablero = [[0] * 9 for _ in range(9)]

# Función para imprimir el tablero
def imprimir_tablero(tablero):
    for fila in tablero:
        print(' '.join(map(str, fila)))

# Ejemplo de uso
imprimir_tablero(tablero)
