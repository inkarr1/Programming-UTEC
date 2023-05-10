# Escribir un programa que genere la lista de números entre 0 y 50
# que no sean pares y que no sean multiplos de 3.

list = [x for x in range(0,50,1) if x%2 != 0 and x%3 != 0]
print(list)