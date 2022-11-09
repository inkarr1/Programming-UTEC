from random import randint

def generarMatrizAleatoria(filas,columnas):
    abecedario ="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in range(filas):
        F = []
        for j in range(columnas):
            F.append(abecedario[randint(1,25)])
        M.append(F)

def mostrarMatriz(M):
    print("")
    for i in range(len(M)):
        for j in range(len(M[0])):
            print(M[i][j], end=" ")
        print("")

def buscarMatriz(M, buscar):
    inicioF = -1
    inicioC = -1
    encontrado = False
    for i in range(len(M)):
        for j in range(len(M[0])):
            if buscar[0] == M[i][j]:
                inicioF=i
                inicioC=j
                encontrado= True
                for k in range(len(buscar)):
                    if buscar[k] != M[i][j+k]:
                        encontrado = False
            if encontrado:
                break
        if encontrado:
            break
    return inicioF, inicioC

filas = int(input("Ingrese las filas: "))
columnas = int(input("Ingrese las columnas: "))

M=[]
generarMatrizAleatoria(filas,columnas)
mostrarMatriz(M)

buscar = input("Ingrese las caraceteres a buscar: ")
inicioF, inicioC = buscarMatriz(M,buscar)
print("Los caracteres " + buscar + " se encuentran en las posiciones:")
print("Inicio:",inicioF,",",inicioC)
print("Fin:",inicioF,",",inicioC + len(buscar) -1)