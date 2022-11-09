from random import randint

def mostrarMatriz(M):
    print("")
    for i in range(len(M)):
        for j in range(len(M[0])):
            print(M[i][j], end=" ")
        print("")

def generarMatrizAleatoria(filas,columnas):
    for i in range(filas):
        F = []
        for j in range(columnas):
            F.append(randint(1,9))
        M.append(F)

def disparo(fila, columna):
    ochos = 0
    for i in range(len(M)):
        if (M[i][columna]) ==8:
            ochos+=1
        M[i][columna] = 0
    for j in range(0, len(M[0])):
        if (M[fila][j]) ==8:
            ochos+=1
        M[fila][j] = 0
    return ochos

filas=0;
while filas < 3:
    filas = int(input("Ingrese las filas: "))
columnas = 0;
while columnas < 3:
    columnas = int(input("Ingrese las columnas: "))

M=[]
generarMatrizAleatoria(filas,columnas)
mostrarMatriz(M)
print("Ingrese las coordenadas para el disparo: ")
fila = int(input("fila: "))
columna = int(input("columna: "))
bomberman = disparo(fila,columna)
mostrarMatriz(M)
print('Se eliminaron a ', bomberman, 'enemigos')