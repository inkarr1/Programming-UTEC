frase = input("Frase: ")
vocales = "aeiou"
nuevaFrase = [l for l in frase if l not in vocales]
print(nuevaFrase)
