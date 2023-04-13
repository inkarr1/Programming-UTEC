
def generarMatriz(filas,columnas):
    for i in range(filas):
        dots = []
        for j in range(columnas):
            dots.append(".")
        matriz.append(dots)
def mostrarMatriz(matriz):
    print("")
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            print(matriz[i][j], end=" ")
        print("")
def mostrarMatrizU(matriz,medio):
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if i == medio:
                print(matriz[i][j], end=".")
            else:
                if (j==0 or j==columnas-1):
                    print(M[i][j], end=".")
                else: print(" ", end=".")
        print("")

print("Ingrese posición de inicio: ")
px_fila = int(input("Fila: "))
py_colum = int(input("Columna: "))
size_u = int(input("Ingrese tamaño de la letra U: "))

matriz = []

generarMatriz(9, 9)
mostrarMatriz(matriz)
medio= 9//2
mostrarMatrizU(matriz,medio)