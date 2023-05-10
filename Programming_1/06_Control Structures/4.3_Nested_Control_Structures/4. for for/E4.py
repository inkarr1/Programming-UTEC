tam = int(input("filas: "))

for i in range(1, tam + 1):
    for j in range(1, tam - i +1):
        print(" ", end="")
    for j in range(1, i * 2):
        print(j % 10, end="")
    print("")