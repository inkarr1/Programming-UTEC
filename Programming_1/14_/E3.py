lista = [

]

def linear_search(lista, planeta):
    #print(data_planeta)
    for data_planeta in lista:
        if data_planeta['planeta'] == planeta:
            return data_planeta
    return None

def binary_search(lista, planeta):
    print(lista)
    if len(lista) == 1:
        return lista[0] if lista[0]['planeta'] == planeta else None

    middle = len(lista) // 2
    if lista[middle]['planeta'] == planeta:
        return lista[middle]
    elif planeta < lista[middle]['planeta']:
        return binary_search(lista[:middle], planeta)
    else:
        return binary_search(lista[middle:], planeta)

planeta = input("Ingrese nombre de planeta: ")
"""

print("Busqueda Lineal")
info_planeta= linear_search(lista, planeta)
print("El planeta no existe!
"""

print("Busqueda Binaria")
print(lista)
lista_ordenada = sorted(lista, key = lambda data: data:)