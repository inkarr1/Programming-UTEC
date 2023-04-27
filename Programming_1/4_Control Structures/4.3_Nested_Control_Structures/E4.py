cantPar = 0
cantImpar = 0
i = 0

while num != 0:
    num = int(input("Número [con 0 termina]: "))

    if num != 0 and num % 2 == 0:
        cantPar += 1
    elif num != 0:
        cantImpar += 1
    i += 1

print("Números leídos", i - 1)
print("Números pares", cantPar)
print("Números impares", cantImpar)