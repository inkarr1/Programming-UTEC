# Sin crear una lista adicional y sin usar slicing, invierta una lista.

# input: [1, 2, 3, 4, 5]
# output: [5, 4, 3, 2, 1]

lista_normal = [1, 2, 3, 4, 5]

print(lista_normal[::-1])

print(lista_normal[-1:-len(lista_normal)-1:-1])

for i in range((len(lista_normal)//2)):
    temp = lista_normal[len(lista_normal) - i -1]
    lista_normal[len(lista_normal) - i - 1] = lista_normal[i]
    lista_normal[i] = temp
print(lista_normal)