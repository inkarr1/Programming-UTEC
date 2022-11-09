inputFile = open('python.txt', "r")
outputFile = open('C:\\Users\\\jsilv\\\Downloads\\python.txt', "w")
cadenas = inputFile.readlines()
for linea in cadenas:
    outputFile.write(linea)

inputFile.close()
outputFile.close()