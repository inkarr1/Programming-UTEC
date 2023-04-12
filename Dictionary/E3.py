# Diseñe e implemente un algoritmo que reciba como datos de entrada un texto,
# y proceda a extraer todas las palabras del texto asociando la cantidad de veces
# que se repite dicha palabra en el texto. Use un diccionario para guardar cada
# palabra diferente y las veces que se repite.

# Input: Hola Como Estas hola como estas HOLA
# Output: {'hola': 3, 'como': 2, 'estas': 2}

# Input: Cuando cuentes cuentos cuenta cuantos cuentos cuentas porque si cuentas cuantos
# cuentos cuentas sabras cuantos cuentos sabes contar
#Output: {'cuando': 1, 'cuentes': 1, 'cuentos': 4, 'cuenta': 1, 'cuantos': 3, 'cuentas': 3, porque: 1, si:1 sabras:!, sabes:1 contar:1}

texto = input("Input: ")
texto = texto.lower()
lista = texto.split(' ')
print(lista)

d={}
for palabra in lista:
    if palabra in d.keys():
        d[palabra] =d[palabra]+1
    else:
        d[palabra] = 1

print(d)
