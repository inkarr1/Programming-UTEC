# Haciendo uso de un diccionario, implemente un algoritmok que permita determinar
# cuántas veces se repite cada carácter de un string. Considere que su algoritmo debe
# considerar cualquier caracter (letras, números, símbolos, etc.) excepto espacios en
# blanco.

# Input: aabbaa
# Output: a: 5, b: 2

# Input: hola como estas
# Output: h: 1, o: 3, l: 1, a: 2, c: 1, m: 1, e: 1, s: 2

# Ingrese frase: Sacare 20 en esta practica
# Output: {"s": 2, "a": 5, "c": 3, "r": 2, "e": 3, "2": 1, "0": 1, "n": 1, "t": 2, "i": 1}
phrase = input("Input: ")
d = {}

for letter in phrase:
    if letter in d.keys():
        d[letter] = d[letter] + 1
    else:
        d[letter] = 1

print(d)

for key in d.keys():
    print(key + ":", d[key], end=", ")