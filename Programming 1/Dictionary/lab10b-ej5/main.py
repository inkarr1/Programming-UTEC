dni = 0
i=0
d = {}
while dni!=-1:
    dni = input("DNI " + str(i+1) + ": ")
    tam = len(dni)
    dni = int(dni)
    if dni == -1:
        break
    elif tam != 8:
        print("DNI incorrecto")
    else:
        if dni not in d.values():
            d[len(d)+1] = dni
    i+=1
print("El DNI con el valor máximo es:", max(d.values()))
print(d)

