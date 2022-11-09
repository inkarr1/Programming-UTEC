PAISES = 5
TIPOS_MEDALLA = 3
nombres_paises = [ "Estados Unidos", "Unión Soviética", "Reino Unido",
               "China", "Alemania"]
medallas = [
        [1022, 794, 704],
        [395, 319, 296],
        [263, 295, 289],
        [227, 163, 153],
        [219, 246, 269]
       ]
print("%17s"%" ","  ORO   PLATA   BRONCE")
for i in range(PAISES):
     print("%17s"%nombres_paises[i], end = " ")
     for j in range(TIPOS_MEDALLA):
           print("%6d" % medallas[i][j], end = " ")
     print()
"""
total = 0
i=3
for j in range(TIPOS_MEDALLA) :  
    total = total + medallas[i][j]
print("\nEl total de medallas de China: ", total)

"""
"""
total = 0
j = 2
for i in range(PAISES) :
    total = total + medallas[i][j]
print("\nEl total de medallas de bronce: ", total)

"""
suma = 0
for i in range(PAISES):
    for j in range(TIPOS_MEDALLA):
        suma = suma + medallas[i][j]
print ("\nLa cantidad total de medallas es: ", suma)
