#Escribir un programa que genere la lista de 20 numeros aleatorios entre 1 y 15

from random import randint
list = [randint(1, 15) for x in range(20)]
print(list)