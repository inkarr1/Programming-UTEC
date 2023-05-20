texto = input("Ingrese un string: ")
letras = [c for c in texto if c.isalpha()]
especiales = ['[', '(', '*']
resultado = list(texto)

for i in range(len(letras)):
    letra_actual = letras[i]
    indice_actual = texto.index(letra_actual)
    siguiente_letra = letras[(i + 1) % len(letras)]

    resultado[indice_actual] = siguiente_letra

resultado[texto.index(letras[0])] = letras[-1]

resultado = ''.join(resultado)
print("El resultado es:", resultado)
