Lista = [2, 3, 8, 4, 7, 9, 8, 2, 6, 5, 1, 6, 1, 2, 3, 4, 6, 9, 1, 2]

maxRepeticiones = 0
maxNumero = -1
for elem in Lista:
    repeticiones = Lista.count(elem)
    if repeticiones>maxRepeticiones:
        maxRepeticiones=repeticiones
        maxNumero = elem

print("[" + str(maxNumero)+"] ---> " + str(maxRepeticiones) +" veces")