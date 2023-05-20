# Seleccione la cantidad de veces que el programa imprime en consola
# No es neceario saber el valor de x para hallar el resultado

# x fue definido previamente
x = 7
x = x * x
temp = x ** 0.5

while x > temp:
    print((x ** 2) + (26 % 12) - ((x * 4) ** 2))
    x -= temp

# x -1