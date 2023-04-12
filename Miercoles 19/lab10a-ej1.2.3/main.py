"""
lista1 = [x for x in range(0, 51) if x % 2 != 0 and x % 3 != 0]
print(lista1)
"""

"""
from random import randint
lista3 = [randint(1, 15) for x in range(20)]
print(lista3)

"""
texto = "10,20, 33, 40, 11, 90"

lista = [int(x) for x in texto.split(',')]
print(lista)

suma = sum([x for x in lista if x % 10 == 0])
print(suma)
