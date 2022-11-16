import ramdom as rn

def busquedaBinaria(lista, busqueda):
    #print(lista)
    if len(lista) == 1:
        return lista[0] == busqueda
    mid = len(lista) // 2
    if lista[mid] == busqueda:
        return True
    elif busqueda < lista[mid]:
        return busquedaBinaria(lista[:mid], busqueda)
    else:
        return busquedaBinaria(lista[mid + 1:], busqueda)

def leerDatoMayor
    n = 0
