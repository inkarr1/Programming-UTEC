frase = input("Ingrese frase")
vocales="aeiou"
nuevaFrase = [x for x in frase if x not in vocales]
print(nuevaFrase)
