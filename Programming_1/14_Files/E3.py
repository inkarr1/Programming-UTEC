inputFile = open('../14_Files/python.txt', "r")
outputFile = open('/home/inkarri/GitHub/Programming-UTEC/Programming_1/14_Files/python2.txt' , "w")

cadenas = inputFile.readlines()
for linea in cadenas:
    outputFile.write(linea)

inputFile.close()
outputFile.close()
