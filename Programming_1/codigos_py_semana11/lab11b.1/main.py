"""
#inputFile = open('covid-19-peru-camas-uci.csv', "r")
inputFile = open('C:\\Users\\jsilv\\PycharmProjects\\2022-2\\S11\\lab11b.1\\covid-19-peru-camas-uci.csv', "r")
i=0
for cadena in inputFile:
    print(cadena, end="")
    if i==5: break;
    i+=1


inputFile = open('covid-19-peru-camas-uci.csv', "r")
i=0
cadena = inputFile.readline()
while cadena != "":
    print(cadena,end="")
    cadena = inputFile.readline()
    if i==5: break;
    i+=1


inputFile = open('covid-19-peru-camas-uci.csv', "r")
cadenas = inputFile.readlines()
print(cadenas)
#print(len(cadenas))


inputFile2 = open('utec.txt', "w+")
inputFile2.write("UTEC " + "Prog1\n")
inputFile2.write("Bienvenidos al curso de Progamacion 1\n")
inputFile2.write("del 2022-1\n")
inputFile2.close()

"""
inputFile2 = open('utec.txt', "a")
inputFile2.write("Finalmente\n")
inputFile2.write("Bienvenidos al curso de Progamacion 1\n")
inputFile2.write("del 2022-1\n")
inputFile2.close()
