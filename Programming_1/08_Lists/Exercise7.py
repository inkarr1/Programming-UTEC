# Dado el siguiente texto:

texto = "10, 20, 33, 40, 11, 90"

# Escribir un programa que genere una lista con 6 valores numéricos incluidos
# en el texto y luego calcular la suma de aquellos valores múltiplos de 10.

list = [int(x) for x in texto.split(', ')]
print(list)

sum_list = sum([x for x in list if x % 10 == 0])
print(sum_list)