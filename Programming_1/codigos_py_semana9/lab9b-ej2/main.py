def crearPanel():
    #creacion de la matriz
    for i in range(FILAS):
        M.append(["x"]*COLUMNAS)

def crearDigitos():
    global d1,d2
    d1=[
        [' ', ' ', 'x', ' ', ' '],
        [' ', 'x', 'x', ' ', ' '],
        ['x', ' ', 'x', ' ', ' '],
        [' ', ' ', 'x', ' ', ' '],
        [' ', ' ', 'x', ' ', ' '],
        [' ', ' ', 'x', ' ', ' '],
        ['x', 'x', 'x', 'x', 'x']
        ]
    d2=[
        ['x', 'x', 'x', 'x', 'x'],
        [' ', ' ', ' ', ' ', 'x'],
        [' ', ' ', ' ', ' ', 'x'],
        ['x', 'x', 'x', 'x', 'x'],
        ['x', ' ', ' ', ' ', ' '],
        ['x', ' ', ' ', ' ', ' '],
        ['x', 'x', 'x', 'x', 'x']
        ]

def mostrarDigito(digito):
    print("")
    for i in range(len(digito)):
        for j in range(len(digito[0])):
            print(digito[i][j], end="")
        print("")

# MAIN
FILAS=7
COLUMNAS=7*4
M=[]
d1=[]
d2=[]
#crearPanel()
#mostrarDigito(M)
crearDigitos()
#mostrarDigito(d1)
#mostrarDigito(d2)

#mostrarDigito(d1 + d2)

d3=[]
for i in range(FILAS):
    d3.append(d1[i] + [" "," "] + d2[i])
mostrarDigito(d3)


d4=[]
for i in range(FILAS):
    d4.append(d1[i] + [" "," "] + d2[i] + [" "," "] + d1[i] + [" "," "] + d2[i])
mostrarDigito(d4)
