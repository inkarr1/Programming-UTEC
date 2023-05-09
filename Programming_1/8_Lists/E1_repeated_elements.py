# Dado una lista de valores, escriba un programa que permita identificar si un
# elemento se repite varias veces, luego proceder a dejar solo la primera ocurrencia
# del elemento y eliminar el resto de apariciones.

# input: [5, 8, 4, 7, 6, 2, 1, 9, 8, 4, 3, 2, 8]
# output: [5, 8, 4, 7, 6, 2, 1, 9, 3]

lista_general = [5, 8, 4, 7, 6, 2, 1, 9, 8, 4, 3, 2, 8]

lista_filtrada = []

for elemento_lista in lista_general:
    if elemento_lista not in lista_filtrada:
        lista_filtrada.append(elemento_lista)
print(lista_filtrada)

for i in range(len(lista_general)-1):
    for j in range(i+1, len(lista_general)):
        if j > len(lista_general)-1:
            break
        if lista_general[i] == lista_general[j]:
            #del lista_general[j]
            lista_general.pop(j)
    print(lista_general)