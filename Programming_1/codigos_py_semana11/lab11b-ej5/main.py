inputFile = open('python.txt', "r")
outputFile = open('python-inverso.txt', "w")
cadenas = inputFile.readlines()
for i in range(len(cadenas)-1,-1,-1):
    outputFile.write(cadenas[i])
outputFile.close()
