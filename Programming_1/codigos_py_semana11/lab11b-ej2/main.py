inputFile = open('python.txt', "r")
cadenas = inputFile.readlines()
cantPalabras = 0
for linea in cadenas:
    palabras = linea.split(" ")
    cantPalabras += len(palabras)
print(cantPalabras)