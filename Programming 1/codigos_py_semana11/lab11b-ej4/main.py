palabra=""
i = 1
while palabra!="fin":
    palabra = input("Ingrese la palabra: ")
    if palabra=="fin":
        break
    inputFile1 = open('archivo' + str(i) +'.txt', "w")
    inputFile1.write(palabra + "\n")
    inputFile1.close()

    inputFile2 = open('archivo.txt', "a")
    inputFile2.write(palabra + "\n")

    i+=1
inputFile2.close()
