"""
paises = [ "Argentina", "Bolivia", "Brasil", "Chile",
        "Colombia", "Ecuador", "Mexico", "Paraguay",
        "Perú", "Uruguay", "Venezuela"]
pbi = [
    [2.9 , 2.5],
    [3.9 , 4.0],
    [0.9 , 2.2],
    [1.5 , 3.3],
    [1.8 , 2.6],
    [1.0 , 2.0],
    [2.2 , 2.3],
    [4.0 , 4.0],
    [2.5 , 3.5],
    [3.0 , 3.0],
    [-9.5 , -8.5]
    ]
#print(len(pbi[0]))
print(pbi[2][1])

print('{:^15}'.format("País"),2017,"\t", 2018)
for i in range(len(paises)):
    print('{:^15}'.format(paises[i]),pbi[i][0],"\t", pbi[i][1])

"""

PAISES = 11
AÑOS = 2
paises = [ "Argentina", "Bolivia", "Brasil", "Chile", "Colombia",
          "Ecuador", "Mexico", "Paraguay", "Perú", "Uruguay", 
          "Venezuela"]
pbi = [ [2.9 , 2.5], [3.9 ,  4.0], [0.9 ,  2.2],[1.5 , 3.3],
        [1.8 , 2.6], [1.0 , 2.0],  [2.2 , 2.3], [4.0 , 4.0],
        [2.5 , 3.5], [3.0 , 3.0], [-9.5 , -8.5] ]
print("            2017    2018")
for i in range(PAISES):
    print("%10s"%paises[i], end="   ")
    for j in range(AÑOS):
        print("{0:.1f}".format(pbi[i][j]), end="\t")
    print()
