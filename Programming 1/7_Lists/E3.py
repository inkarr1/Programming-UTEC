# Sin recorrer explícitamente la lista de inicio a fin, encuentre todas
# las posiciones en las que se encuentra un elemento determinado en una lista.

# input: [8, 4, 3, 2, 1, 5, 6, 2, 1, 4, 5, 8, 9]
# Research_number: 2
# output: 3, 7
lista_general = [8, 4, 3, 2, 1, 5, 6, 2, 1, 4, 5, 8, 9]

repetead = int(input("Ingrese el numero a encontrar: "))

i = 0

while True:
    if repetead in lista_general:
        idx = lista_general.index(repetead)
        print(idx + i, end=" ")
        del lista_general[idx]
        i += 1
    else:
        break