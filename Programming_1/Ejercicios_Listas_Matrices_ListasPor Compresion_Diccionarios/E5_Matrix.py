import random

def mostrarMatriz(M):
    print("")
    for i in range(len(M)):
        for j in range(len(M[0])):
            print(M[i][j], end=" ")
        print("")

def mostrarMatrizH(M,medio):
    print("")
    for i in range(len(M)):
        for j in range(len(M[0])):
            if i == medio:
                print(M[i][j], end=" ")
            else:
                if (j==0 or j==columnas-1):
                    print(M[i][j], end=" ")
                else: print(" ", end=" ")
        print("")


def generarMatrizAleatoria(filas,columnas):
    for i in range(filas):
        F = []
        for j in range(columnas):
            F.append(random.randint(0,9))
        M.append(F)

def sumarBorde():
    suma=0
    for i in range(len(M)):
        suma += M[i][0]
        suma += M[i][len(M[0]) - 1]
    #sumaLista = [M[i][0] + M[i][len(M[0]) - 1] for i in range(len(M))]
        #print(M[i][0],M[i][len(M[0]) - 1])
    for j in range(1, len(M[0]) - 1):
        suma += M[0][j]
        suma += M[len(M) - 1][j]
        #print(M[0][j],M[len(M) - 1][j])
    return suma

def sumarMatrizH(medio):
    suma=0
    for i in range(len(M)):
        suma += M[i][0]
        suma += M[i][len(M[0]) - 1]
    for j in range(1, len(M[0]) - 1):
        suma += M[medio][j]
    return suma

def sumarBordeCompresion():
    suma=0
    sumaL=[]
    sumaL = [M[i][0] + M[i][len(M[0]) - 1] for i in range(len(M))]
    suma += sum(sumaL)
    sumaL = [M[0][j] + M[len(M) - 1][j] for j in range(1, len(M[0]) - 1)]
    suma += sum(sumaL)
    return suma

# MAIN
filas=0;
while filas < 2:
    filas = int(input("Ingrese las filas: "))
columnas = 0;
while columnas < 2:
    columnas = int(input("Ingrese las columnas: "))

M=[]

generarMatrizAleatoria(filas,columnas)
mostrarMatriz(M)
medio=filas//2
mostrarMatrizH(M,medio)
print('\nLa suma de los números es: ', sumarMatrizH(medio))
#print('Negativos: ',buscarNegativos())
