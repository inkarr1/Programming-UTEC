def imprimir_tablero(tablero):
    for fila in tablero:
        for elemento in fila:
            print("[{:>3}]".format(elemento), end=' ')
        print()

# Pedir al usuario las dimensiones del tablero
filas = int(input("Ingresa el número de filas: "))
columnas = int(input("Ingresa el número de columnas: "))

# Crear un tablero con las dimensiones ingresadas por el usuario
tablero = [[j + 1 + i * 4 for j in range(columnas)] for i in range(filas)]

# Imprimir el tablero
imprimir_tablero(tablero)

