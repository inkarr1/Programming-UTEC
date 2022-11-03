import random

def crearMatriz():
    # creacion de la matriz
    for i in range(FILAS):
        M.append([0]*COLUMNAS)

def mostrarMatriz():
    #print(M)
    print("")
    for i in range(FILAS):
        for j in range(COLUMNAS):
            print(M[i][j], end=" ")
        print("")

def generarAleatorio():
    for i in range(FILAS):
        for j in range(COLUMNAS):
            M[i][j] = random.randint(-1,9)

def sumarColuma(col):
    suma=0
    for i in range(FILAS):
        suma += M[i][col]
    return suma

def buscarNegativos():
    flag=False
    for i in range(FILAS):
        for j in range(COLUMNAS):
            if M[i][j] < 0:
                flag = True
                return flag
    return flag

# MAIN
FILAS=4
COLUMNAS=6
M=[]

crearMatriz()
mostrarMatriz()
generarAleatorio()
mostrarMatriz()
print('\nSuma Columa 2: ',sumarColuma(2))
print('Negativos: ',buscarNegativos())
