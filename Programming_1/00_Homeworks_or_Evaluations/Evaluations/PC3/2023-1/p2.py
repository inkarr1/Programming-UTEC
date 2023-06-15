import random

abecedario = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
matriz = []

filas = int(input("Ingrese la posición de inicio de fila: "))
columnas = int(input("Ingrese la posición de inicio de columnas: "))


for i in range(filas):
    fila = [random.choice(abecedario) for j in range(columnas)]
    matriz.append(fila)

for fila in matriz:
    print(' '.join(fila))


fila_inicio = int(input("Ingrese la posición de inicio de fila: "))
columna_inicio = int(input("Ingrese la posición de inicio de columna: "))
tamano = int(input("Ingrese el tamaño del string: "))


filas = len(matriz)
columnas = len(matriz[0])
string = ""

if fila_inicio >= filas or columna_inicio >= columnas:
    print("Resultado: ")
    print("No se puede generar el string")
elif columna_inicio + tamano > columnas:
    print("Resultado: ")
    print("No se puede generar el string")
else:
    for i in range(tamano):
        letra = matriz[fila_inicio][columna_inicio + i]
        string += letra
    print("Resultado: ")
    print(string)

