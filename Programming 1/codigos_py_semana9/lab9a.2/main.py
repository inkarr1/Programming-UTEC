"""
matriz=[]
FILAS = 4
COLUMNAS = 6

for i in range(FILAS) :
    fila = [0] * COLUMNAS
    matriz.append(fila)

for i in range(FILAS):
    for j in range(COLUMNAS):
        print(matriz[i][j],end=" ")
    print("")

"""



from random import randint
matriz=[]
FILAS = 4
COLUMNAS = 6

for i in range(FILAS) :
    fila = []
    for j in range(COLUMNAS):
        fila.append(randint(0,9))
    matriz.append(fila)

for i in range(FILAS):
    for j in range(COLUMNAS):
        print(matriz[i][j],end=" ")
    print("")
