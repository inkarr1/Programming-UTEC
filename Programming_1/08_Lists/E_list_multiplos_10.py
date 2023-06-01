texto = "10, 20, 33, 40, 11, 90"

lista = [int(x) for x in texto.split(',')]
print(lista)

suma = sum([x for x in lista if x % 10 == 0])
print(suma)
